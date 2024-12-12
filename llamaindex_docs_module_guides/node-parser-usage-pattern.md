# Node Parser Usage Pattern#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/

# Node Parser Usage Pattern#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/#node-parser-usage-pattern)

Node parsers are a simple abstraction that take a list of documents, and chunk them into Node objects, such that each node is a specific chunk of the parent document. When a document is broken into nodes, all of it's attributes are inherited to the children nodes (i.e. metadata, text and metadata templates, etc.). You can read more about Node and Document properties [here](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/).

```
Node
```

```
metadata
```

```
Node
```

```
Document
```

## Getting Started#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/#getting-started)

### Standalone Usage#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/#standalone-usage)

Node parsers can be used on their own:

```
from llama_index.core import Document
from llama_index.core.node_parser import SentenceSplitter

node_parser = SentenceSplitter(chunk_size=1024, chunk_overlap=20)

nodes = node_parser.get_nodes_from_documents(
    [Document(text="long text")], show_progress=False
)
```

```
from llama_index.core import Document
from llama_index.core.node_parser import SentenceSplitter

node_parser = SentenceSplitter(chunk_size=1024, chunk_overlap=20)

nodes = node_parser.get_nodes_from_documents(
    [Document(text="long text")], show_progress=False
)
```

### Transformation Usage#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/#transformation-usage)

Node parsers can be included in any set of transformations with an ingestion pipeline.

```
from llama_index.core import SimpleDirectoryReader
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import TokenTextSplitter

documents = SimpleDirectoryReader("./data").load_data()

pipeline = IngestionPipeline(transformations=[TokenTextSplitter(), ...])

nodes = pipeline.run(documents=documents)
```

```
from llama_index.core import SimpleDirectoryReader
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import TokenTextSplitter

documents = SimpleDirectoryReader("./data").load_data()

pipeline = IngestionPipeline(transformations=[TokenTextSplitter(), ...])

nodes = pipeline.run(documents=documents)
```

### Index Usage#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/#index-usage)

Or set inside a transformations or global settings to be used automatically when an index is constructed using .from_documents():

```
transformations
```

```
.from_documents()
```

```
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter

documents = SimpleDirectoryReader("./data").load_data()

# global
from llama_index.core import Settings

Settings.text_splitter = SentenceSplitter(chunk_size=1024, chunk_overlap=20)

# per-index
index = VectorStoreIndex.from_documents(
    documents,
    transformations=[SentenceSplitter(chunk_size=1024, chunk_overlap=20)],
)
```

```
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter

documents = SimpleDirectoryReader("./data").load_data()

# global
from llama_index.core import Settings

Settings.text_splitter = SentenceSplitter(chunk_size=1024, chunk_overlap=20)

# per-index
index = VectorStoreIndex.from_documents(
    documents,
    transformations=[SentenceSplitter(chunk_size=1024, chunk_overlap=20)],
)
```

## Modules#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/#modules)

See the full [modules guide](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/).

