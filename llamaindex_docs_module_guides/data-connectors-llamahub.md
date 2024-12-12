# Data Connectors (LlamaHub)#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/

# Data Connectors (LlamaHub)#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/#data-connectors-llamahub)

## Concept#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/#concept)

A data connector (aka Reader) ingest data from different data sources and data formats into a simple Document representation (text and simple metadata).

```
Reader
```

```
Document
```

Tip

Once you've ingested your data, you can build an [Index](https://docs.llamaindex.ai/en/stable/module_guides/indexing/) on top, ask questions using a [Query Engine](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/), and have a conversation using a [Chat Engine](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/).

## LlamaHub#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/#llamahub)

Our data connectors are offered through [LlamaHub](https://llamahub.ai/) 🦙.
[LlamaHub](https://llamahub.ai/) is an open-source repository containing data loaders that you can easily plug and play into any LlamaIndex application.

## Usage Pattern#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/#usage-pattern)

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

See the full [usage pattern guide](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/usage_pattern/) for more details.

## Modules#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/#modules)

Some sample data connectors:

- local file directory (SimpleDirectoryReader). Can support parsing a wide range of file types: .pdf, .jpg, .png, .docx, etc.
```
SimpleDirectoryReader
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

- [Apify Actors](https://llamahub.ai/l/readers/llama-index-readers-apify) (ApifyActor). Can crawl the web, scrape webpages, extract text content, download files including .pdf, .jpg, .png, .docx, etc.
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

See the [modules guide](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/modules/) for more details.

