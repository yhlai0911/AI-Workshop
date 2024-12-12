import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from pathlib import Path
import time
import re

def get_llamaindex_links(url, visited_links=None, depth=0, max_depth=10):
    """遞迴爬取 LlamaIndex 文件連結，限定在 understanding 目錄下"""
    if visited_links is None:
        visited_links = set()
    
    if url in visited_links or depth > max_depth:
        return []
    
    visited_links.add(url)
    print(f"{'  ' * depth}正在爬取: {url}")
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        
        unique_links = set()
        base_url = "https://docs.llamaindex.ai"
        # target_path = "/en/stable/understanding/"
        target_path = "/en/stable/module_guides/"
        
        for link in links:
            href = link.get('href')
            if href:
                # 忽略錨點連結和外部連結
                if href.startswith('#') or href.startswith('http') and not href.startswith(base_url):
                    continue
                
                # 處理相對路徑
                if href.startswith('/'):
                    full_url = base_url + href
                else:
                    full_url = urljoin(url, href)
                
                parsed_url = urlparse(full_url)
                
                # 只處理 LlamaIndex 文檔網站的連結，且必須在 understanding 目錄下
                if parsed_url.netloc == 'docs.llamaindex.ai' and target_path in parsed_url.path:
                    clean_url = base_url + parsed_url.path
                    if clean_url not in visited_links:
                        unique_links.add(clean_url)
                        # 遞迴爬取子頁面的連結
                        time.sleep(1)  # 加入延遲避免請求過於頻繁
                        sub_links = get_llamaindex_links(clean_url, visited_links, depth + 1, max_depth)
                        unique_links.update(sub_links)
        
        return sorted(unique_links)
    
    except requests.RequestException as e:
        print(f"{'  ' * depth}請求錯誤 {url}: {e}")
        return []
    except Exception as e:
        print(f"{'  ' * depth}處理錯誤 {url}: {e}")
        return []

def get_page_content(url, headers):
    """抓取頁面內容並轉換為 Markdown 格式，保留所有連結"""
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 找到主要內容區域
        main_content = soup.find('article')
        if not main_content:
            main_content = soup.find('main')
        if not main_content:
            main_content = soup
            
        # 移除不需要的元素
        for element in main_content.find_all(['script', 'style', 'nav', 'footer']):
            element.decompose()
        
        # 提取標題
        title = soup.find('h1')
        title_text = title.text.strip() if title else url.split('/')[-2].replace('-', ' ').title()
        
        # 組合 Markdown 內容
        md_content = [f"# {title_text}\n\n"]
        md_content.append(f"原始連結：{url}\n\n")
        
        # 處理內容
        for element in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'pre', 'code', 'ul', 'ol', 'li', 'blockquote', 'a']):
            if element.name.startswith('h'):
                level = int(element.name[1])
                md_content.append(f"{'#' * level} {element.text.strip()}\n\n")
            elif element.name == 'p':
                if element.text.strip():
                    # 處理段落中的連結
                    p_content = element.text.strip()
                    links = element.find_all('a')
                    for link in links:
                        href = link.get('href')
                        if href:
                            if href.startswith('/'):
                                href = f"https://docs.llamaindex.ai{href}"
                            elif not href.startswith(('http://', 'https://')):
                                href = urljoin(url, href)
                            p_content = p_content.replace(link.text, f"[{link.text}]({href})")
                    md_content.append(f"{p_content}\n\n")
            elif element.name in ['pre', 'code']:
                code = element.text.strip()
                if code:
                    md_content.append(f"```\n{code}\n```\n\n")
            elif element.name == 'blockquote':
                quote_content = element.text.strip()
                links = element.find_all('a')
                for link in links:
                    href = link.get('href')
                    if href:
                        if href.startswith('/'):
                            href = f"https://docs.llamaindex.ai{href}"
                        elif not href.startswith(('http://', 'https://')):
                            href = urljoin(url, href)
                        quote_content = quote_content.replace(link.text, f"[{link.text}]({href})")
                md_content.append(f"> {quote_content}\n\n")
            elif element.name == 'li':
                if element.parent.name in ['ul', 'ol'] and element.parent.find_parent(['ul', 'ol']) is None:
                    prefix = "- " if element.parent.name == 'ul' else f"1. "
                    # 處理列表項中的連結
                    li_content = element.text.strip()
                    links = element.find_all('a')
                    for link in links:
                        href = link.get('href')
                        if href:
                            if href.startswith('/'):
                                href = f"https://docs.llamaindex.ai{href}"
                            elif not href.startswith(('http://', 'https://')):
                                href = urljoin(url, href)
                            li_content = li_content.replace(link.text, f"[{link.text}]({href})")
                    md_content.append(f"{prefix}{li_content}\n")
            elif element.name == 'a' and element.parent.name not in ['p', 'li', 'blockquote']:
                # 處理獨立的連結
                href = element.get('href')
                if href:
                    if href.startswith('/'):
                        href = f"https://docs.llamaindex.ai{href}"
                    elif not href.startswith(('http://', 'https://')):
                        href = urljoin(url, href)
                    md_content.append(f"[{element.text.strip()}]({href})\n\n")
        
        return title_text, ''.join(md_content)
    
    except Exception as e:
        print(f"處理頁面 {url} 時發生錯誤：{e}")
        return None, None

def save_to_markdown(title, content, output_dir):
    """將內容保存為 Markdown 檔案"""
    try:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        filename = re.sub(r'[^\w\s-]', '', title.lower())
        filename = re.sub(r'[-\s]+', '-', filename)
        filepath = output_dir / f"{filename}.md"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return filepath
    except Exception as e:
        print(f"保存檔案時發生錯誤：{e}")
        return None

def main():
    # base_url = "https://docs.llamaindex.ai/en/stable/understanding/"  # 只爬取 understanding 目錄
    base_url = "https://docs.llamaindex.ai/en/stable/module_guides/"
    output_dir = "./llamaindex_docs_module_guides"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        print("開始遞迴爬取文件連結...")
        links = get_llamaindex_links(base_url)
        total_links = len(links)
        print(f"\n找到 {total_links} 個文件連結")
        
        for i, url in enumerate(links, 1):
            print(f"\n處理第 {i}/{total_links} 個頁面: {url}")
            
            # 抓取頁面內容
            title, content = get_page_content(url, headers)
            if title and content:
                # 保存為 Markdown
                filepath = save_to_markdown(title, content, output_dir)
                if filepath:
                    print(f"已保存到: {filepath}")
                else:
                    print(f"保存失敗: {url}")
            else:
                print(f"抓取失敗: {url}")
            
            # 加入延遲，避免請求過於頻繁
            if i < total_links:
                time.sleep(2)
        
        print(f"\n完成！所有文件都已保存到 {output_dir}")
    
    except Exception as e:
        print(f"發生錯誤: {e}")

if __name__ == "__main__":
    main()