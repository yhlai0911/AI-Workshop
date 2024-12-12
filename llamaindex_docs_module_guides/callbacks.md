# Callbacks#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/observability/callbacks/

# Callbacks#

[#](https://docs.llamaindex.ai/en/stable/module_guides/observability/callbacks/#callbacks)

## Concept#

[#](https://docs.llamaindex.ai/en/stable/module_guides/observability/callbacks/#concept)

LlamaIndex provides callbacks to help debug, track, and trace the inner workings of the library.
Using the callback manager, as many callbacks as needed can be added.

In addition to logging data related to events, you can also track the duration and number of occurrences
of each event.

Furthermore, a trace map of events is also recorded, and callbacks can use this data
however they want. For example, the LlamaDebugHandler will, by default, print the trace of events
after most operations.

```
LlamaDebugHandler
```

Callback Event Types
While each callback may not leverage each event type, the following events are available to be tracked:

- CHUNKING -> Logs for the before and after of text splitting.
```
CHUNKING
```

- NODE_PARSING -> Logs for the documents and the nodes that they are parsed into.
```
NODE_PARSING
```

- EMBEDDING -> Logs for the number of texts embedded.
```
EMBEDDING
```

- LLM -> Logs for the template and response of LLM calls.
```
LLM
```

- QUERY -> Keeps track of the start and end of each query.
```
QUERY
```

- RETRIEVE -> Logs for the nodes retrieved for a query.
```
RETRIEVE
```

- SYNTHESIZE -> Logs for the result for synthesize calls.
```
SYNTHESIZE
```

- TREE -> Logs for the summary and level of summaries generated.
```
TREE
```

- SUB_QUESTION -> Log for a generated sub question and answer.
```
SUB_QUESTION
```

You can implement your own callback to track and trace these events, or use an existing callback.

## Modules#

[#](https://docs.llamaindex.ai/en/stable/module_guides/observability/callbacks/#modules)

Currently supported callbacks are as follows:

- [TokenCountingHandler](https://docs.llamaindex.ai/en/stable/examples/callbacks/TokenCountingHandler.ipynb) -> Flexible token counting for prompt, completion, and embedding token usage. See [the migration details](https://docs.llamaindex.ai/en/stable/module_guides/observability/callbacks/token_counting_migration/)
- [LlamaDebugHanlder](https://docs.llamaindex.ai/en/stable/examples/callbacks/LlamaDebugHandler.ipynb) -> Basic tracking and tracing for events. Example usage can be found in the notebook below.
- [[Wandb](https://docs.wandb.ai/guides/prompts/quickstart)CallbackHandler](https://docs.llamaindex.ai/en/stable/examples/callbacks/[Wandb](https://docs.wandb.ai/guides/prompts/quickstart)CallbackHandler.ipynb) -> Tracking of events and traces using the [Wandb](https://docs.wandb.ai/guides/prompts/quickstart) Prompts frontend. More details are in the notebook below or at [Wandb](https://docs.wandb.ai/guides/prompts/quickstart)
- [AimCallback](https://docs.llamaindex.ai/en/stable/examples/callbacks/AimCallback.ipynb) -> Tracking of LLM inputs and outputs. Example usage can be found in the notebook below.
- [OpenInferenceCallbackHandler](https://docs.llamaindex.ai/en/stable/examples/callbacks/OpenInferenceCallback.ipynb) -> Tracking of AI model inferences. Example usage can be found in the notebook below.
- [OpenAIFineTuningHandler](https://github.com/jerryjliu/llama_index/blob/main/experimental/openai_fine_tuning/openai_fine_tuning.ipynb) -> Records all LLM inputs and outputs. Then, provides a function save_finetuning_events() to save inputs and outputs in a format suitable for fine-tuning with OpenAI.
```
save_finetuning_events()
```

