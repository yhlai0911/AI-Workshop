# Chat Engine#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/

# Chat Engine#

[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/#chat-engine)

## Concept#

[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/#concept)

Chat engine is a high-level interface for having a conversation with your data
(multiple back-and-forth instead of a single question & answer).
Think ChatGPT, but augmented with your knowledge base.

Conceptually, it is a stateful analogy of a [Query Engine](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/).
By keeping track of the conversation history, it can answer questions with past context in mind.

Tip

If you want to ask standalone question over your data (i.e. without keeping track of conversation history), use [Query Engine](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/) instead.

## Usage Pattern#

[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/#usage-pattern)

Get started with:

```
chat_engine = index.as_chat_engine()
response = chat_engine.chat("Tell me a joke.")
```

```
chat_engine = index.as_chat_engine()
response = chat_engine.chat("Tell me a joke.")
```

To stream response:

```
chat_engine = index.as_chat_engine()
streaming_response = chat_engine.stream_chat("Tell me a joke.")
for token in streaming_response.response_gen:
    print(token, end="")
```

```
chat_engine = index.as_chat_engine()
streaming_response = chat_engine.stream_chat("Tell me a joke.")
for token in streaming_response.response_gen:
    print(token, end="")
```

More details in the complete [usage pattern guide](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/usage_pattern/).

## Modules#

[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/#modules)

In our [modules section](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/modules/), you can find corresponding tutorials to see the available chat engines in action.

