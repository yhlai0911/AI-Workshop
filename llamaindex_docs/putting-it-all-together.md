# Putting It All Together#

原始連結：https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/

# Putting It All Together#

[#](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/#putting-it-all-together)

Congratulations! You've loaded your data, indexed it, stored your index, and queried your index. Now you've got to ship something to production. We can show you how to do that!

- In [Q&A Patterns](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/q_and_a.md) we'll go into some of the more advanced and subtle ways you can build a query engine beyond the basics.
- The [terms definition tutorial](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/q_and_a/terms_definitions_tutorial/) is a detailed, step-by-step tutorial on creating a subtle query application including defining your prompts and supporting images as input.
- We have a guide to [creating a unified query framework over your indexes](https://docs.llamaindex.ai/en/stable/examples/retrievers/reciprocal_rerank_fusion/) which shows you how to run queries across multiple indexes.
- And also over [structured data like SQL](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/structured_data.md)
- We have a guide on [how to build a chatbot](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/chatbots/building_a_chatbot/)
- We talk about [building agents in LlamaIndex](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/agents/)
- We have a complete guide to using [property graphs for indexing and retrieval](https://docs.llamaindex.ai/en/stable/module_guides/indexing/lpg_index_guide/)
- And last but not least we show you how to build [a full stack web application](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/apps/) using LlamaIndex
LlamaIndex also provides some tools / project templates to help you build a full-stack template. For instance, [create-llama](https://github.com/run-llama/LlamaIndexTS/tree/main/packages/create-llama) spins up a full-stack scaffold for you.

```
create-llama
```

Check out our [Full-Stack Projects](https://docs.llamaindex.ai/en/stable/community/full_stack_projects/) page for more details.

We also have the [llamaindex-cli rag CLI tool](https://docs.llamaindex.ai/en/stable/getting_started/starter_tools/rag_cli/) that combines some of the above concepts into an easy to use tool for chatting with files from your terminal!

```
llamaindex-cli rag
```

