# Usage Pattern#

原始連結：https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/usage_pattern/

# Usage Pattern#

[#](https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/usage_pattern/#usage-pattern)

## Estimating LLM and Embedding Token Counts#

[#](https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/usage_pattern/#estimating-llm-and-embedding-token-counts)

In order to measure LLM and Embedding token counts, you'll need to

1. Setup MockLLM and MockEmbedding objects
```
MockLLM
```

```
MockEmbedding
```

```
from llama_index.core.llms import MockLLM
from llama_index.core import MockEmbedding

llm = MockLLM(max_tokens=256)
embed_model = MockEmbedding(embed_dim=1536)
```

```
from llama_index.core.llms import MockLLM
from llama_index.core import MockEmbedding

llm = MockLLM(max_tokens=256)
embed_model = MockEmbedding(embed_dim=1536)
```

1. Setup the TokenCountingCallback handler
```
TokenCountingCallback
```

```
import tiktoken
from llama_index.core.callbacks import CallbackManager, TokenCountingHandler

token_counter = TokenCountingHandler(
    tokenizer=tiktoken.encoding_for_model("gpt-3.5-turbo").encode
)

callback_manager = CallbackManager([token_counter])
```

```
import tiktoken
from llama_index.core.callbacks import CallbackManager, TokenCountingHandler

token_counter = TokenCountingHandler(
    tokenizer=tiktoken.encoding_for_model("gpt-3.5-turbo").encode
)

callback_manager = CallbackManager([token_counter])
```

1. Add them to the global Settings
```
Settings
```

```
from llama_index.core import Settings

Settings.llm = llm
Settings.embed_model = embed_model
Settings.callback_manager = callback_manager
```

```
from llama_index.core import Settings

Settings.llm = llm
Settings.embed_model = embed_model
Settings.callback_manager = callback_manager
```

1. Construct an Index
```
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader(
    "./docs/examples/data/paul_graham"
).load_data()

index = VectorStoreIndex.from_documents(documents)
```

```
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader(
    "./docs/examples/data/paul_graham"
).load_data()

index = VectorStoreIndex.from_documents(documents)
```

1. Measure the counts!
```
print(
    "Embedding Tokens: ",
    token_counter.total_embedding_token_count,
    "\n",
    "LLM Prompt Tokens: ",
    token_counter.prompt_llm_token_count,
    "\n",
    "LLM Completion Tokens: ",
    token_counter.completion_llm_token_count,
    "\n",
    "Total LLM Token Count: ",
    token_counter.total_llm_token_count,
    "\n",
)

# reset counts
token_counter.reset_counts()
```

```
print(
    "Embedding Tokens: ",
    token_counter.total_embedding_token_count,
    "\n",
    "LLM Prompt Tokens: ",
    token_counter.prompt_llm_token_count,
    "\n",
    "LLM Completion Tokens: ",
    token_counter.completion_llm_token_count,
    "\n",
    "Total LLM Token Count: ",
    token_counter.total_llm_token_count,
    "\n",
)

# reset counts
token_counter.reset_counts()
```

1. Run a query, measure again
```
query_engine = index.as_query_engine()

response = query_engine.query("query")

print(
    "Embedding Tokens: ",
    token_counter.total_embedding_token_count,
    "\n",
    "LLM Prompt Tokens: ",
    token_counter.prompt_llm_token_count,
    "\n",
    "LLM Completion Tokens: ",
    token_counter.completion_llm_token_count,
    "\n",
    "Total LLM Token Count: ",
    token_counter.total_llm_token_count,
    "\n",
)
```

```
query_engine = index.as_query_engine()

response = query_engine.query("query")

print(
    "Embedding Tokens: ",
    token_counter.total_embedding_token_count,
    "\n",
    "LLM Prompt Tokens: ",
    token_counter.prompt_llm_token_count,
    "\n",
    "LLM Completion Tokens: ",
    token_counter.completion_llm_token_count,
    "\n",
    "Total LLM Token Count: ",
    token_counter.total_llm_token_count,
    "\n",
)
```

