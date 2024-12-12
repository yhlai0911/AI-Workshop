# Core Components#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/

# Core Components#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/#core-components)

Llama Deploy consists of several core components acting as services in order to provide the environment where
multi-agent applications can run and communicate with each other. This sections details each and every component and
will help you navigate the rest of the documentation.

## Deployment#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/#deployment)

In Llama Deploy each workflow is wrapped in a [Service](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/#service) object, endlessly processing incoming requests in
form of [Task](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/#task) objects. Each service pulls and publishes messages to and from a [Message Queue](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/#message-queue).
An internal component called [Control Plane](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/#control-plane) handles ongoing tasks, manages the internal state, keeps
track of which services are available, and decides which service should handle the next step of a task using another
internal component called [Orchestrator](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/#orchestrator).

A well defined set of these components is called Deployment.

Deployments can be defined with YAML code, for example:

```
name: QuickStart

control-plane:
  port: 8000

default-service: dummy_workflow

services:
  dummy_workflow:
    name: Dummy Workflow
    source:
      type: local
      name: src
    path: workflow:echo_workflow
```

```
name: QuickStart

control-plane:
  port: 8000

default-service: dummy_workflow

services:
  dummy_workflow:
    name: Dummy Workflow
    source:
      type: local
      name: src
    path: workflow:echo_workflow
```

For more details, see the API reference for the deployment [Config](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/apiserver/#llama_deploy.apiserver.config_parser.Config) object.

```
Config
```

## API Server#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/#api-server)

The API Server is a core component of Llama Deploy responsible for serving and managing multiple deployments. It is
responsible for running and managing multiple deployments at the same time, and it exposes a HTTP API that can be used
for administrative purposes as well as for querying the deployed services. You can interact with the administrative
API through [llamactl](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/50_llamactl/) or the [Python SDK](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/40_python_sdk/).

```
llamactl
```

For more details see [the Python API reference](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/apiserver/), while the administrative
API is documented below.

## Control Plane#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/#control-plane)

The control plane is responsible for managing the state of the system, including:

- Registering services.
- Managing sessions and tasks.
- Handling service completion.
- Launching the control plane server.
The state of the system is persisted in a key-value store that by default consists of a simple mapping in memory.
In particular, the state store contains:

- The name and definition of the registered services.
- The active sessions and their relative tasks and event streams.
- The Context, in case the service is of type Workflow,
In case you need a more scalable storage for the system state, you can set the state_store_uri field in the Control
Plane configuration to point to one of the databases we support (see
[the Python API reference](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/control_plane/)) for more details.
Using a scalable storage for the global state is mostly needed when:
- You want to scale the control plane horizontally, and you want every instance to share the same global state.
- The control plane has to deal with high traffic (many services, sessions and tasks).
- The global state needs to be persisted across restarts (for example, workflow contexts are stored in the global state).

```
state_store_uri
```

## Service#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/#service)

The general structure of a service is as follows:

- A service has a name.
- A service has a service definition.
- A service uses a message queue to send/receive messages.
- A service has a processing loop, for continuous processing of messages.
- A service can process a message.
- A service can publish a message to another service.
- A service can be launched in-process.
- A service can be launched as a server.
- A service can be registered to the control plane.
- A service can be registered to the message queue.
## Message Queue#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/#message-queue)

In addition to SimpleMessageQueue, we provide integrations for various
message queue providers, such as RabbitMQ, Redis, etc. The general usage pattern
for any of these message queues is the same as that for SimpleMessageQueue,
however the appropriate extra would need to be installed along with llama-deploy.

```
SimpleMessageQueue
```

```
SimpleMessageQueue
```

```
llama-deploy
```

For example, for RabbitMQMessageQueue, we need to install the "rabbitmq" extra:

```
RabbitMQMessageQueue
```

```
# using pip install
pip install llama-agents[rabbitmq]

# using poetry
poetry add llama-agents -E "rabbitmq"
```

```
# using pip install
pip install llama-agents[rabbitmq]

# using poetry
poetry add llama-agents -E "rabbitmq"
```

Using the RabbitMQMessageQueue is then done as follows:

```
RabbitMQMessageQueue
```

```
from llama_agents.message_queue.rabbitmq import (
    RabbitMQMessageQueueConfig,
    RabbitMQMessageQueue,
)

message_queue_config = (
    RabbitMQMessageQueueConfig()
)  # loads params from environment vars
message_queue = RabbitMQMessageQueue(**message_queue_config)
```

```
from llama_agents.message_queue.rabbitmq import (
    RabbitMQMessageQueueConfig,
    RabbitMQMessageQueue,
)

message_queue_config = (
    RabbitMQMessageQueueConfig()
)  # loads params from environment vars
message_queue = RabbitMQMessageQueue(**message_queue_config)
```

Note

RabbitMQMessageQueueConfig can load its params from environment variables.

```
RabbitMQMessageQueueConfig
```

## Orchestrator#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/#orchestrator)

The general idea for an orchestrator is to manage the flow of messages between services.

Given some state, and task, figure out the next messages to publish. Then, once
the messages are processed, update the state with the results.

## Task#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/#task)

A Task is an object representing a request for an operation sent to a Service and the response that will be sent back.
For the details you can look at the [API reference](https://docs.llamaindex.ai/en/stable/api_reference/llama_deploy/types/)

