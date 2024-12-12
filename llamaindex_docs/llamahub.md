# LlamaHub#

原始連結：https://docs.llamaindex.ai/en/stable/understanding/loading/llamahub/

# LlamaHub#

[#](https://docs.llamaindex.ai/en/stable/understanding/loading/llamahub/#llamahub)

Our data connectors are offered through [LlamaHub](https://llamahub.ai/) 🦙.
[LlamaHub](https://llamahub.ai/) contains a registry of open-source data connectors that you can easily plug into any LlamaIndex application (+ Agent Tools, and Llama Packs).

## Usage Pattern#

[#](https://docs.llamaindex.ai/en/stable/understanding/loading/llamahub/#usage-pattern)

Get started with:

```
from llama_index.core import download_loader

from llama_index.readers.google import GoogleDocsReader

loader = GoogleDocsReader()
documents = loader.load_data(document_ids=[...])
```

```
from llama_index.core import download_loader

from llama_index.readers.google import GoogleDocsReader

loader = GoogleDocsReader()
documents = loader.load_data(document_ids=[...])
```

## Built-in connector: SimpleDirectoryReader#

[#](https://docs.llamaindex.ai/en/stable/understanding/loading/llamahub/#built-in-connector-simpledirectoryreader)

SimpleDirectoryReader. Can support parsing a wide range of file types including .md, .pdf, .jpg, .png, .docx, as well as audio and video types. It is available directly as part of LlamaIndex:

```
SimpleDirectoryReader
```

```
.md
```

```
.pdf
```

```
.jpg
```

```
.png
```

```
.docx
```

```
from llama_index.core import SimpleDirectoryReader

documents = SimpleDirectoryReader("./data").load_data()
```

```
from llama_index.core import SimpleDirectoryReader

documents = SimpleDirectoryReader("./data").load_data()
```

## Available connectors#

[#](https://docs.llamaindex.ai/en/stable/understanding/loading/llamahub/#available-connectors)

Browse [LlamaHub](https://llamahub.ai/) directly to see the hundreds of connectors available, including:

- [Notion](https://developers.notion.com/) ([Notion](https://developers.notion.com/)PageReader)
```
NotionPageReader
```

- [Google Docs](https://developers.google.com/docs/api) (GoogleDocsReader)
```
GoogleDocsReader
```

- [Slack](https://api.slack.com/) ([Slack](https://api.slack.com/)Reader)
```
SlackReader
```

- [Discord](https://discord.com/developers/docs/intro) ([Discord](https://discord.com/developers/docs/intro)Reader)
```
DiscordReader
```

- [Apify Actors](https://llamahub.ai/l/apify-actor) (ApifyActor). Can crawl the web, scrape webpages, extract text content, download files including .pdf, .jpg, .png, .docx, etc.
```
ApifyActor
```

```
.pdf
```

```
.jpg
```

```
.png
```

```
.docx
```

