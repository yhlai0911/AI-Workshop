# Documents / Nodes#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/

# Documents / Nodes#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/#documents-nodes)

## Concept#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/#concept)

Document and Node objects are core abstractions within LlamaIndex.

A Document is a generic container around any data source - for instance, a PDF, an API output, or retrieved data from a database. They can be constructed manually, or created automatically via our data loaders. By default, a Document stores text along with some other attributes. Some of these are listed below.

- metadata - a dictionary of annotations that can be appended to the text.
```
metadata
```

- relationships - a dictionary containing relationships to other Documents/Nodes.
```
relationships
```

Note: We have beta support for allowing Documents to store images, and are actively working on improving its multimodal capabilities.

A Node represents a "chunk" of a source Document, whether that is a text chunk, an image, or other. Similar to Documents, they contain metadata and relationship information with other nodes.

Nodes are a first-class citizen in LlamaIndex. You can choose to define Nodes and all its attributes directly. You may also choose to "parse" source Documents into Nodes through our NodeParser classes. By default every Node derived from a Document will inherit the same metadata from that Document (e.g. a "file_name" filed in the Document is propagated to every Node).

```
NodeParser
```

## Usage Pattern#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/#usage-pattern)

Here are some simple snippets to get started with Documents and Nodes.

#### Documents#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/#documents)

```
from llama_index.core import Document, VectorStoreIndex

text_list = [text1, text2, ...]
documents = [Document(text=t) for t in text_list]

# build index
index = VectorStoreIndex.from_documents(documents)
```

```
from llama_index.core import Document, VectorStoreIndex

text_list = [text1, text2, ...]
documents = [Document(text=t) for t in text_list]

# build index
index = VectorStoreIndex.from_documents(documents)
```

#### Nodes#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/#nodes)

```
from llama_index.core.node_parser import SentenceSplitter

# load documents
...

# parse nodes
parser = SentenceSplitter()
nodes = parser.get_nodes_from_documents(documents)

# build index
index = VectorStoreIndex(nodes)
```

```
from llama_index.core.node_parser import SentenceSplitter

# load documents
...

# parse nodes
parser = SentenceSplitter()
nodes = parser.get_nodes_from_documents(documents)

# build index
index = VectorStoreIndex(nodes)
```

### Document/Node Usage#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/#documentnode-usage)

Take a look at our in-depth guides for more details on how to use Documents/Nodes.

- [Using Documents](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/)
- [Using Nodes](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_nodes/)
- [Ingestion Pipeline](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/)
