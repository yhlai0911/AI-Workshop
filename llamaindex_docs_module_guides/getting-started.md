# Getting Started#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/10_getting_started/

# Getting Started#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/10_getting_started/#getting-started)

Let's start with deploying a simple workflow on a local instance of Llama Deploy. After installing Llama Deploy, create
a src folder and a workflow.py file to it containing the following Python code:

```
src
```

```
workflow.py
```

```
import asyncio
from llama_index.core.workflow import Workflow, StartEvent, StopEvent, step


class EchoWorkflow(Workflow):
    """A dummy workflow with only one step sending back the input given."""

    @step()
    async def run_step(self, ev: StartEvent) -> StopEvent:
        message = str(ev.get("message", ""))
        return StopEvent(result=f"Message received: {message}")


# `echo_workflow` will be imported by Llama Deploy
echo_workflow = EchoWorkflow()


async def main():
    print(await echo_workflow.run(message="Hello!"))


# Make this script runnable from the shell so we can test the workflow execution
if __name__ == "__main__":
    asyncio.run(main())
```

```
import asyncio
from llama_index.core.workflow import Workflow, StartEvent, StopEvent, step


class EchoWorkflow(Workflow):
    """A dummy workflow with only one step sending back the input given."""

    @step()
    async def run_step(self, ev: StartEvent) -> StopEvent:
        message = str(ev.get("message", ""))
        return StopEvent(result=f"Message received: {message}")


# `echo_workflow` will be imported by Llama Deploy
echo_workflow = EchoWorkflow()


async def main():
    print(await echo_workflow.run(message="Hello!"))


# Make this script runnable from the shell so we can test the workflow execution
if __name__ == "__main__":
    asyncio.run(main())
```

Test the workflow runs locally:

```
$ python src/workflow.py
Message received: Hello!
```

```
$ python src/workflow.py
Message received: Hello!
```

Time to deploy that workflow! Create a file called deployment.yml containing the following YAML code:

```
deployment.yml
```

```
name: QuickStart

control-plane:
  port: 8000

default-service: echo_workflow

services:
  echo_workflow:
    name: Echo Workflow
    # We tell Llama Deploy where to look for our workflow
    source:
      # In this case, we instruct Llama Deploy to look in the local filesystem
      type: local
      # The path in the local filesystem where to look. This assumes there's an src folder in the
      # current working directory containing the file workflow.py we created previously
      name: ./src
    # This assumes the file workflow.py contains a variable called `echo_workflow` containing our workflow instance
    path: workflow:echo_workflow
```

```
name: QuickStart

control-plane:
  port: 8000

default-service: echo_workflow

services:
  echo_workflow:
    name: Echo Workflow
    # We tell Llama Deploy where to look for our workflow
    source:
      # In this case, we instruct Llama Deploy to look in the local filesystem
      type: local
      # The path in the local filesystem where to look. This assumes there's an src folder in the
      # current working directory containing the file workflow.py we created previously
      name: ./src
    # This assumes the file workflow.py contains a variable called `echo_workflow` containing our workflow instance
    path: workflow:echo_workflow
```

The YAML code above defines the deployment that Llama Deploy will create and run as a service. As you can
see, this deployment has a name, some configuration for the control plane and one service to wrap our workflow. The
service will look for a Python variable named echo_workflow in a Python module named workflow and run the workflow.

```
echo_workflow
```

```
workflow
```

At this point we have all we need to run this deployment. Ideally, we would have the API server already running
somewhere in the cloud, but to get started let's start an instance locally. Run the following python script from a shell:

```
$ python -m llama_deploy.apiserver
INFO:     Started server process [10842]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:4501 (Press CTRL+C to quit)
```

```
$ python -m llama_deploy.apiserver
INFO:     Started server process [10842]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:4501 (Press CTRL+C to quit)
```

From another shell, use llamactl to create the deployment:

```
llamactl
```

```
$ llamactl deploy deployment.yml
Deployment successful: QuickStart
```

```
$ llamactl deploy deployment.yml
Deployment successful: QuickStart
```

Our workflow is now part of the QuickStart deployment and ready to serve requests! We can use llamactl to interact
with this deployment:

```
QuickStart
```

```
llamactl
```

```
$ llamactl run --deployment QuickStart --arg message 'Hello from my shell!'
Message received: Hello from my shell!
```

```
$ llamactl run --deployment QuickStart --arg message 'Hello from my shell!'
Message received: Hello from my shell!
```

### Run the API server with Docker#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/10_getting_started/#run-the-api-server-with-docker)

Llama Deploy comes with Docker images that can be used to run the API server without effort. In the previous example,
if you have Docker installed, you can replace running the API server locally with python -m llama_deploy.apiserver
with:

```
python -m llama_deploy.apiserver
```

```
$ docker run -p 4501:4501 -v .:/opt/quickstart -w /opt/quickstart llamaindex/llama-deploy
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:4501 (Press CTRL+C to quit)
```

```
$ docker run -p 4501:4501 -v .:/opt/quickstart -w /opt/quickstart llamaindex/llama-deploy
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:4501 (Press CTRL+C to quit)
```

The API server will be available at http://localhost:4501 on your host, so llamactl will work the same as if you
run python -m llama_deploy.apiserver.

```
http://localhost:4501
```

```
llamactl
```

```
python -m llama_deploy.apiserver
```

