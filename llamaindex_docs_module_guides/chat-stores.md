# Chat Stores#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/storing/chat_stores/

# Chat Stores#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/chat_stores/#chat-stores)

A chat store serves as a centralized interface to store your chat history. Chat history is unique compared to other storage formats, since the order of messages is important for maintaining an overall conversation.

Chat stores can organize sequences of chat messages by keys (like user_ids or other unique identifiable strings), and handle delete, insert, and get operations.

```
user_ids
```

```
delete
```

```
insert
```

```
get
```

## SimpleChatStore#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/chat_stores/#simplechatstore)

The most basic chat store is SimpleChatStore, which stores messages in memory and can save to/from disk, or can be serialized and stored elsewhere.

```
SimpleChatStore
```

Typically, you will instantiate a chat store and give it to a memory module. Memory modules that use chat stores will default to using SimpleChatStore if not provided.

```
SimpleChatStore
```

```
from llama_index.core.storage.chat_store import SimpleChatStore
from llama_index.core.memory import ChatMemoryBuffer

chat_store = SimpleChatStore()

chat_memory = ChatMemoryBuffer.from_defaults(
    token_limit=3000,
    chat_store=chat_store,
    chat_store_key="user1",
)
```

```
from llama_index.core.storage.chat_store import SimpleChatStore
from llama_index.core.memory import ChatMemoryBuffer

chat_store = SimpleChatStore()

chat_memory = ChatMemoryBuffer.from_defaults(
    token_limit=3000,
    chat_store=chat_store,
    chat_store_key="user1",
)
```

Once you have the memory created, you might include it in an agent or chat engine:

```
agent = OpenAIAgent.from_tools(tools, memory=memory)
# OR
chat_engine = index.as_chat_engine(memory=memory)
```

```
agent = OpenAIAgent.from_tools(tools, memory=memory)
# OR
chat_engine = index.as_chat_engine(memory=memory)
```

To save the chat store for later, you can either save/load from disk

```
chat_store.persist(persist_path="chat_store.json")
loaded_chat_store = SimpleChatStore.from_persist_path(
    persist_path="chat_store.json"
)
```

```
chat_store.persist(persist_path="chat_store.json")
loaded_chat_store = SimpleChatStore.from_persist_path(
    persist_path="chat_store.json"
)
```

Or you can convert to/from a string, saving the string somewhere else along the way

```
chat_store_string = chat_store.json()
loaded_chat_store = SimpleChatStore.parse_raw(chat_store_string)
```

```
chat_store_string = chat_store.json()
loaded_chat_store = SimpleChatStore.parse_raw(chat_store_string)
```

## UpstashChatStore#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/chat_stores/#upstashchatstore)

Using UpstashChatStore, you can store your chat history remotely using Upstash Redis, which offers a serverless Redis solution, making it ideal for applications that require scalable and efficient chat storage.
This chat store supports both synchronous and asynchronous operations.

```
UpstashChatStore
```

### Installation#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/chat_stores/#installation)

```
pip install llama-index-storage-chat-store-upstash
```

```
pip install llama-index-storage-chat-store-upstash
```

### Usage#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/chat_stores/#usage)

```
from llama_index.storage.chat_store.upstash import UpstashChatStore
from llama_index.core.memory import ChatMemoryBuffer

chat_store = UpstashChatStore(
    redis_url="YOUR_UPSTASH_REDIS_URL",
    redis_token="YOUR_UPSTASH_REDIS_TOKEN",
    ttl=300,  # Optional: Time to live in seconds
)

chat_memory = ChatMemoryBuffer.from_defaults(
    token_limit=3000,
    chat_store=chat_store,
    chat_store_key="user1",
)
```

```
from llama_index.storage.chat_store.upstash import UpstashChatStore
from llama_index.core.memory import ChatMemoryBuffer

chat_store = UpstashChatStore(
    redis_url="YOUR_UPSTASH_REDIS_URL",
    redis_token="YOUR_UPSTASH_REDIS_TOKEN",
    ttl=300,  # Optional: Time to live in seconds
)

chat_memory = ChatMemoryBuffer.from_defaults(
    token_limit=3000,
    chat_store=chat_store,
    chat_store_key="user1",
)
```

UpstashChatStore supports both synchronous and asynchronous operations. Here's an example of using async methods:

```
import asyncio
from llama_index.core.llms import ChatMessage


async def main():
    # Add messages
    messages = [
        ChatMessage(content="Hello", role="user"),
        ChatMessage(content="Hi there!", role="assistant"),
    ]
    await chat_store.async_set_messages("conversation1", messages)

    # Retrieve messages
    retrieved_messages = await chat_store.async_get_messages("conversation1")
    print(retrieved_messages)

    # Delete last message
    deleted_message = await chat_store.async_delete_last_message(
        "conversation1"
    )
    print(f"Deleted message: {deleted_message}")


asyncio.run(main())
```

```
import asyncio
from llama_index.core.llms import ChatMessage


async def main():
    # Add messages
    messages = [
        ChatMessage(content="Hello", role="user"),
        ChatMessage(content="Hi there!", role="assistant"),
    ]
    await chat_store.async_set_messages("conversation1", messages)

    # Retrieve messages
    retrieved_messages = await chat_store.async_get_messages("conversation1")
    print(retrieved_messages)

    # Delete last message
    deleted_message = await chat_store.async_delete_last_message(
        "conversation1"
    )
    print(f"Deleted message: {deleted_message}")


asyncio.run(main())
```

## RedisChatStore#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/chat_stores/#redischatstore)

Using RedisChatStore, you can store your chat history remotely, without having to worry about manually persisting and loading the chat history.

```
RedisChatStore
```

```
from llama_index.storage.chat_store.redis import RedisChatStore
from llama_index.core.memory import ChatMemoryBuffer

chat_store = RedisChatStore(redis_url="redis://localhost:6379", ttl=300)

chat_memory = ChatMemoryBuffer.from_defaults(
    token_limit=3000,
    chat_store=chat_store,
    chat_store_key="user1",
)
```

```
from llama_index.storage.chat_store.redis import RedisChatStore
from llama_index.core.memory import ChatMemoryBuffer

chat_store = RedisChatStore(redis_url="redis://localhost:6379", ttl=300)

chat_memory = ChatMemoryBuffer.from_defaults(
    token_limit=3000,
    chat_store=chat_store,
    chat_store_key="user1",
)
```

## AzureChatStore#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/chat_stores/#azurechatstore)

Using AzureChatStore, you can store your chat history remotely in Azure Table Storage or CosmosDB, without having to worry about manually persisting and loading the chat history.

```
AzureChatStore
```

```
pip install llama-index
pip install llama-index-llms-azure-openai
pip install llama-index-storage-chat-store-azure
```

```
pip install llama-index
pip install llama-index-llms-azure-openai
pip install llama-index-storage-chat-store-azure
```

```
from llama_index.core.chat_engine import SimpleChatEngine
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.storage.chat_store.azure import AzureChatStore

chat_store = AzureChatStore.from_account_and_key(
    account_name="",
    account_key="",
    chat_table_name="ChatUser",
)

memory = ChatMemoryBuffer.from_defaults(
    token_limit=3000,
    chat_store=chat_store,
    chat_store_key="conversation1",
)

chat_engine = SimpleChatEngine(
    memory=memory, llm=Settings.llm, prefix_messages=[]
)

response = chat_engine.chat("Hello.")
```

```
from llama_index.core.chat_engine import SimpleChatEngine
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.storage.chat_store.azure import AzureChatStore

chat_store = AzureChatStore.from_account_and_key(
    account_name="",
    account_key="",
    chat_table_name="ChatUser",
)

memory = ChatMemoryBuffer.from_defaults(
    token_limit=3000,
    chat_store=chat_store,
    chat_store_key="conversation1",
)

chat_engine = SimpleChatEngine(
    memory=memory, llm=Settings.llm, prefix_messages=[]
)

response = chat_engine.chat("Hello.")
```

## DynamoDBChatStore#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/chat_stores/#dynamodbchatstore)

Using DynamoDBChatStore, you can store your chat history in AWS DynamoDB.

```
DynamoDBChatStore
```

### Installation#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/chat_stores/#installation_1)

```
pip install llama-index-storage-chat-store-dynamodb
```

```
pip install llama-index-storage-chat-store-dynamodb
```

### Usage#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/chat_stores/#usage_1)

Ensure you have a DynamoDB table created with the appropriate schema. By default, here is an example:

```
import boto3

# Get the service resource.
dynamodb = boto3.resource("dynamodb")

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName="EXAMPLE_TABLE",
    KeySchema=[{"AttributeName": "SessionId", "KeyType": "HASH"}],
    AttributeDefinitions=[
        {"AttributeName": "SessionId", "AttributeType": "S"}
    ],
    BillingMode="PAY_PER_REQUEST",
)
```

```
import boto3

# Get the service resource.
dynamodb = boto3.resource("dynamodb")

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName="EXAMPLE_TABLE",
    KeySchema=[{"AttributeName": "SessionId", "KeyType": "HASH"}],
    AttributeDefinitions=[
        {"AttributeName": "SessionId", "AttributeType": "S"}
    ],
    BillingMode="PAY_PER_REQUEST",
)
```

You can then use the DynamoDBChatStore class to persist and retrieve chat histories:

```
DynamoDBChatStore
```

```
import os
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.storage.chat_store.dynamodb.base import DynamoDBChatStore

# Initialize DynamoDB chat store
chat_store = DynamoDBChatStore(
    table_name="EXAMPLE_TABLE", profile_name=os.getenv("AWS_PROFILE")
)

# A chat history, which doesn't exist yet, returns an empty array.
print(chat_store.get_messages("123"))
# >>> []

# Initializing a chat history with a key of "SessionID = 123"
messages = [
    ChatMessage(role=MessageRole.USER, content="Who are you?"),
    ChatMessage(
        role=MessageRole.ASSISTANT, content="I am your helpful AI assistant."
    ),
]
chat_store.set_messages(key="123", messages=messages)
print(chat_store.get_messages("123"))
# >>> [ChatMessage(role=<MessageRole.USER: 'user'>, content='Who are you?', additional_kwargs={}),
#      ChatMessage(role=<MessageRole.ASSISTANT: 'assistant'>, content='I am your helpful AI assistant.', additional_kwargs={})]]

# Appending a message to an existing chat history
message = ChatMessage(role=MessageRole.USER, content="What can you do?")
chat_store.add_message(key="123", message=message)
print(chat_store.get_messages("123"))
# >>> [ChatMessage(role=<MessageRole.USER: 'user'>, content='Who are you?', additional_kwargs={}),
#      ChatMessage(role=<MessageRole.ASSISTANT: 'assistant'>, content='I am your helpful AI assistant.', additional_kwargs={})],
#      ChatMessage(role=<MessageRole.USER: 'user'>, content='What can you do?', additional_kwargs={})]
```

```
import os
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.storage.chat_store.dynamodb.base import DynamoDBChatStore

# Initialize DynamoDB chat store
chat_store = DynamoDBChatStore(
    table_name="EXAMPLE_TABLE", profile_name=os.getenv("AWS_PROFILE")
)

# A chat history, which doesn't exist yet, returns an empty array.
print(chat_store.get_messages("123"))
# >>> []

# Initializing a chat history with a key of "SessionID = 123"
messages = [
    ChatMessage(role=MessageRole.USER, content="Who are you?"),
    ChatMessage(
        role=MessageRole.ASSISTANT, content="I am your helpful AI assistant."
    ),
]
chat_store.set_messages(key="123", messages=messages)
print(chat_store.get_messages("123"))
# >>> [ChatMessage(role=<MessageRole.USER: 'user'>, content='Who are you?', additional_kwargs={}),
#      ChatMessage(role=<MessageRole.ASSISTANT: 'assistant'>, content='I am your helpful AI assistant.', additional_kwargs={})]]

# Appending a message to an existing chat history
message = ChatMessage(role=MessageRole.USER, content="What can you do?")
chat_store.add_message(key="123", message=message)
print(chat_store.get_messages("123"))
# >>> [ChatMessage(role=<MessageRole.USER: 'user'>, content='Who are you?', additional_kwargs={}),
#      ChatMessage(role=<MessageRole.ASSISTANT: 'assistant'>, content='I am your helpful AI assistant.', additional_kwargs={})],
#      ChatMessage(role=<MessageRole.USER: 'user'>, content='What can you do?', additional_kwargs={})]
```

## PostgresChatStore#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/chat_stores/#postgreschatstore)

Using PostgresChatStore, you can store your chat history remotely, without having to worry about manually persisting and loading the chat history.

```
PostgresChatStore
```

```
from llama_index.storage.chat_store.postgres import PostgresChatStore
from llama_index.core.memory import ChatMemoryBuffer

chat_store = PostgresChatStore.from_uri(
    uri="postgresql+asyncpg://postgres:[email protected]:5432/database",
)

chat_memory = ChatMemoryBuffer.from_defaults(
    token_limit=3000,
    chat_store=chat_store,
    chat_store_key="user1",
)
```

```
from llama_index.storage.chat_store.postgres import PostgresChatStore
from llama_index.core.memory import ChatMemoryBuffer

chat_store = PostgresChatStore.from_uri(
    uri="postgresql+asyncpg://postgres:[email protected]:5432/database",
)

chat_memory = ChatMemoryBuffer.from_defaults(
    token_limit=3000,
    chat_store=chat_store,
    chat_store_key="user1",
)
```

[[email protected]](https://docs.llamaindex.ai/cdn-cgi/l/email-protection)

