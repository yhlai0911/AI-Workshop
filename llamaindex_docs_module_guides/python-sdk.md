# Python SDK#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/40_python_sdk/

# Python SDK#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/40_python_sdk/#python-sdk)

Llama Deploy provides a Python SDK for interacting with deployed systems. The SDK supports both synchronous and
asynchronous operations through a unified client interface. The asynchronous API is recommended for production use.

## Getting started#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/40_python_sdk/#getting-started)

Creating a client is as simple as this:

```
import llama_deploy

client = llama_deploy.Client()
```

```
import llama_deploy

client = llama_deploy.Client()
```

## Client Configuration#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/40_python_sdk/#client-configuration)

The client can be configured either through constructor arguments or environment variables.
To set a configuration parameter through environment variables, their name should be the
uppercase version of the parameter name, prefixed by the string LLAMA_DEPLOY_:

```
LLAMA_DEPLOY_
```

```
import os
import llama_deploy

# Set `disable_ssl` to False with an environment variable
os.environ["LLAMA_DEPLOY_DISABLE_SSL"] = "False"


async def check_status():
    # Pass other config settings to the Client constructor
    client = llama_deploy.Client(
        api_server_url="http://localhost:4501", timeout=10
    )
    status = await client.apiserver.status()
    print(status)
```

```
import os
import llama_deploy

# Set `disable_ssl` to False with an environment variable
os.environ["LLAMA_DEPLOY_DISABLE_SSL"] = "False"


async def check_status():
    # Pass other config settings to the Client constructor
    client = llama_deploy.Client(
        api_server_url="http://localhost:4501", timeout=10
    )
    status = await client.apiserver.status()
    print(status)
```

Note

For a list of all the available configuration parameters, see the dedicated
 [API Reference section](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/python_sdk/).

## Client Components#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/40_python_sdk/#client-components)

The client provides access to two main components:

- apiserver: Interact with the [API server](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/#apiserver)
```
apiserver
```

- core: Access [core functionalities](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/#control-plane) like the Control Plane.
```
core
```

Each component exposes specific methods for managing and interacting with the deployed system.

Note

For a complete list of available methods and detailed API reference, see the
 [API Reference section](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/python_sdk/).

## Usage Examples#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/40_python_sdk/#usage-examples)

### Asynchronous Operations#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/40_python_sdk/#asynchronous-operations)

```
import llama_deploy


async def check_status():
    client = llama_deploy.Client()
    status = await client.apiserver.status()
    print(status)
```

```
import llama_deploy


async def check_status():
    client = llama_deploy.Client()
    status = await client.apiserver.status()
    print(status)
```

### Synchronous Operations#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/40_python_sdk/#synchronous-operations)

```
import llama_deploy

client = llama_deploy.Client()
status = client.sync.apiserver.status()
print(status)
```

```
import llama_deploy

client = llama_deploy.Client()
status = client.sync.apiserver.status()
print(status)
```

Important

The synchronous API (client.sync) cannot be used within an async event loop.
 Use the async methods directly in that case.

```
client.sync
```

### A more complex example#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/40_python_sdk/#a-more-complex-example)

This is an example of how you would use the recommended async version of the client to
run a deployed workflow and collect the events it streams.

```
import llama_deploy


async def stream_events(services):
    client = llama_deploy.Client(timeout=10)

    # Create a new session
    session = await client.core.sessions.create()

    # Assuming there's a workflow called `streaming_workflow`, run it in the background
    task_id = await session.run_nowait(
        "streaming_workflow", arg="Hello, world!"
    )

    # The workflow is supposed to stream events signalling its progress
    async for event in session.get_task_result_stream(task_id):
        if "progress" in event:
            print(f'Workflow Progress: {event["progress"]}')

    # When done, collect the workflow output
    final_result = await session.get_task_result(task_id)
    print(final_result)

    # Clean up the session
    await client.core.sessions.delete(session.id)
```

```
import llama_deploy


async def stream_events(services):
    client = llama_deploy.Client(timeout=10)

    # Create a new session
    session = await client.core.sessions.create()

    # Assuming there's a workflow called `streaming_workflow`, run it in the background
    task_id = await session.run_nowait(
        "streaming_workflow", arg="Hello, world!"
    )

    # The workflow is supposed to stream events signalling its progress
    async for event in session.get_task_result_stream(task_id):
        if "progress" in event:
            print(f'Workflow Progress: {event["progress"]}')

    # When done, collect the workflow output
    final_result = await session.get_task_result(task_id)
    print(final_result)

    # Clean up the session
    await client.core.sessions.delete(session.id)
```

The equivalent synchronous version would be the following:

```
import llama_deploy


def stream_events(services):
    client = llama_deploy.Client(timeout=10)

    # Create a new session
    session = client.sync.core.sessions.create()

    # Assuming there's a workflow called `streaming_workflow`, run it
    task_id = session.run_nowait("streaming_workflow", arg1="hello_world")

    # The workflow is supposed to stream events signalling its progress.
    # Since this is a synchronous call, by this time all the events were
    # streamed and collected in a list.
    for event in session.get_task_result_stream(task_id):
        if "progress" in event:
            print(f'Workflow Progress: {event["progress"]}')

    # Collect the workflow output
    final_result = session.get_task_result(task_id)
    print(final_result)

    # Clean up the session
    client.sync.core.sessions.delete(session.id)
```

```
import llama_deploy


def stream_events(services):
    client = llama_deploy.Client(timeout=10)

    # Create a new session
    session = client.sync.core.sessions.create()

    # Assuming there's a workflow called `streaming_workflow`, run it
    task_id = session.run_nowait("streaming_workflow", arg1="hello_world")

    # The workflow is supposed to stream events signalling its progress.
    # Since this is a synchronous call, by this time all the events were
    # streamed and collected in a list.
    for event in session.get_task_result_stream(task_id):
        if "progress" in event:
            print(f'Workflow Progress: {event["progress"]}')

    # Collect the workflow output
    final_result = session.get_task_result(task_id)
    print(final_result)

    # Clean up the session
    client.sync.core.sessions.delete(session.id)
```

