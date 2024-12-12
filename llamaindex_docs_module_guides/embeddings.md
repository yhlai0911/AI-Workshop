# Embeddings#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/

# Embeddings#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/#embeddings)

## Concept#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/#concept)

Embeddings are used in LlamaIndex to represent your documents using a sophisticated numerical representation. Embedding models take text as input, and return a long list of numbers used to capture the semantics of the text. These embedding models have been trained to represent text this way, and help enable many applications, including search!

At a high level, if a user asks a question about dogs, then the embedding for that question will be highly similar to text that talks about dogs.

When calculating the similarity between embeddings, there are many methods to use (dot product, cosine similarity, etc.). By default, LlamaIndex uses cosine similarity when comparing embeddings.

T[here](https://python.langchain.com/docs/modules/data_connection/text_embedding/) are many embedding models to pick from. By default, LlamaIndex uses text-embedding-ada-002 from OpenAI. We also support any embedding model offered by Langchain [here](https://python.langchain.com/docs/modules/data_connection/text_embedding/), as well as providing an easy to extend base class for implementing your own embeddings.

```
text-embedding-ada-002
```

## Usage Pattern#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/#usage-pattern)

Most commonly in LlamaIndex, embedding models will be specified in the Settings object, and then used in a vector index. The embedding model will be used to embed the documents used during index construction, as well as embedding any queries you make using the query engine later on. You can also specify embedding models per-index.

```
Settings
```

If you don't already have your embeddings installed:

```
pip install llama-index-embeddings-openai
```

```
pip install llama-index-embeddings-openai
```

Then:

```
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import VectorStoreIndex
from llama_index.core import Settings

# global
Settings.embed_model = OpenAIEmbedding()

# per-index
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
```

```
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import VectorStoreIndex
from llama_index.core import Settings

# global
Settings.embed_model = OpenAIEmbedding()

# per-index
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
```

To save costs, you may want to use a local model.

```
pip install llama-index-embeddings-huggingface
```

```
pip install llama-index-embeddings-huggingface
```

```
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)
```

```
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)
```

This will use a well-performing and fast default from Hugging Face.

You can find more usage details and available customization options below.

## Getting Started#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/#getting-started)

The most common usage for an embedding model will be setting it in the global Settings object, and then using it to construct an index and query. The input documents will be broken into nodes, and the embedding model will generate an embedding for each node.

```
Settings
```

By default, LlamaIndex will use text-embedding-ada-002, which is what the example below manually sets up for you.

```
text-embedding-ada-002
```

```
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings

# global default
Settings.embed_model = OpenAIEmbedding()

documents = SimpleDirectoryReader("./data").load_data()

index = VectorStoreIndex.from_documents(documents)
```

```
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings

# global default
Settings.embed_model = OpenAIEmbedding()

documents = SimpleDirectoryReader("./data").load_data()

index = VectorStoreIndex.from_documents(documents)
```

Then, at query time, the embedding model will be used again to embed the query text.

```
query_engine = index.as_query_engine()

response = query_engine.query("query string")
```

```
query_engine = index.as_query_engine()

response = query_engine.query("query string")
```

## Customization#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/#customization)

### Batch Size#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/#batch-size)

By default, embeddings requests are sent to OpenAI in batches of 10. For some users, this may (rarely) incur a rate limit. For other users embedding many documents, this batch size may be too small.

```
# set the batch size to 42
embed_model = OpenAIEmbedding(embed_batch_size=42)
```

```
# set the batch size to 42
embed_model = OpenAIEmbedding(embed_batch_size=42)
```

### Local Embedding Models#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/#local-embedding-models)

The easiest way to use a local model is:

```
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)
```

```
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)
```

### HuggingFace Optimum ONNX Embeddings#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/#huggingface-optimum-onnx-embeddings)

LlamaIndex also supports creating and using ONNX embeddings using the Optimum library from HuggingFace. Simple create and save the ONNX embeddings, and use them.

Some prerequisites:

```
pip install transformers optimum[exporters]
pip install llama-index-embeddings-huggingface-optimum
```

```
pip install transformers optimum[exporters]
pip install llama-index-embeddings-huggingface-optimum
```

Creation with specifying the model and output path:

```
from llama_index.embeddings.huggingface_optimum import OptimumEmbedding

OptimumEmbedding.create_and_save_optimum_model(
    "BAAI/bge-small-en-v1.5", "./bge_onnx"
)
```

```
from llama_index.embeddings.huggingface_optimum import OptimumEmbedding

OptimumEmbedding.create_and_save_optimum_model(
    "BAAI/bge-small-en-v1.5", "./bge_onnx"
)
```

And then usage:

```
Settings.embed_model = OptimumEmbedding(folder_name="./bge_onnx")
```

```
Settings.embed_model = OptimumEmbedding(folder_name="./bge_onnx")
```

### LangChain Integrations#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/#langchain-integrations)

We also support any embeddings offered by Langchain [here](https://python.langchain.com/docs/modules/data_connection/text_embedding/).

The example below loads a model from Hugging Face, using Langchain's embedding class.

```
pip install llama-index-embeddings-langchain
```

```
pip install llama-index-embeddings-langchain
```

```
from langchain.embeddings.huggingface import HuggingFaceBgeEmbeddings
from llama_index.core import Settings

Settings.embed_model = HuggingFaceBgeEmbeddings(model_name="BAAI/bge-base-en")
```

```
from langchain.embeddings.huggingface import HuggingFaceBgeEmbeddings
from llama_index.core import Settings

Settings.embed_model = HuggingFaceBgeEmbeddings(model_name="BAAI/bge-base-en")
```

### Custom Embedding Model#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/#custom-embedding-model)

If you wanted to use embeddings not offered by LlamaIndex or Langchain, you can also extend our base embeddings class and implement your own!

The example below uses Instructor Embeddings ([install/setup details here](https://huggingface.co/hkunlp/instructor-large)), and implements a custom embeddings class. Instructor embeddings work by providing text, as well as "instructions" on the domain of the text to embed. This is helpful when embedding text from a very specific and specialized topic.

```
from typing import Any, List
from InstructorEmbedding import INSTRUCTOR
from llama_index.core.embeddings import BaseEmbedding


class InstructorEmbeddings(BaseEmbedding):
    def __init__(
        self,
        instructor_model_name: str = "hkunlp/instructor-large",
        instruction: str = "Represent the Computer Science documentation or question:",
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self._model = INSTRUCTOR(instructor_model_name)
        self._instruction = instruction

        def _get_query_embedding(self, query: str) -> List[float]:
            embeddings = self._model.encode([[self._instruction, query]])
            return embeddings[0]

        def _get_text_embedding(self, text: str) -> List[float]:
            embeddings = self._model.encode([[self._instruction, text]])
            return embeddings[0]

        def _get_text_embeddings(self, texts: List[str]) -> List[List[float]]:
            embeddings = self._model.encode(
                [[self._instruction, text] for text in texts]
            )
            return embeddings

        async def _get_query_embedding(self, query: str) -> List[float]:
            return self._get_query_embedding(query)

        async def _get_text_embedding(self, text: str) -> List[float]:
            return self._get_text_embedding(text)
```

```
from typing import Any, List
from InstructorEmbedding import INSTRUCTOR
from llama_index.core.embeddings import BaseEmbedding


class InstructorEmbeddings(BaseEmbedding):
    def __init__(
        self,
        instructor_model_name: str = "hkunlp/instructor-large",
        instruction: str = "Represent the Computer Science documentation or question:",
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self._model = INSTRUCTOR(instructor_model_name)
        self._instruction = instruction

        def _get_query_embedding(self, query: str) -> List[float]:
            embeddings = self._model.encode([[self._instruction, query]])
            return embeddings[0]

        def _get_text_embedding(self, text: str) -> List[float]:
            embeddings = self._model.encode([[self._instruction, text]])
            return embeddings[0]

        def _get_text_embeddings(self, texts: List[str]) -> List[List[float]]:
            embeddings = self._model.encode(
                [[self._instruction, text] for text in texts]
            )
            return embeddings

        async def _get_query_embedding(self, query: str) -> List[float]:
            return self._get_query_embedding(query)

        async def _get_text_embedding(self, text: str) -> List[float]:
            return self._get_text_embedding(text)
```

## Standalone Usage#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/#standalone-usage)

You can also use embeddings as a standalone module for your project, existing application, or general testing and exploration.

```
embeddings = embed_model.get_text_embedding(
    "It is raining cats and dogs here!"
)
```

```
embeddings = embed_model.get_text_embedding(
    "It is raining cats and dogs here!"
)
```

## List of supported embeddings#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/#list-of-supported-embeddings)

We support integrations with OpenAI, Azure, and anything LangChain offers.

- [Azure OpenAI](https://docs.llamaindex.ai/en/stable/examples/customization/llms/AzureOpenAI/)
- [CalrifAI](https://docs.llamaindex.ai/en/stable/examples/embeddings/clarifai/)
- [Cohere](https://docs.llamaindex.ai/en/stable/examples/embeddings/cohereai/)
- [Custom](https://docs.llamaindex.ai/en/stable/examples/embeddings/custom_embeddings/)
- [Dashscope](https://docs.llamaindex.ai/en/stable/examples/embeddings/dashscope_embeddings/)
- [ElasticSearch](https://docs.llamaindex.ai/en/stable/examples/embeddings/elasticsearch/)
- [FastEmbed](https://docs.llamaindex.ai/en/stable/examples/embeddings/fastembed/)
- [Google Palm](https://docs.llamaindex.ai/en/stable/examples/embeddings/google_palm/)
- [Gradient](https://docs.llamaindex.ai/en/stable/module_guides/examples/embeddings/gradient.ipynb)
- [Anyscale](https://docs.llamaindex.ai/en/stable/examples/embeddings/Anyscale/)
- [Huggingface](https://docs.llamaindex.ai/en/stable/examples/embeddings/huggingface/)
- [JinaAI](https://docs.llamaindex.ai/en/stable/examples/embeddings/jinaai_embeddings/)
- [Langchain](https://docs.llamaindex.ai/en/stable/examples/embeddings/Langchain/)
- [LLM Rails](https://docs.llamaindex.ai/en/stable/examples/embeddings/llm_rails/)
- [MistralAI](https://docs.llamaindex.ai/en/stable/examples/embeddings/mistralai/)
- [OpenAI](https://docs.llamaindex.ai/en/stable/examples/embeddings/OpenAI/)
- [Sagemaker](https://docs.llamaindex.ai/en/stable/examples/embeddings/sagemaker_embedding_endpoint/)
- [Text Embedding Inference](https://docs.llamaindex.ai/en/stable/examples/embeddings/text_embedding_inference/)
- [TogetherAI](https://docs.llamaindex.ai/en/stable/examples/embeddings/together/)
- [Upstage](https://docs.llamaindex.ai/en/stable/examples/embeddings/upstage/)
- [VoyageAI](https://docs.llamaindex.ai/en/stable/examples/embeddings/voyageai/)
- [Nomic](https://docs.llamaindex.ai/en/stable/examples/embeddings/nomic/)
- [Fireworks AI](https://docs.llamaindex.ai/en/stable/examples/embeddings/fireworks/)
