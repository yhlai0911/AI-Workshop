# 🦙 Llama Deploy 🤖#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/

# 🦙 Llama Deploy 🤖#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/#llama-deploy)

Llama Deploy (formerly llama-agents) is an async-first framework for deploying, scaling, and productionizing agentic
multi-service systems based on [workflows from llama_index](https://docs.llamaindex.ai/en/stable/understanding/workflows/).
With Llama Deploy, you can build any number of workflows in llama_index and then run them as services, accessible
through a HTTP API by a user interface or other services part of your system.

```
llama-agents
```

```
llama_index
```

```
llama_index
```

The goal of Llama Deploy is to easily transition something that you built in a notebook to something running on the
cloud with the minimum amount of changes to the original code, possibly zero. In order to make this transition a
pleasant one, the intrinsic complexity of running agents as services is managed by a component called
[API Server](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/#api-server), the only one in Llama Deploy that's user facing. You can interact
with the [API Server](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/#api-server) in two ways:

- Using the [llamactl](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/50_llamactl/) CLI from a shell.
```
llamactl
```

- Through the [LLama Deploy SDK](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/40_python_sdk/) from a Python application or script.
Both the SDK and the CLI are distributed with the Llama Deploy Python package, so batteries are included.

The overall system layout is pictured below.

## Why Llama Deploy?#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/#why-llama-deploy)

1. Seamless Deployment: It bridges the gap between development and production, allowing you to deploy llama_index
   workflows with minimal changes to your code.
```
llama_index
```

1. Scalability: The microservices architecture enables easy scaling of individual components as your system grows.
1. Flexibility: By using a hub-and-spoke architecture, you can easily swap out components (like message queues) or
   add new services without disrupting the entire system.
1. Fault Tolerance: With built-in retry mechanisms and failure handling, Llama Deploy adds robustness in
   production environments.
1. State Management: The control plane manages state across services, simplifying complex multi-step processes.
1. Async-First: Designed for high-concurrency scenarios, making it suitable for real-time and high-throughput
   applications.
## Wait, where is llama-agents?#

```
llama-agents
```

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/#wait-where-is-llama-agents)

The introduction of [Workflows](https://docs.llamaindex.ai/en/stable/module_guides/workflow/#workflows) in llama_index
turned out to be the most intuitive way for our users to develop agentic applications. While we keep building more and
more features to support agentic applications into llama_index, Llama Deploy focuses on closing the gap between local
development and remote execution of agents as services.

```
llama_index
```

```
llama_index
```

## Installation#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/#installation)

llama_deploy can be installed with pip, and includes the API Server Python SDK and llamactl:

```
llama_deploy
```

```
llamactl
```

```
pip install llama_deploy
```

```
pip install llama_deploy
```

