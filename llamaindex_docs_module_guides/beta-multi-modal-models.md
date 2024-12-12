# [Beta] Multi-modal models#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/models/multi_modal/

# [Beta] Multi-modal models#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/multi_modal/#beta-multi-modal-models)

## Concept#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/multi_modal/#concept)

Large language models (LLMs) are text-in, text-out. Large Multi-modal Models (LMMs) generalize this beyond the text modalities. For instance, models such as GPT-4V allow you to jointly input both images and text, and output text.

We've included a base MultiModalLLM abstraction to allow for text+image models. NOTE: This naming is subject to change!

```
MultiModalLLM
```

## Usage Pattern#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/multi_modal/#usage-pattern)

1. The following code snippet shows how you can get started using LMMs e.g. with GPT-4V.
```
from llama_index.multi_modal_llms.openai import OpenAIMultiModal
from llama_index.core.multi_modal_llms.generic_utils import load_image_urls
from llama_index.core import SimpleDirectoryReader

# load image documents from urls
image_documents = load_image_urls(image_urls)

# load image documents from local directory
image_documents = SimpleDirectoryReader(local_directory).load_data()

# non-streaming
openai_mm_llm = OpenAIMultiModal(
    model="gpt-4-vision-preview", api_key=OPENAI_API_KEY, max_new_tokens=300
)
response = openai_mm_llm.complete(
    prompt="what is in the image?", image_documents=image_documents
)
```

```
from llama_index.multi_modal_llms.openai import OpenAIMultiModal
from llama_index.core.multi_modal_llms.generic_utils import load_image_urls
from llama_index.core import SimpleDirectoryReader

# load image documents from urls
image_documents = load_image_urls(image_urls)

# load image documents from local directory
image_documents = SimpleDirectoryReader(local_directory).load_data()

# non-streaming
openai_mm_llm = OpenAIMultiModal(
    model="gpt-4-vision-preview", api_key=OPENAI_API_KEY, max_new_tokens=300
)
response = openai_mm_llm.complete(
    prompt="what is in the image?", image_documents=image_documents
)
```

1. The following code snippet shows how you can build MultiModal Vector Stores/Index.
```
from llama_index.core.indices import MultiModalVectorStoreIndex
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import SimpleDirectoryReader, StorageContext

import qdrant_client
from llama_index.core import SimpleDirectoryReader

# Create a local Qdrant vector store
client = qdrant_client.QdrantClient(path="qdrant_mm_db")

# if you only need image_store for image retrieval,
# you can remove text_sotre
text_store = QdrantVectorStore(
    client=client, collection_name="text_collection"
)
image_store = QdrantVectorStore(
    client=client, collection_name="image_collection"
)

storage_context = StorageContext.from_defaults(
    vector_store=text_store, image_store=image_store
)

# Load text and image documents from local folder
documents = SimpleDirectoryReader("./data_folder/").load_data()
# Create the MultiModal index
index = MultiModalVectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context,
)
```

```
from llama_index.core.indices import MultiModalVectorStoreIndex
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import SimpleDirectoryReader, StorageContext

import qdrant_client
from llama_index.core import SimpleDirectoryReader

# Create a local Qdrant vector store
client = qdrant_client.QdrantClient(path="qdrant_mm_db")

# if you only need image_store for image retrieval,
# you can remove text_sotre
text_store = QdrantVectorStore(
    client=client, collection_name="text_collection"
)
image_store = QdrantVectorStore(
    client=client, collection_name="image_collection"
)

storage_context = StorageContext.from_defaults(
    vector_store=text_store, image_store=image_store
)

# Load text and image documents from local folder
documents = SimpleDirectoryReader("./data_folder/").load_data()
# Create the MultiModal index
index = MultiModalVectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context,
)
```

1. The following code snippet shows how you can use MultiModal Retriever and Query Engine.
```
from llama_index.multi_modal_llms.openai import OpenAIMultiModal
from llama_index.core import PromptTemplate
from llama_index.core.query_engine import SimpleMultiModalQueryEngine

retriever_engine = index.as_retriever(
    similarity_top_k=3, image_similarity_top_k=3
)

# retrieve more information from the GPT4V response
retrieval_results = retriever_engine.retrieve(response)

# if you only need image retrieval without text retrieval
# you can use `text_to_image_retrieve`
# retrieval_results = retriever_engine.text_to_image_retrieve(response)

qa_tmpl_str = (
    "Context information is below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Given the context information and not prior knowledge, "
    "answer the query.\n"
    "Query: {query_str}\n"
    "Answer: "
)
qa_tmpl = PromptTemplate(qa_tmpl_str)

query_engine = index.as_query_engine(
    multi_modal_llm=openai_mm_llm, text_qa_template=qa_tmpl
)

query_str = "Tell me more about the Porsche"
response = query_engine.query(query_str)
```

```
from llama_index.multi_modal_llms.openai import OpenAIMultiModal
from llama_index.core import PromptTemplate
from llama_index.core.query_engine import SimpleMultiModalQueryEngine

retriever_engine = index.as_retriever(
    similarity_top_k=3, image_similarity_top_k=3
)

# retrieve more information from the GPT4V response
retrieval_results = retriever_engine.retrieve(response)

# if you only need image retrieval without text retrieval
# you can use `text_to_image_retrieve`
# retrieval_results = retriever_engine.text_to_image_retrieve(response)

qa_tmpl_str = (
    "Context information is below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Given the context information and not prior knowledge, "
    "answer the query.\n"
    "Query: {query_str}\n"
    "Answer: "
)
qa_tmpl = PromptTemplate(qa_tmpl_str)

query_engine = index.as_query_engine(
    multi_modal_llm=openai_mm_llm, text_qa_template=qa_tmpl
)

query_str = "Tell me more about the Porsche"
response = query_engine.query(query_str)
```

Legend

- ✅ = should work fine
- ⚠️ = sometimes unreliable, may need more tuning to improve
- 🛑 = not available at the moment.
### End to End Multi-Modal Work Flow#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/multi_modal/#end-to-end-multi-modal-work-flow)

The tables below attempt to show the initial steps with various LlamaIndex features for building your own Multi-Modal RAGs (Retrieval Augmented Generation). You can combine different modules/steps together for composing your own Multi-Modal RAG orchestration.

### Multi-Modal LLM Models#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/multi_modal/#multi-modal-llm-models)

These notebooks serve as examples how to leverage and integrate Multi-Modal LLM model, Multi-Modal embeddings, Multi-Modal vector stores, Retriever, Query engine for composing Multi-Modal Retrieval Augmented Generation (RAG) orchestration.

[GPT4V](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4v_multi_modal_retrieval/)

[GPT4V-Azure](https://docs.llamaindex.ai/en/stable/examples/multi_modal/azure_openai_multi_modal/)

[Gemini](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/)

[CLIP](https://docs.llamaindex.ai/en/stable/examples/multi_modal/image_to_image_retrieval/)

[LLaVa](https://docs.llamaindex.ai/en/stable/examples/multi_modal/llava_multi_modal_tesla_10q/)

[Fuyu-8B](https://docs.llamaindex.ai/en/stable/examples/multi_modal/replicate_multi_modal/)

[ImageBind](https://imagebind.metademolab.com/)

[MiniGPT-4](https://docs.llamaindex.ai/en/stable/examples/multi_modal/replicate_multi_modal/)

[CogVLM](https://github.com/THUDM/CogVLM)

[Qwen-VL](https://arxiv.org/abs/2308.12966)

### Multi Modal Vector Stores#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/multi_modal/#multi-modal-vector-stores)

Below table lists some vector stores supporting Multi-Modal use cases. Our LlamaIndex built-in MultiModalVectorStoreIndex supports building separate vector stores for image and text embedding vector stores. MultiModalRetriever, and SimpleMultiModalQueryEngine support text to text/image and image to image retrieval and simple ranking fusion functions for combining text and image retrieval results.
| Multi-ModalVector Stores | SingleVectorStore | MultipleVectorStores | TextEmbedding | ImageEmbedding |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | --------------------------- | --------------------------------------------------------- | ------------------------------------------------------- |
| [LLamaIndex self-builtMultiModal Index](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4v_multi_modal_retrieval/) | 🛑 | ✅ | Can be arbitrarytext embedding(Default is GPT3.5) | Can be arbitraryImage embedding(Default is CLIP) |
| [Chroma](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ChromaMultiModalDemo/) | ✅ | 🛑 | CLIP ✅ | CLIP ✅ |
| [Weaviate](https://weaviate.io/developers/weaviate/modules/retriever-vectorizer-modules/multi2vec-bind)[To integrate] | ✅ | 🛑 | CLIP ✅ImageBind ✅ | CLIP ✅ImageBind ✅ |

```
MultiModalVectorStoreIndex
```

```
MultiModalRetriever
```

```
SimpleMultiModalQueryEngine
```

## Multi-Modal LLM Modules#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/multi_modal/#multi-modal-llm-modules)

We support integrations with GPT4-V, Anthropic (Opus, Sonnet), Gemini (Google), CLIP (OpenAI), BLIP (Salesforce), and Replicate (LLaVA, Fuyu-8B, MiniGPT-4, CogVLM), and more.

- [OpenAI](https://docs.llamaindex.ai/en/stable/examples/multi_modal/openai_multi_modal/)
- [Gemini](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/)
- [Anthropic](https://docs.llamaindex.ai/en/stable/examples/multi_modal/anthropic_multi_modal/)
- [Replicate](https://docs.llamaindex.ai/en/stable/examples/multi_modal/replicate_multi_modal/)
- [Pydantic Multi-Modal](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/)
- [GPT-4v COT Experiments](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4v_experiments_cot/)
- [Llava Tesla 10q](https://docs.llamaindex.ai/en/stable/examples/multi_modal/llava_multi_modal_tesla_10q/)
## Multi-Modal Retrieval Augmented Generation#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/multi_modal/#multi-modal-retrieval-augmented-generation)

We support Multi-Modal Retrieval Augmented Generation with different Multi-Modal LLMs with Multi-Modal vector stores.

- [GPT-4v Retrieval](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4v_multi_modal_retrieval/)
- [Multi-Modal Retrieval](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_retrieval/)
- [Image-to-Image Retrieval](https://docs.llamaindex.ai/en/stable/examples/multi_modal/image_to_image_retrieval/)
- [Chroma Multi-Modal](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ChromaMultiModalDemo/)
## Evaluation#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/multi_modal/#evaluation)

We support basic evaluation for Multi-Modal LLM and Retrieval Augmented Generation.

- [Multi-Modal RAG Eval](https://docs.llamaindex.ai/en/stable/examples/evaluation/multi_modal/multi_modal_rag_evaluation/)
