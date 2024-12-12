# Introduction to Structured Data Extraction#

原始連結：https://docs.llamaindex.ai/en/stable/understanding/extraction/

# Introduction to Structured Data Extraction#

[#](https://docs.llamaindex.ai/en/stable/understanding/extraction/#introduction-to-structured-data-extraction)

LLMs excel at data understanding, leading to one of their most important use cases: the ability to turn regular human language (which we refer to as unstructured data) into specific, regular, expected formats for consumption by computer programs. We call the output of this process structured data. Since in the process of conversion a lot of superfluous data is often ignored, we call it extraction.

The core of the way structured data extraction works in LlamaIndex is [Pydantic](https://docs.pydantic.dev/latest/) classes: you define a data structure in [Pydantic](https://docs.pydantic.dev/latest/) and LlamaIndex works with [Pydantic](https://docs.pydantic.dev/latest/) to coerce the output of the LLM into that structure.

## What is Pydantic?#

[#](https://docs.llamaindex.ai/en/stable/understanding/extraction/#what-is-pydantic)

Pydantic is a widely-used data validation and conversion library. It relies heavily on Python type declarations. There is an [extensive guide](https://docs.pydantic.dev/latest/concepts/models/) to Pydantic in that project’s documentation, but we’ll cover the very basics here.

To create a Pydantic class, inherit from Pydantic’s BaseModel class:

```
BaseModel
```

```
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "Jane Doe"
```

```
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "Jane Doe"
```

In this example, you’ve created a User class with two fields, id and name. You’ve defined id as an integer, and name as a string that defaults to Jane Doe.

```
User
```

```
id
```

```
name
```

```
id
```

```
name
```

```
Jane Doe
```

You can create more complex structures by nesting these models:

```
from typing import List, Optional
from pydantic import BaseModel


class Foo(BaseModel):
    count: int
    size: Optional[float] = None


class Bar(BaseModel):
    apple: str = "x"
    banana: str = "y"


class Spam(BaseModel):
    foo: Foo
    bars: List[Bar]
```

```
from typing import List, Optional
from pydantic import BaseModel


class Foo(BaseModel):
    count: int
    size: Optional[float] = None


class Bar(BaseModel):
    apple: str = "x"
    banana: str = "y"


class Spam(BaseModel):
    foo: Foo
    bars: List[Bar]
```

Now Spam has a foo and a bars. Foo has a count and an optional size , and bars is a List of objects each of which has an apple and banana property.

```
Spam
```

```
foo
```

```
bars
```

```
Foo
```

```
count
```

```
size
```

```
bars
```

```
apple
```

```
banana
```

## Converting Pydantic objects to JSON schemas#

[#](https://docs.llamaindex.ai/en/stable/understanding/extraction/#converting-pydantic-objects-to-json-schemas)

Pydantic supports converting Pydantic classes into JSON-serialized schema objects which conform to [popular standards](https://docs.pydantic.dev/latest/concepts/json_schema/). The User class above for instance serializes into this:

```
User
```

```
{
  "properties": {
    "id": {
      "title": "Id",
      "type": "integer"
    },
    "name": {
      "default": "Jane Doe",
      "title": "Name",
      "type": "string"
    }
  },
  "required": [
    "id"
  ],
  "title": "User",
  "type": "object"
}
```

```
{
  "properties": {
    "id": {
      "title": "Id",
      "type": "integer"
    },
    "name": {
      "default": "Jane Doe",
      "title": "Name",
      "type": "string"
    }
  },
  "required": [
    "id"
  ],
  "title": "User",
  "type": "object"
}
```

This property is crucial: these JSON-formatted schemas are often passed to LLMs and the LLMs in turn use them as instructions on how to return data.

## Using annotations#

[#](https://docs.llamaindex.ai/en/stable/understanding/extraction/#using-annotations)

As mentioned, LLMs are using JSON schemas from Pydantic as instructions on how to return data. To assist them and improve the accuracy of your returned data, it’s helpful to include natural-language descriptions of objects and fields and what they’re used for. Pydantic has support for this with [docstrings](https://www.geeksforgeeks.org/python-docstrings/) and [Fields](https://docs.pydantic.dev/latest/concepts/fields/).

We’ll be using the following example Pydantic classes in all of our examples going forward:

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

This expands to a much more complex JSON schema:

```
{
  "$defs": {
    "LineItem": {
      "description": "A line item in an invoice.",
      "properties": {
        "item_name": {
          "description": "The name of this item",
          "title": "Item Name",
          "type": "string"
        },
        "price": {
          "description": "The price of this item",
          "title": "Price",
          "type": "number"
        }
      },
      "required": [
        "item_name",
        "price"
      ],
      "title": "LineItem",
      "type": "object"
    }
  },
  "description": "A representation of information from an invoice.",
  "properties": {
    "invoice_id": {
      "description": "A unique identifier for this invoice, often a number",
      "title": "Invoice Id",
      "type": "string"
    },
    "date": {
      "description": "The date this invoice was created",
      "format": "date-time",
      "title": "Date",
      "type": "string"
    },
    "line_items": {
      "description": "A list of all the items in this invoice",
      "items": {
        "$ref": "#/$defs/LineItem"
      },
      "title": "Line Items",
      "type": "array"
    }
  },
  "required": [
    "invoice_id",
    "date",
    "line_items"
  ],
  "title": "Invoice",
  "type": "object"
}
```

```
{
  "$defs": {
    "LineItem": {
      "description": "A line item in an invoice.",
      "properties": {
        "item_name": {
          "description": "The name of this item",
          "title": "Item Name",
          "type": "string"
        },
        "price": {
          "description": "The price of this item",
          "title": "Price",
          "type": "number"
        }
      },
      "required": [
        "item_name",
        "price"
      ],
      "title": "LineItem",
      "type": "object"
    }
  },
  "description": "A representation of information from an invoice.",
  "properties": {
    "invoice_id": {
      "description": "A unique identifier for this invoice, often a number",
      "title": "Invoice Id",
      "type": "string"
    },
    "date": {
      "description": "The date this invoice was created",
      "format": "date-time",
      "title": "Date",
      "type": "string"
    },
    "line_items": {
      "description": "A list of all the items in this invoice",
      "items": {
        "$ref": "#/$defs/LineItem"
      },
      "title": "Line Items",
      "type": "array"
    }
  },
  "required": [
    "invoice_id",
    "date",
    "line_items"
  ],
  "title": "Invoice",
  "type": "object"
}
```

Now that you have a basic understanding of Pydantic and the schemas it generates, you can move on to using Pydantic classes for structured data extraction in LlamaIndex, starting with [Structured LLMs](https://docs.llamaindex.ai/en/stable/understanding/extraction/structured_llms/).

