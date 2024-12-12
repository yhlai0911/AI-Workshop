# Enhancing with LlamaParse#

原始連結：https://docs.llamaindex.ai/en/stable/understanding/agent/llamaparse/

# Enhancing with LlamaParse#

[#](https://docs.llamaindex.ai/en/stable/understanding/agent/llamaparse/#enhancing-with-llamaparse)

In the previous example we asked a very basic question of our document, about the total amount of the budget. Let's instead ask a more complicated question about a specific fact in the document:

```
documents = SimpleDirectoryReader("./data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

response = query_engine.query(
    "How much exactly was allocated to a tax credit to promote investment in green technologies in the 2023 Canadian federal budget?"
)
print(response)
```

```
documents = SimpleDirectoryReader("./data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

response = query_engine.query(
    "How much exactly was allocated to a tax credit to promote investment in green technologies in the 2023 Canadian federal budget?"
)
print(response)
```

We unfortunately get an unhelpful answer:

```
The budget allocated funds to a new green investments tax credit, but the exact amount was not specified in the provided context information.
```

```
The budget allocated funds to a new green investments tax credit, but the exact amount was not specified in the provided context information.
```

This is bad, because we happen to know the exact number is in the document! But the PDF is complicated, with tables and multi-column layout, and the LLM is missing the answer. Luckily, we can use LlamaParse to help us out.

First, you need a LlamaCloud API key. You can [get one for free](https://cloud.llamaindex.ai/) by signing up for LlamaCloud. Then put it in your .env file just like your OpenAI key:

```
.env
```

```
LLAMA_CLOUD_API_KEY=llx-xxxxx
```

```
LLAMA_CLOUD_API_KEY=llx-xxxxx
```

Now you're ready to use LlamaParse in your code. Let's bring it in as as import:

```
from llama_parse import LlamaParse
```

```
from llama_parse import LlamaParse
```

And let's put in a second attempt to parse and query the file (note that this uses documents2, index2, etc.) and see if we get a better answer to the exact same question:

```
documents2
```

```
index2
```

```
documents2 = LlamaParse(result_type="markdown").load_data(
    "./data/2023_canadian_budget.pdf"
)
index2 = VectorStoreIndex.from_documents(documents2)
query_engine2 = index2.as_query_engine()

response2 = query_engine2.query(
    "How much exactly was allocated to a tax credit to promote investment in green technologies in the 2023 Canadian federal budget?"
)
print(response2)
```

```
documents2 = LlamaParse(result_type="markdown").load_data(
    "./data/2023_canadian_budget.pdf"
)
index2 = VectorStoreIndex.from_documents(documents2)
query_engine2 = index2.as_query_engine()

response2 = query_engine2.query(
    "How much exactly was allocated to a tax credit to promote investment in green technologies in the 2023 Canadian federal budget?"
)
print(response2)
```

We do!

```
$20 billion was allocated to a tax credit to promote investment in green technologies in the 2023 Canadian federal budget.
```

```
$20 billion was allocated to a tax credit to promote investment in green technologies in the 2023 Canadian federal budget.
```

You can always check [the repo](https://github.com/run-llama/python-agents-tutorial/blob/main/4_llamaparse.py) to what this code looks like.

As you can see, parsing quality makes a big difference to what the LLM can understand, even for relatively simple questions. Next let's see how [memory](https://docs.llamaindex.ai/en/stable/understanding/agent/memory/) can help us with more complex questions.

