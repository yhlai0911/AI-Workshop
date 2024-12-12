# Metadata Extraction Usage Pattern#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_metadata_extractor/

# Metadata Extraction Usage Pattern#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_metadata_extractor/#metadata-extraction-usage-pattern)

You can use LLMs to automate metadata extraction with our Metadata Extractor modules.

```
Metadata Extractor
```

Our metadata extractor modules include the following "feature extractors":

- SummaryExtractor - automatically extracts a summary over a set of Nodes
```
SummaryExtractor
```

- QuestionsAnsweredExtractor - extracts a set of questions that each Node can answer
```
QuestionsAnsweredExtractor
```

- TitleExtractor - extracts a title over the context of each Node
```
TitleExtractor
```

- EntityExtractor - extracts entities (i.e. names of places, people, things) mentioned in the content of each Node
```
EntityExtractor
```

Then you can chain the Metadata Extractors with our node parser:

```
Metadata Extractor
```

```
from llama_index.core.extractors import (
    TitleExtractor,
    QuestionsAnsweredExtractor,
)
from llama_index.core.node_parser import TokenTextSplitter

text_splitter = TokenTextSplitter(
    separator=" ", chunk_size=512, chunk_overlap=128
)
title_extractor = TitleExtractor(nodes=5)
qa_extractor = QuestionsAnsweredExtractor(questions=3)

# assume documents are defined -> extract nodes
from llama_index.core.ingestion import IngestionPipeline

pipeline = IngestionPipeline(
    transformations=[text_splitter, title_extractor, qa_extractor]
)

nodes = pipeline.run(
    documents=documents,
    in_place=True,
    show_progress=True,
)
```

```
from llama_index.core.extractors import (
    TitleExtractor,
    QuestionsAnsweredExtractor,
)
from llama_index.core.node_parser import TokenTextSplitter

text_splitter = TokenTextSplitter(
    separator=" ", chunk_size=512, chunk_overlap=128
)
title_extractor = TitleExtractor(nodes=5)
qa_extractor = QuestionsAnsweredExtractor(questions=3)

# assume documents are defined -> extract nodes
from llama_index.core.ingestion import IngestionPipeline

pipeline = IngestionPipeline(
    transformations=[text_splitter, title_extractor, qa_extractor]
)

nodes = pipeline.run(
    documents=documents,
    in_place=True,
    show_progress=True,
)
```

or insert into an index:

```
from llama_index.core import VectorStoreIndex

index = VectorStoreIndex.from_documents(
    documents, transformations=[text_splitter, title_extractor, qa_extractor]
)
```

```
from llama_index.core import VectorStoreIndex

index = VectorStoreIndex.from_documents(
    documents, transformations=[text_splitter, title_extractor, qa_extractor]
)
```

## Resources#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_metadata_extractor/#resources)

- [SEC Documents Metadata Extraction](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtractionSEC/)
- [LLM Survey Extraction](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtraction_LLMSurvey/)
- [Entity Extraction](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/EntityExtractionClimate/)
- [Marvin Metadata Extraction](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MarvinMetadataExtractorDemo/)
- [Pydantic Metadata Extraction](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/PydanticExtractor/)
