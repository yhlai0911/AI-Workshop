# Cost Analysis#

原始連結：https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/

# Cost Analysis#

[#](https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/#cost-analysis)

## Concept#

[#](https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/#concept)

Each call to an LLM will cost some amount of money - for instance, OpenAI's gpt-3.5-turbo costs $0.002 / 1k tokens. The cost of building an index and querying depends on

- the type of LLM used
- the type of data structure used
- parameters used during building
- parameters used during querying
The cost of building and querying each index is a TODO in the reference documentation. In the meantime, we provide the following information:

1. A high-level overview of the cost structure of the indices.
1. A token predictor that you can use directly within LlamaIndex!
### Overview of Cost Structure#

[#](https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/#overview-of-cost-structure)

#### Indices with no LLM calls#

[#](https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/#indices-with-no-llm-calls)

The following indices don't require LLM calls at all during building (0 cost):

- SummaryIndex
```
SummaryIndex
```

- SimpleKeywordTableIndex - uses a regex keyword extractor to extract keywords from each document
```
SimpleKeywordTableIndex
```

- RAKEKeywordTableIndex - uses a RAKE keyword extractor to extract keywords from each document
```
RAKEKeywordTableIndex
```

#### Indices with LLM calls#

[#](https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/#indices-with-llm-calls)

The following indices do require LLM calls during build time:

- TreeIndex - use LLM to hierarchically summarize the text to build the tree
```
TreeIndex
```

- KeywordTableIndex - use LLM to extract keywords from each document
```
KeywordTableIndex
```

### Query Time#

[#](https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/#query-time)

There will always be >= 1 LLM call during query time, in order to synthesize the final answer.
Some indices contain cost tradeoffs between index building and querying. SummaryIndex, for instance,
is free to build, but running a query over a summary index (without filtering or embedding lookups), will
call the LLM {math}N times.

```
SummaryIndex
```

```
N
```

Here are some notes regarding each of the indices:

- SummaryIndex: by default requires {math}N LLM calls, where N is the number of nodes.
```
SummaryIndex
```

```
N
```

- TreeIndex: by default requires {math}\log (N) LLM calls, where N is the number of leaf nodes.
```
TreeIndex
```

```
\log (N)
```

- Setting child_branch_factor=2 will be more expensive than the default child_branch_factor=1 (polynomial vs logarithmic), because we traverse 2 children instead of just 1 for each parent node.
```
child_branch_factor=2
```

```
child_branch_factor=1
```

- KeywordTableIndex: by default requires an LLM call to extract query keywords.
```
KeywordTableIndex
```

- Can do index.as_retriever(retriever_mode="simple") or index.as_retriever(retriever_mode="rake") to also use regex/RAKE keyword extractors on your query text.
```
index.as_retriever(retriever_mode="simple")
```

```
index.as_retriever(retriever_mode="rake")
```

- VectorStoreIndex: by default, requires one LLM call per query. If you increase the similarity_top_k or chunk_size, or change the response_mode, then this number will increase.
```
VectorStoreIndex
```

```
similarity_top_k
```

```
chunk_size
```

```
response_mode
```

## Usage Pattern#

[#](https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/#usage-pattern)

LlamaIndex offers token predictors to predict token usage of LLM and embedding calls.
This allows you to estimate your costs during 1) index construction, and 2) index querying, before
any respective LLM calls are made.

Tokens are counted using the TokenCountingHandler callback. See the [example notebook](https://docs.llamaindex.ai/en/stable/examples/callbacks/TokenCountingHandler.ipynb) for details on the setup.

```
TokenCountingHandler
```

### Using MockLLM#

[#](https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/#using-mockllm)

To predict token usage of LLM calls, import and instantiate the MockLLM as shown below. The max_tokens parameter is used as a "worst case" prediction, where each LLM response will contain exactly that number of tokens. If max_tokens is not specified, then it will simply predict back the prompt.

```
max_tokens
```

```
max_tokens
```

```
from llama_index.core.llms import MockLLM
from llama_index.core import Settings

# use a mock llm globally
Settings.llm = MockLLM(max_tokens=256)
```

```
from llama_index.core.llms import MockLLM
from llama_index.core import Settings

# use a mock llm globally
Settings.llm = MockLLM(max_tokens=256)
```

You can then use this predictor during both index construction and querying.

### Using MockEmbedding#

[#](https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/#using-mockembedding)

You may also predict the token usage of embedding calls with MockEmbedding.

```
MockEmbedding
```

```
from llama_index.core import MockEmbedding
from llama_index.core import Settings

# use a mock embedding globally
Settings.embed_model = MockEmbedding(embed_dim=1536)
```

```
from llama_index.core import MockEmbedding
from llama_index.core import Settings

# use a mock embedding globally
Settings.embed_model = MockEmbedding(embed_dim=1536)
```

## Usage Pattern#

[#](https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/#usage-pattern_1)

Read about the [full usage pattern](https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/usage_pattern/) for more details!

