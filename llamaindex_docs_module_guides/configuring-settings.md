# Configuring Settings#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/supporting_modules/settings/

# Configuring Settings#

[#](https://docs.llamaindex.ai/en/stable/module_guides/supporting_modules/settings/#configuring-settings)

The Settings is a bundle of commonly used resources used during the indexing and querying stage in a LlamaIndex workflow/application.

```
Settings
```

You can use it to set the [global configuration](https://docs.llamaindex.ai/en/stable/module_guides/supporting_modules/settings/#setting-global-configuration). Local configurations (transformations, LLMs, embedding models) can be passed directly into the interfaces that make use of them.

The Settings is a simple singleton object that lives throughout your application. Whenever a particular component is not provided, the Settings object is used to provide it as a global default.

```
Settings
```

```
Settings
```

The following attributes can be configured on the Settings object:

```
Settings
```

## LLM#

[#](https://docs.llamaindex.ai/en/stable/module_guides/supporting_modules/settings/#llm)

The LLM is used to respond to prompts and queries, and is responsible for writing natural language responses.

```
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings

Settings.llm = OpenAI(model="gpt-3.5-turbo", temperature=0.1)
```

```
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings

Settings.llm = OpenAI(model="gpt-3.5-turbo", temperature=0.1)
```

## Embed Model#

[#](https://docs.llamaindex.ai/en/stable/module_guides/supporting_modules/settings/#embed-model)

The embedding model is used to convert text to numerical representations, used for calculating similarity and top-k retrieval.

```
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings

Settings.embed_model = OpenAIEmbedding(
    model="text-embedding-3-small", embed_batch_size=100
)
```

```
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings

Settings.embed_model = OpenAIEmbedding(
    model="text-embedding-3-small", embed_batch_size=100
)
```

## Node Parser / Text Splitter#

[#](https://docs.llamaindex.ai/en/stable/module_guides/supporting_modules/settings/#node-parser-text-splitter)

The node parser / text splitter is used to parse documents into smaller chunks, called nodes.

```
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Settings

Settings.text_splitter = SentenceSplitter(chunk_size=1024)
```

```
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Settings

Settings.text_splitter = SentenceSplitter(chunk_size=1024)
```

If you just want to change the chunk size or chunk overlap without changing the default splitter, this is also possible:

```
Settings.chunk_size = 512
Settings.chunk_overlap = 20
```

```
Settings.chunk_size = 512
Settings.chunk_overlap = 20
```

## Transformations#

[#](https://docs.llamaindex.ai/en/stable/module_guides/supporting_modules/settings/#transformations)

Transformations are applied to Documents during ingestion. By default, the node_parser/text_splitter is used, but this can be overridden and customized further.

```
Document
```

```
node_parser
```

```
text_splitter
```

```
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Settings

Settings.transformations = [SentenceSplitter(chunk_size=1024)]
```

```
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Settings

Settings.transformations = [SentenceSplitter(chunk_size=1024)]
```

## Tokenizer#

[#](https://docs.llamaindex.ai/en/stable/module_guides/supporting_modules/settings/#tokenizer)

The tokenizer is used to count tokens. This should be set to something that matches the LLM you are using.

```
from llama_index.core import Settings

# openai
import tiktoken

Settings.tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo").encode

# open-source
from transformers import AutoTokenizer

Settings.tokenzier = AutoTokenizer.from_pretrained(
    "mistralai/Mixtral-8x7B-Instruct-v0.1"
)
```

```
from llama_index.core import Settings

# openai
import tiktoken

Settings.tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo").encode

# open-source
from transformers import AutoTokenizer

Settings.tokenzier = AutoTokenizer.from_pretrained(
    "mistralai/Mixtral-8x7B-Instruct-v0.1"
)
```

## Callbacks#

[#](https://docs.llamaindex.ai/en/stable/module_guides/supporting_modules/settings/#callbacks)

You can set a global callback manager, which can be used to observe and consume events generated throughout the llama-index code

```
from llama_index.core.callbacks import TokenCountingHandler, CallbackManager
from llama_index.core import Settings

token_counter = TokenCountingHandler()
Settings.callback_manager = CallbackManager([token_counter])
```

```
from llama_index.core.callbacks import TokenCountingHandler, CallbackManager
from llama_index.core import Settings

token_counter = TokenCountingHandler()
Settings.callback_manager = CallbackManager([token_counter])
```

## Prompt Helper Arguments#

[#](https://docs.llamaindex.ai/en/stable/module_guides/supporting_modules/settings/#prompt-helper-arguments)

A few specific arguments/values are used during querying, to ensure that the input prompts to the LLM have enough room to generate a certain number of tokens.

Typically these are automatically configured using attributes from the LLM, but they can be overridden in special cases.

```
from llama_index.core import Settings

# maximum input size to the LLM
Settings.context_window = 4096

# number of tokens reserved for text generation.
Settings.num_output = 256
```

```
from llama_index.core import Settings

# maximum input size to the LLM
Settings.context_window = 4096

# number of tokens reserved for text generation.
Settings.num_output = 256
```

Tip

Learn how to configure specific modules: - [LLM](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/usage_custom/) - [Embedding Model](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/) - [Node Parser/Text Splitters](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/) - [Callbacks](https://docs.llamaindex.ai/en/stable/module_guides/observability/callbacks/)

## Setting local configurations#

[#](https://docs.llamaindex.ai/en/stable/module_guides/supporting_modules/settings/#setting-local-configurations)

Interfaces that use specific parts of the settings can also accept local overrides.

```
index = VectorStoreIndex.from_documents(
    documents, embed_model=embed_model, transformations=transformations
)

query_engine = index.as_query_engine(llm=llm)
```

```
index = VectorStoreIndex.from_documents(
    documents, embed_model=embed_model, transformations=transformations
)

query_engine = index.as_query_engine(llm=llm)
```

