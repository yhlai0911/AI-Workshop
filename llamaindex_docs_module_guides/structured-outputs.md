# Structured Outputs#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/

# Structured Outputs#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/#structured-outputs)

The ability of LLMs to produce structured outputs are important for downstream applications that rely on reliably parsing output values.
LlamaIndex itself also relies on structured output in the following ways.

- Document retrieval: Many data structures within LlamaIndex rely on LLM calls with a specific schema for Document retrieval. For instance, the tree index expects LLM calls to be in the format "ANSWER: (number)".
- Response synthesis: Users may expect that the final response contains some degree of structure (e.g. a JSON output, a formatted SQL query, etc.)
LlamaIndex provides a variety of modules enabling LLMs to produce outputs in a structured format. By default, structured output is offered within our LLM classes. We also provide lower-level modules:

- Pydantic Programs: These are generic modules that map an input prompt to a structured output, represented by a Pydantic object. They may use function calling APIs or text completion APIs + output parsers. These can also be integrated with query engines.
- Pre-defined Pydantic Program: We have pre-defined Pydantic programs that map inputs to specific output types (like dataframes).
- Output Parsers: These are modules that operate before and after an LLM text completion endpoint. They are not used with LLM function calling endpoints (since those contain structured outputs out of the box).
See the sections below for an overview of output parsers and Pydantic programs.

## 🔬 Anatomy of a Structured Output Function#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/#anatomy-of-a-structured-output-function)

Here we describe the different components of an LLM-powered structured output function. The pipeline depends on whether you're using a generic LLM text completion API or an LLM function calling API.

With generic completion APIs, the inputs and outputs are handled by text prompts. The output parser plays a role before and after the LLM call in ensuring structured outputs. Before the LLM call, the output parser can
append format instructions to the prompt. After the LLM call, the output parser can parse the output to the specified instructions.

With function calling APIs, the output is inherently in a structured format, and the input can take in the signature of the desired object. The structured output just needs to be cast in the right object format (e.g. Pydantic).

## Starter Guides#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/#starter-guides)

- [Structured data extraction tutorial](https://docs.llamaindex.ai/en/stable/understanding/extraction/)
- [Examples of Structured Outputs](https://docs.llamaindex.ai/en/stable/examples/structured_outputs/structured_outputs/)
## Other Resources#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/#other-resources)

- [Pydantic Programs](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/pydantic_program/)
- [Structured Outputs + Query Engines](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/query_engine/)
- [Output Parsers](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/output_parser/)
