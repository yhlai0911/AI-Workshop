# Pydantic Programs#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/pydantic_program/

# Pydantic Programs#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/pydantic_program/#pydantic-programs)

Tip

Pydantic Programs are a lower-level abstraction for structured output extraction. The default way to perform structured output extraction is with our LLM classes, which lets you plug these LLMs easily into higher-level workflows. Check out our [structured data extraction tutorial](https://docs.llamaindex.ai/en/stable/understanding/extraction/).

A pydantic program is a generic abstraction that takes in an input string and converts it to a structured Pydantic object type.

Because this abstraction is so generic, it encompasses a broad range of LLM workflows. The programs are composable and be for more generic or specific use cases.

There's a few general types of Pydantic Programs:

- Text Completion Pydantic Programs: These convert input text into a user-specified structured object through a text completion API + output parsing.
- Function Calling Pydantic Programs: These convert input text into a user-specified structured object through an LLM function calling API.
- Prepackaged Pydantic Programs: These convert input text into prespecified structured objects.
## Text Completion Pydantic Programs#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/pydantic_program/#text-completion-pydantic-programs)

See the example notebook on [LLM Text Completion programs](https://docs.llamaindex.ai/en/stable/examples/output_parsing/llm_program/)

## Function Calling Pydantic Programs#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/pydantic_program/#function-calling-pydantic-programs)

- [Function Calling Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/function_program/)
- [OpenAI Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_pydantic_program/)
- [Guidance Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/guidance_pydantic_program/)
- [Guidance Sub-Question Generator](https://docs.llamaindex.ai/en/stable/examples/output_parsing/guidance_sub_question/)
## Prepackaged Pydantic Programs#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/pydantic_program/#prepackaged-pydantic-programs)

- [DF Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/df_program/)
- [Evaporate Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/evaporate_program/)
