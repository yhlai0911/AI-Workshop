# Using Structured LLMs#

原始連結：https://docs.llamaindex.ai/en/stable/understanding/extraction/structured_llms/

# Using Structured LLMs#

[#](https://docs.llamaindex.ai/en/stable/understanding/extraction/structured_llms/#using-structured-llms)

The highest-level way to extract structured data in LlamaIndex is to instantiate a Structured LLM. First, let’s instantiate our Pydantic class as previously:

```
from datetime import datetime


class LineItem(BaseModel):
    """A line item in an invoice."""

    item_name: str = Field(description="The name of this item")
    price: float = Field(description="The price of this item")


class Invoice(BaseModel):
    """A representation of information from an invoice."""

    invoice_id: str = Field(
        description="A unique identifier for this invoice, often a number"
    )
    date: datetime = Field(description="The date this invoice was created")
    line_items: list[LineItem] = Field(
        description="A list of all the items in this invoice"
    )
```

```
from datetime import datetime


class LineItem(BaseModel):
    """A line item in an invoice."""

    item_name: str = Field(description="The name of this item")
    price: float = Field(description="The price of this item")


class Invoice(BaseModel):
    """A representation of information from an invoice."""

    invoice_id: str = Field(
        description="A unique identifier for this invoice, often a number"
    )
    date: datetime = Field(description="The date this invoice was created")
    line_items: list[LineItem] = Field(
        description="A list of all the items in this invoice"
    )
```

If this is your first time using LlamaIndex, let’s get our dependencies:

- pip install llama-index-core llama-index-llms-openai to get the LLM (we’ll be using OpenAI for simplicity, but you can always use another one)
```
pip install llama-index-core llama-index-llms-openai
```

- Get an OpenAI API key and set it as an environment variable called OPENAI_API_KEY
```
OPENAI_API_KEY
```

- pip install llama-index-readers-file to get the PDFReader
Note: for better parsing of PDFs, we recommend [LlamaParse](https://docs.cloud.llamaindex.ai/llamaparse/getting_started)
```
pip install llama-index-readers-file
```

Now let’s load in the text of an actual invoice:

```
from llama_index.readers.file import PDFReader
from pathlib import Path

pdf_reader = PDFReader()
documents = pdf_reader.load_data(file=Path("./uber_receipt.pdf"))
text = documents[0].text
```

```
from llama_index.readers.file import PDFReader
from pathlib import Path

pdf_reader = PDFReader()
documents = pdf_reader.load_data(file=Path("./uber_receipt.pdf"))
text = documents[0].text
```

And let’s instantiate an LLM, give it our Pydantic class, and then ask it to complete using the plain text of the invoice:

```
complete
```

```
from llama_index.llms.openai import OpenAI

llm = OpenAI(model="gpt-4o")
sllm = llm.as_structured_llm(Invoice)

response = sllm.complete(text)
```

```
from llama_index.llms.openai import OpenAI

llm = OpenAI(model="gpt-4o")
sllm = llm.as_structured_llm(Invoice)

response = sllm.complete(text)
```

response is a LlamaIndex CompletionResponse with two properties: text and raw. text contains the JSON-serialized form of the Pydantic-ingested response:

```
response
```

```
CompletionResponse
```

```
text
```

```
raw
```

```
text
```

```
json_response = json.loads(response.text)
print(json.dumps(json_response, indent=2))
```

```
json_response = json.loads(response.text)
print(json.dumps(json_response, indent=2))
```

```
{
    "invoice_id": "Visa \u2022\u2022\u2022\u20224469",
    "date": "2024-10-10T19:49:00",
    "line_items": [
        {"item_name": "Trip fare", "price": 12.18},
        {"item_name": "Access for All Fee", "price": 0.1},
        {"item_name": "CA Driver Benefits", "price": 0.32},
        {"item_name": "Booking Fee", "price": 2.0},
        {"item_name": "San Francisco City Tax", "price": 0.21},
    ],
}
```

```
{
    "invoice_id": "Visa \u2022\u2022\u2022\u20224469",
    "date": "2024-10-10T19:49:00",
    "line_items": [
        {"item_name": "Trip fare", "price": 12.18},
        {"item_name": "Access for All Fee", "price": 0.1},
        {"item_name": "CA Driver Benefits", "price": 0.32},
        {"item_name": "Booking Fee", "price": 2.0},
        {"item_name": "San Francisco City Tax", "price": 0.21},
    ],
}
```

Note that this invoice didn’t have an ID so the LLM has tried its best and used the credit card number. Pydantic validation is not a guarantee!

The raw property of response (somewhat confusingly) contains the Pydantic object itself:

```
raw
```

```
from pprint import pprint

pprint(response.raw)
```

```
from pprint import pprint

pprint(response.raw)
```

```
Invoice(
    invoice_id="Visa ••••4469",
    date=datetime.datetime(2024, 10, 10, 19, 49),
    line_items=[
        LineItem(item_name="Trip fare", price=12.18),
        LineItem(item_name="Access for All Fee", price=0.1),
        LineItem(item_name="CA Driver Benefits", price=0.32),
        LineItem(item_name="Booking Fee", price=2.0),
        LineItem(item_name="San Francisco City Tax", price=0.21),
    ],
)
```

```
Invoice(
    invoice_id="Visa ••••4469",
    date=datetime.datetime(2024, 10, 10, 19, 49),
    line_items=[
        LineItem(item_name="Trip fare", price=12.18),
        LineItem(item_name="Access for All Fee", price=0.1),
        LineItem(item_name="CA Driver Benefits", price=0.32),
        LineItem(item_name="Booking Fee", price=2.0),
        LineItem(item_name="San Francisco City Tax", price=0.21),
    ],
)
```

Note that Pydantic is creating a full datetime object and not just translating a string.

```
datetime
```

A structured LLM works exactly like a regular LLM class: you can call chat, stream, achat, astream etc. and it will respond with Pydantic objects in all cases. You can also pass in your Structured LLM as a parameter to VectorStoreIndex.as_query_engine(llm=sllm) and it will automatically respond to your RAG queries with structured objects.

```
chat
```

```
stream
```

```
achat
```

```
astream
```

```
VectorStoreIndex.as_query_engine(llm=sllm)
```

The Structured LLM takes care of all the prompting for you. If you want more control over the prompt, move on to [Structured Prediction](https://docs.llamaindex.ai/en/stable/understanding/extraction/structured_prediction/).

