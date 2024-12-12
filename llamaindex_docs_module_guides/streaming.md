# Streaming#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/streaming/

# Streaming#

[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/streaming/#streaming)

LlamaIndex supports streaming the response as it's being generated.
This allows you to start printing or processing the beginning of the response before the full response is finished.
This can drastically reduce the perceived latency of queries.

### Setup#

[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/streaming/#setup)

To enable streaming, you need to use an LLM that supports streaming.
Right now, streaming is supported by OpenAI, HuggingFaceLLM, and most LangChain LLMs (via LangChainLLM).

```
OpenAI
```

```
HuggingFaceLLM
```

```
LangChainLLM
```

> Note: if streaming is not supported by the LLM you choose a NotImplementedError will be raised.

Note: if streaming is not supported by the LLM you choose a NotImplementedError will be raised.

```
NotImplementedError
```

To configure query engine to use streaming using the high-level API, set streaming=True when building a query engine.

```
streaming=True
```

```
query_engine = index.as_query_engine(streaming=True, similarity_top_k=1)
```

```
query_engine = index.as_query_engine(streaming=True, similarity_top_k=1)
```

If you are using the low-level API to compose the query engine,
pass streaming=True when constructing the Response Synthesizer:

```
streaming=True
```

```
Response Synthesizer
```

```
from llama_index.core import get_response_synthesizer

synth = get_response_synthesizer(streaming=True, ...)
query_engine = RetrieverQueryEngine(response_synthesizer=synth, ...)
```

```
from llama_index.core import get_response_synthesizer

synth = get_response_synthesizer(streaming=True, ...)
query_engine = RetrieverQueryEngine(response_synthesizer=synth, ...)
```

### Streaming Response#

[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/streaming/#streaming-response)

After properly configuring both the LLM and the query engine,
calling query now returns a StreamingResponse object.

```
query
```

```
StreamingResponse
```

```
streaming_response = query_engine.query(
    "What did the author do growing up?",
)
```

```
streaming_response = query_engine.query(
    "What did the author do growing up?",
)
```

The response is returned immediately when the LLM call starts, without having to wait for the full completion.

> Note: In the case where the query engine makes multiple LLM calls, only the last LLM call will be streamed and the response is returned when the last LLM call starts.

Note: In the case where the query engine makes multiple LLM calls, only the last LLM call will be streamed and the response is returned when the last LLM call starts.

You can obtain a Generator from the streaming response and iterate over the tokens as they arrive:

```
Generator
```

```
for text in streaming_response.response_gen:
    # do something with text as they arrive.
    pass
```

```
for text in streaming_response.response_gen:
    # do something with text as they arrive.
    pass
```

Alternatively, if you just want to print the text as they arrive:

```
streaming_response.print_response_stream()
```

```
streaming_response.print_response_stream()
```

See an [end-to-end example](https://docs.llamaindex.ai/en/stable/examples/customization/streaming/SimpleIndexDemo-streaming/)

