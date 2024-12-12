# Transformations#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/transformations/

# Transformations#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/transformations/#transformations)

A transformation is something that takes a list of nodes as an input, and returns a list of nodes. Each component that implements the Transformation base class has both a synchronous __call__() definition and an async acall() definition.

```
Transformation
```

```
__call__()
```

```
acall()
```

Currently, the following components are Transformation objects:

```
Transformation
```

- [TextSplitter](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/#text-splitters)
```
TextSplitter
```

- [NodeParser](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/)
```
NodeParser
```

- [MetadataExtractor](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_metadata_extractor/)
```
MetadataExtractor
```

- Embeddingsmodel (check our [list of supported embeddings](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/#list-of-supported-embeddings))
```
Embeddings
```

## Usage Pattern#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/transformations/#usage-pattern)

While transformations are best used with with an [IngestionPipeline](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/), they can also be used directly.

```
IngestionPipeline
```

```
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor

node_parser = SentenceSplitter(chunk_size=512)
extractor = TitleExtractor()

# use transforms directly
nodes = node_parser(documents)

# or use a transformation in async
nodes = await extractor.acall(nodes)
```

```
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor

node_parser = SentenceSplitter(chunk_size=512)
extractor = TitleExtractor()

# use transforms directly
nodes = node_parser(documents)

# or use a transformation in async
nodes = await extractor.acall(nodes)
```

## Combining with An Index#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/transformations/#combining-with-an-index)

Transformations can be passed into an index or overall global settings, and will be used when calling from_documents() or insert() on an index.

```
from_documents()
```

```
insert()
```

```
from llama_index.core import VectorStoreIndex
from llama_index.core.extractors import (
    TitleExtractor,
    QuestionsAnsweredExtractor,
)
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import TokenTextSplitter

transformations = [
    TokenTextSplitter(chunk_size=512, chunk_overlap=128),
    TitleExtractor(nodes=5),
    QuestionsAnsweredExtractor(questions=3),
]

# global
from llama_index.core import Settings

Settings.transformations = [text_splitter, title_extractor, qa_extractor]

# per-index
index = VectorStoreIndex.from_documents(
    documents, transformations=transformations
)
```

```
from llama_index.core import VectorStoreIndex
from llama_index.core.extractors import (
    TitleExtractor,
    QuestionsAnsweredExtractor,
)
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import TokenTextSplitter

transformations = [
    TokenTextSplitter(chunk_size=512, chunk_overlap=128),
    TitleExtractor(nodes=5),
    QuestionsAnsweredExtractor(questions=3),
]

# global
from llama_index.core import Settings

Settings.transformations = [text_splitter, title_extractor, qa_extractor]

# per-index
index = VectorStoreIndex.from_documents(
    documents, transformations=transformations
)
```

## Custom Transformations#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/transformations/#custom-transformations)

You can implement any transformation yourself by implementing the base class.

The following custom transformation will remove any special characters or punctutaion in text.

```
import re
from llama_index.core import Document
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.schema import TransformComponent


class TextCleaner(TransformComponent):
    def __call__(self, nodes, **kwargs):
        for node in nodes:
            node.text = re.sub(r"[^0-9A-Za-z ]", "", node.text)
        return nodes
```

```
import re
from llama_index.core import Document
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.schema import TransformComponent


class TextCleaner(TransformComponent):
    def __call__(self, nodes, **kwargs):
        for node in nodes:
            node.text = re.sub(r"[^0-9A-Za-z ]", "", node.text)
        return nodes
```

These can then be used directly or in any IngestionPipeline.

```
IngestionPipeline
```

```
# use in a pipeline
pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=25, chunk_overlap=0),
        TextCleaner(),
        OpenAIEmbedding(),
    ],
)

nodes = pipeline.run(documents=[Document.example()])
```

```
# use in a pipeline
pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=25, chunk_overlap=0),
        TextCleaner(),
        OpenAIEmbedding(),
    ],
)

nodes = pipeline.run(documents=[Document.example()])
```

