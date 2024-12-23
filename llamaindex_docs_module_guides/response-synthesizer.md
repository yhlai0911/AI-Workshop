# Response Synthesizer#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/

# Response Synthesizer#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/#response-synthesizer)

## Concept#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/#concept)

A Response Synthesizer is what generates a response from an LLM, using a user query and a given set of text chunks. The output of a response synthesizer is a Response object.

```
Response Synthesizer
```

```
Response
```

The method for doing this can take many forms, from as simple as iterating over text chunks, to as complex as building a tree. The main idea here is to simplify the process of generating a response using an LLM across your data.

When used in a query engine, the response synthesizer is used after nodes are retrieved from a retriever, and after any node-postprocessors are ran.

Tip

Confused about where response synthesizer fits in the RAG workflow? Read the [high-level concepts](https://docs.llamaindex.ai/en/stable/getting_started/concepts/)

## Usage Pattern#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/#usage-pattern)

Use a response synthesizer on it's own:

```
from llama_index.core.data_structs import Node
from llama_index.core.response_synthesizers import ResponseMode
from llama_index.core import get_response_synthesizer

response_synthesizer = get_response_synthesizer(
    response_mode=ResponseMode.COMPACT
)

response = response_synthesizer.synthesize(
    "query text", nodes=[Node(text="text"), ...]
)
```

```
from llama_index.core.data_structs import Node
from llama_index.core.response_synthesizers import ResponseMode
from llama_index.core import get_response_synthesizer

response_synthesizer = get_response_synthesizer(
    response_mode=ResponseMode.COMPACT
)

response = response_synthesizer.synthesize(
    "query text", nodes=[Node(text="text"), ...]
)
```

Or in a query engine after you've created an index:

```
query_engine = index.as_query_engine(response_synthesizer=response_synthesizer)
response = query_engine.query("query_text")
```

```
query_engine = index.as_query_engine(response_synthesizer=response_synthesizer)
response = query_engine.query("query_text")
```

You can find more details on all available response synthesizers, modes, and how to build your own below.

## Usage Pattern#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/#usage-pattern_1)

## Get Started#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/#get-started)

Configuring the response synthesizer for a query engine using response_mode:

```
response_mode
```

```
from llama_index.core.data_structs import Node
from llama_index.core.schema import NodeWithScore
from llama_index.core import get_response_synthesizer

response_synthesizer = get_response_synthesizer(response_mode="compact")

response = response_synthesizer.synthesize(
    "query text", nodes=[NodeWithScore(node=Node(text="text"), score=1.0), ...]
)
```

```
from llama_index.core.data_structs import Node
from llama_index.core.schema import NodeWithScore
from llama_index.core import get_response_synthesizer

response_synthesizer = get_response_synthesizer(response_mode="compact")

response = response_synthesizer.synthesize(
    "query text", nodes=[NodeWithScore(node=Node(text="text"), score=1.0), ...]
)
```

Or, more commonly, in a query engine after you've created an index:

```
query_engine = index.as_query_engine(response_synthesizer=response_synthesizer)
response = query_engine.query("query_text")
```

```
query_engine = index.as_query_engine(response_synthesizer=response_synthesizer)
response = query_engine.query("query_text")
```

Tip

To learn how to build an index, see [Indexing](https://docs.llamaindex.ai/en/stable/module_guides/indexing/)

## Configuring the Response Mode#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/#configuring-the-response-mode)

Response synthesizers are typically specified through a response_mode kwarg setting.

```
response_mode
```

Several response synthesizers are implemented already in LlamaIndex:

- refine: create and refine an answer by sequentially going through each retrieved text chunk.
  This makes a separate LLM call per Node/retrieved chunk.
```
refine
```

Details: the first chunk is used in a query using the
  text_qa_template prompt. Then the answer and the next chunk (as well as the original question) are used
  in another query with the refine_template prompt. And so on until all chunks have been parsed.

```
text_qa_template
```

```
refine_template
```

If a chunk is too large to fit within the window (considering the prompt size), it is split using a TokenTextSplitter
  (allowing some text overlap between chunks) and the (new) additional chunks are considered as chunks
  of the original chunks collection (and thus queried with the refine_template as well).

```
TokenTextSplitter
```

```
refine_template
```

Good for more detailed answers.

- compact (default): similar to refine but compact (concatenate) the chunks beforehand, resulting in less LLM calls.
```
compact
```

```
refine
```

Details: stuff as many text (concatenated/packed from the retrieved chunks) that can fit within the context window
  (considering the maximum prompt size between text_qa_template and refine_template).
  If the text is too long to fit in one prompt, it is split in as many parts as needed
  (using a TokenTextSplitter and thus allowing some overlap between text chunks).

```
text_qa_template
```

```
refine_template
```

```
TokenTextSplitter
```

Each text part is considered a "chunk" and is sent to the refine synthesizer.

```
refine
```

In short, it is like refine, but with less LLM calls.

```
refine
```

- tree_summarize: Query the LLM using the summary_template prompt as many times as needed so that all concatenated chunks
  have been queried, resulting in as many answers that are themselves recursively used as chunks in a tree_summarize LLM call
  and so on, until there's only one chunk left, and thus only one final answer.
```
tree_summarize
```

```
summary_template
```

```
tree_summarize
```

Details: concatenate the chunks as much as possible to fit within the context window using the summary_template prompt,
  and split them if needed (again with a TokenTextSplitter and some text overlap). Then, query each resulting chunk/split against
  summary_template (there is no refine query !) and get as many answers.

```
summary_template
```

```
TokenTextSplitter
```

```
summary_template
```

If there is only one answer (because there was only one chunk), then it's the final answer.

If there are more than one answer, these themselves are considered as chunks and sent recursively
  to the tree_summarize process (concatenated/splitted-to-fit/queried).

```
tree_summarize
```

Good for summarization purposes.

- simple_summarize: Truncates all text chunks to fit into a single LLM prompt. Good for quick
  summarization purposes, but may lose detail due to truncation.
```
simple_summarize
```

- no_text: Only runs the retriever to fetch the nodes that would have been sent to the LLM,
  without actually sending them. Then can be inspected by checking response.source_nodes.
```
no_text
```

```
response.source_nodes
```

- context_only: Returns a concatenated string of all text chunks.
```
context_only
```

- accumulate: Given a set of text chunks and the query, apply the query to each text
  chunk while accumulating the responses into an array. Returns a concatenated string of all
  responses. Good for when you need to run the same query separately against each text
  chunk.
```
accumulate
```

- compact_accumulate: The same as accumulate, but will "compact" each LLM prompt similar to
  compact, and run the same query against each text chunk.
```
compact_accumulate
```

```
compact
```

## Custom Response Synthesizers#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/#custom-response-synthesizers)

Each response synthesizer inherits from llama_index.response_synthesizers.base.BaseSynthesizer. The base API is extremely simple, which makes it easy to create your own response synthesizer.

```
llama_index.response_synthesizers.base.BaseSynthesizer
```

Maybe you want to customize which template is used at each step in tree_summarize, or maybe a new research paper came out detailing a new way to generate a response to a query, you can create your own response synthesizer and plug it into any query engine or use it on it's own.

```
tree_summarize
```

Below we show the __init__() function, as well as the two abstract methods that every response synthesizer must implement. The basic requirements are to process a query and text chunks, and return a string (or string generator) response.

```
__init__()
```

```
from llama_index.core import Settings


class BaseSynthesizer(ABC):
    """Response builder class."""

    def __init__(
        self,
        llm: Optional[LLM] = None,
        streaming: bool = False,
    ) -> None:
        """Init params."""
        self._llm = llm or Settings.llm
        self._callback_manager = Settings.callback_manager
        self._streaming = streaming

    @abstractmethod
    def get_response(
        self,
        query_str: str,
        text_chunks: Sequence[str],
        **response_kwargs: Any,
    ) -> RESPONSE_TEXT_TYPE:
        """Get response."""
        ...

    @abstractmethod
    async def aget_response(
        self,
        query_str: str,
        text_chunks: Sequence[str],
        **response_kwargs: Any,
    ) -> RESPONSE_TEXT_TYPE:
        """Get response."""
        ...
```

```
from llama_index.core import Settings


class BaseSynthesizer(ABC):
    """Response builder class."""

    def __init__(
        self,
        llm: Optional[LLM] = None,
        streaming: bool = False,
    ) -> None:
        """Init params."""
        self._llm = llm or Settings.llm
        self._callback_manager = Settings.callback_manager
        self._streaming = streaming

    @abstractmethod
    def get_response(
        self,
        query_str: str,
        text_chunks: Sequence[str],
        **response_kwargs: Any,
    ) -> RESPONSE_TEXT_TYPE:
        """Get response."""
        ...

    @abstractmethod
    async def aget_response(
        self,
        query_str: str,
        text_chunks: Sequence[str],
        **response_kwargs: Any,
    ) -> RESPONSE_TEXT_TYPE:
        """Get response."""
        ...
```

## Using Structured Answer Filtering#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/#using-structured-answer-filtering)

When using either the "refine" or "compact" response synthesis modules, you may find it beneficial to experiment with the structured_answer_filtering option.

```
"refine"
```

```
"compact"
```

```
structured_answer_filtering
```

```
from llama_index.core import get_response_synthesizer

response_synthesizer = get_response_synthesizer(structured_answer_filtering=True)
```

```
from llama_index.core import get_response_synthesizer

response_synthesizer = get_response_synthesizer(structured_answer_filtering=True)
```

With structured_answer_filtering set to True, our refine module is able to filter out any input nodes that are not relevant to the question being asked. This is particularly useful for RAG-based Q&A systems that involve retrieving chunks of text from external vector store for a given user query.

```
structured_answer_filtering
```

```
True
```

This option is particularly useful if you're using an [OpenAI model that supports function calling](https://openai.com/blog/function-calling-and-other-api-updates). Other LLM providers or models that don't have native function calling support may be less reliable in producing the structured response this feature relies on.

## Using Custom Prompt Templates (with additional variables)#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/#using-custom-prompt-templates-with-additional-variables)

You may want to customize the prompts used in our response synthesizer, and also add additional variables during query-time.

You can specify these additional variables in the **kwargs for get_response.

```
**kwargs
```

```
get_response
```

For example,

```
from llama_index.core import PromptTemplate
from llama_index.core.response_synthesizers import TreeSummarize

# NOTE: we add an extra tone_name variable here
qa_prompt_tmpl = (
    "Context information is below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Given the context information and not prior knowledge, "
    "answer the query.\n"
    "Please also write the answer in the tone of {tone_name}.\n"
    "Query: {query_str}\n"
    "Answer: "
)
qa_prompt = PromptTemplate(qa_prompt_tmpl)

# initialize response synthesizer
summarizer = TreeSummarize(verbose=True, summary_template=qa_prompt)

# get response
response = summarizer.get_response(
    "who is Paul Graham?", [text], tone_name="a Shakespeare play"
)
```

```
from llama_index.core import PromptTemplate
from llama_index.core.response_synthesizers import TreeSummarize

# NOTE: we add an extra tone_name variable here
qa_prompt_tmpl = (
    "Context information is below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Given the context information and not prior knowledge, "
    "answer the query.\n"
    "Please also write the answer in the tone of {tone_name}.\n"
    "Query: {query_str}\n"
    "Answer: "
)
qa_prompt = PromptTemplate(qa_prompt_tmpl)

# initialize response synthesizer
summarizer = TreeSummarize(verbose=True, summary_template=qa_prompt)

# get response
response = summarizer.get_response(
    "who is Paul Graham?", [text], tone_name="a Shakespeare play"
)
```

## Modules#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/#modules)

See the full [module guide](https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/response_synthesizers/) for more details.

