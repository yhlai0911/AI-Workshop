# Loading Data#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/loading/

# Loading Data#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/#loading-data)

The key to data ingestion in LlamaIndex is loading and transformations. Once you have loaded Documents, you can process them via transformations and output Nodes.

Once you have [learned about the basics of loading data](https://docs.llamaindex.ai/en/stable/understanding/loading/loading/) in our Understanding section, you can read on to learn more about:

### Loading#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/#loading)

- [SimpleDirectoryReader](https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader/), our built-in loader for loading all sorts of file types from a local directory
- [LlamaParse](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/llama_parse/), LlamaIndex's official tool for PDF parsing, available as a managed API.
- [LlamaHub](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/), our registry of hundreds of data loading libraries to ingest data from any source
### Transformations#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/#transformations)

This includes common operations like splitting text.

- [Node Parser Usage Pattern](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/), showing you how to use our node parsers
- [Node Parser Modules](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/), showing our text splitters (sentence, token, HTML, JSON) and other parser modules.
### Putting it all Together#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/#putting-it-all-together)

- [The ingestion pipeline](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/) which allows you to set up a repeatable, cache-optimized process for loading data.
### Abstractions#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/#abstractions)

- [Document and Node objects](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/) and how to customize them for more advanced use cases
