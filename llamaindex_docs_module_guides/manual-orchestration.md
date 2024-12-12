# Manual orchestration#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/30_manual_orchestration/

# Manual orchestration#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/30_manual_orchestration/#manual-orchestration)

Llama Deploy offers different abstraction layers for maximum flexibility. For example, if you don't need the [API
server](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/#api-server), you can go down one layer and orchestrate the core components on your own.
Llama Deploy provides a simple way to self-manage a deployment using configuration objects and helper functions.

## Manual orchestration with Python wrappers#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/30_manual_orchestration/#manual-orchestration-with-python-wrappers)

Llama Deploy provides a set of utility functions that wrap the lower-level Python API in order to simplify certain
operations that are common when you need to orchestrate the different core components, let's see how to use them.

### Deploying the Core System#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/30_manual_orchestration/#deploying-the-core-system)

Note

When manually orchestrating a deployment, generally you'll want to deploy the core components and workflows services
each from their own python scripts (or docker images, etc.).

To manually orchestrate a deployment, the first thing to do is to deploy the core system: message queue, control plane,
and orchestrator. You can use the deploy_core function:

```
deploy_core
```

```
from llama_deploy import (
    deploy_core,
    ControlPlaneConfig,
    SimpleMessageQueueConfig,
)


async def main():
    await deploy_core(
        control_plane_config=ControlPlaneConfig(),
        message_queue_config=SimpleMessageQueueConfig(),
    )


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

```
from llama_deploy import (
    deploy_core,
    ControlPlaneConfig,
    SimpleMessageQueueConfig,
)


async def main():
    await deploy_core(
        control_plane_config=ControlPlaneConfig(),
        message_queue_config=SimpleMessageQueueConfig(),
    )


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

This will set up the basic infrastructure for your deployment. You can customize the configs to adjust ports and basic
settings, as well as swap in different message queue configs (Redis, Kafka, RabbiMQ, etc.).

### Deploying a Workflow#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/30_manual_orchestration/#deploying-a-workflow)

To deploy a workflow as a service, you can use the deploy_workflow function:

```
deploy_workflow
```

```
from llama_deploy import (
    deploy_workflow,
    WorkflowServiceConfig,
    ControlPlaneConfig,
    SimpleMessageQueueConfig,
)
from llama_index.core.workflow import (
    Context,
    Event,
    Workflow,
    StartEvent,
    StopEvent,
    step,
)


class ProgressEvent(Event):
    progress: str


# create a dummy workflow
class MyWorkflow(Workflow):
    @step()
    async def run_step(self, ctx: Context, ev: StartEvent) -> StopEvent:
        # Your workflow logic here
        arg1 = str(ev.get("arg1", ""))
        result = arg1 + "_result"

        # stream events as steps run
        ctx.write_event_to_stream(
            ProgressEvent(progress="I am doing something!")
        )

        return StopEvent(result=result)


async def main():
    await deploy_workflow(
        workflow=MyWorkflow(),
        workflow_config=WorkflowServiceConfig(
            host="127.0.0.1", port=8002, service_name="my_workflow"
        ),
        control_plane_config=ControlPlaneConfig(),
    )


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

```
from llama_deploy import (
    deploy_workflow,
    WorkflowServiceConfig,
    ControlPlaneConfig,
    SimpleMessageQueueConfig,
)
from llama_index.core.workflow import (
    Context,
    Event,
    Workflow,
    StartEvent,
    StopEvent,
    step,
)


class ProgressEvent(Event):
    progress: str


# create a dummy workflow
class MyWorkflow(Workflow):
    @step()
    async def run_step(self, ctx: Context, ev: StartEvent) -> StopEvent:
        # Your workflow logic here
        arg1 = str(ev.get("arg1", ""))
        result = arg1 + "_result"

        # stream events as steps run
        ctx.write_event_to_stream(
            ProgressEvent(progress="I am doing something!")
        )

        return StopEvent(result=result)


async def main():
    await deploy_workflow(
        workflow=MyWorkflow(),
        workflow_config=WorkflowServiceConfig(
            host="127.0.0.1", port=8002, service_name="my_workflow"
        ),
        control_plane_config=ControlPlaneConfig(),
    )


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

This will deploy your workflow as a service and register it with the existing control plane and message queue.

### Interacting with your Deployment#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/30_manual_orchestration/#interacting-with-your-deployment)

Once deployed, you can interact with your deployment using a client.

```
from llama_deploy import LlamaDeployClient, ControlPlaneConfig

# points to deployed control plane
client = LlamaDeployClient(ControlPlaneConfig())

session = client.create_session()
result = session.run("my_workflow", arg1="hello_world")
print(result)
# prints 'hello_world_result'
```

```
from llama_deploy import LlamaDeployClient, ControlPlaneConfig

# points to deployed control plane
client = LlamaDeployClient(ControlPlaneConfig())

session = client.create_session()
result = session.run("my_workflow", arg1="hello_world")
print(result)
# prints 'hello_world_result'
```

If you want to see the event stream as well, you can do:

```
# create a session
session = client.create_session()

# kick off run
task_id = session.run_nowait("streaming_workflow", arg1="hello_world")

# stream events -- the will yield a dict representing each event
for event in session.get_task_result_stream(task_id):
    print(event)

# get final result
result = session.get_task_result(task_id)
print(result)
# prints 'hello_world_result'
```

```
# create a session
session = client.create_session()

# kick off run
task_id = session.run_nowait("streaming_workflow", arg1="hello_world")

# stream events -- the will yield a dict representing each event
for event in session.get_task_result_stream(task_id):
    print(event)

# get final result
result = session.get_task_result(task_id)
print(result)
# prints 'hello_world_result'
```

### Deploying Nested Workflows#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/30_manual_orchestration/#deploying-nested-workflows)

Every Workflow is capable of injecting and running nested workflows. For example

```
Workflow
```

```
from llama_index.core.workflow import Workflow, StartEvent, StopEvent, step


class InnerWorkflow(Workflow):
    @step()
    async def run_step(self, ev: StartEvent) -> StopEvent:
        arg1 = ev.get("arg1")
        if not arg1:
            raise ValueError("arg1 is required.")

        return StopEvent(result=str(arg1) + "_result")


class OuterWorkflow(Workflow):
    @step()
    async def run_step(
        self, ev: StartEvent, inner: InnerWorkflow
    ) -> StopEvent:
        arg1 = ev.get("arg1")
        if not arg1:
            raise ValueError("arg1 is required.")

        arg1 = await inner.run(arg1=arg1)

        return StopEvent(result=str(arg1) + "_result")


inner = InnerWorkflow()
outer = OuterWorkflow()
outer.add_workflows(inner=InnerWorkflow())
```

```
from llama_index.core.workflow import Workflow, StartEvent, StopEvent, step


class InnerWorkflow(Workflow):
    @step()
    async def run_step(self, ev: StartEvent) -> StopEvent:
        arg1 = ev.get("arg1")
        if not arg1:
            raise ValueError("arg1 is required.")

        return StopEvent(result=str(arg1) + "_result")


class OuterWorkflow(Workflow):
    @step()
    async def run_step(
        self, ev: StartEvent, inner: InnerWorkflow
    ) -> StopEvent:
        arg1 = ev.get("arg1")
        if not arg1:
            raise ValueError("arg1 is required.")

        arg1 = await inner.run(arg1=arg1)

        return StopEvent(result=str(arg1) + "_result")


inner = InnerWorkflow()
outer = OuterWorkflow()
outer.add_workflows(inner=InnerWorkflow())
```

Llama Deploy makes it dead simple to spin up each workflow above as a service, and run everything without any changes
to your code!

Just deploy each workflow:

Note

This code is launching both workflows from the same script, but these could easily be separate scripts, machines,
or docker containers!

```
import asyncio
from llama_deploy import (
    WorkflowServiceConfig,
    ControlPlaneConfig,
    deploy_workflow,
)


async def main():
    inner_task = asyncio.create_task(
        deploy_workflow(
            inner,
            WorkflowServiceConfig(
                host="127.0.0.1", port=8003, service_name="inner"
            ),
            ControlPlaneConfig(),
        )
    )

    outer_task = asyncio.create_task(
        deploy_workflow(
            outer,
            WorkflowServiceConfig(
                host="127.0.0.1", port=8002, service_name="outer"
            ),
            ControlPlaneConfig(),
        )
    )

    await asyncio.gather(inner_task, outer_task)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

```
import asyncio
from llama_deploy import (
    WorkflowServiceConfig,
    ControlPlaneConfig,
    deploy_workflow,
)


async def main():
    inner_task = asyncio.create_task(
        deploy_workflow(
            inner,
            WorkflowServiceConfig(
                host="127.0.0.1", port=8003, service_name="inner"
            ),
            ControlPlaneConfig(),
        )
    )

    outer_task = asyncio.create_task(
        deploy_workflow(
            outer,
            WorkflowServiceConfig(
                host="127.0.0.1", port=8002, service_name="outer"
            ),
            ControlPlaneConfig(),
        )
    )

    await asyncio.gather(inner_task, outer_task)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

And then use it as before:

```
from llama_deploy import LlamaDeployClient

# points to deployed control plane
client = LlamaDeployClient(ControlPlaneConfig())

session = client.create_session()
result = session.run("outer", arg1="hello_world")
print(result)
# prints 'hello_world_result_result'
```

```
from llama_deploy import LlamaDeployClient

# points to deployed control plane
client = LlamaDeployClient(ControlPlaneConfig())

session = client.create_session()
result = session.run("outer", arg1="hello_world")
print(result)
# prints 'hello_world_result_result'
```

## Manual orchestration using the lower level Python API#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/30_manual_orchestration/#manual-orchestration-using-the-lower-level-python-api)

For more control over the deployment process, you can use the lower-level API. In this section we'll see what happens
under the hood when you use wrappers like deploy_core and deploy_workflow that we saw in the previous section.

```
deploy_core
```

```
deploy_workflow
```

### deploy_core#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/30_manual_orchestration/#deploy_core)

The deploy_core function sets up the message queue, control plane, and orchestrator. Here's what it does:

```
deploy_core
```

```
async def deploy_core(
    control_plane_config: ControlPlaneConfig,
    message_queue_config: BaseSettings,
    orchestrator_config: Optional[SimpleOrchestratorConfig] = None,
) -> None:
    orchestrator_config = orchestrator_config or SimpleOrchestratorConfig()

    message_queue_client = _get_message_queue_client(message_queue_config)

    control_plane = ControlPlaneServer(
        message_queue_client,
        SimpleOrchestrator(**orchestrator_config.model_dump()),
        **control_plane_config.model_dump(),
    )

    message_queue_task = None
    if isinstance(message_queue_config, SimpleMessageQueueConfig):
        message_queue_task = _deploy_local_message_queue(message_queue_config)

    control_plane_task = asyncio.create_task(control_plane.launch_server())

    # let services spin up
    await asyncio.sleep(1)

    # register the control plane as a consumer
    control_plane_consumer_fn = await control_plane.register_to_message_queue()

    consumer_task = asyncio.create_task(control_plane_consumer_fn())

    # let things sync up
    await asyncio.sleep(1)

    # let things run
    if message_queue_task:
        all_tasks = [control_plane_task, consumer_task, message_queue_task]
    else:
        all_tasks = [control_plane_task, consumer_task]

    shutdown_handler = _get_shutdown_handler(all_tasks)
    loop = asyncio.get_event_loop()
    while loop.is_running():
        await asyncio.sleep(0.1)
        signal.signal(signal.SIGINT, shutdown_handler)

        for task in all_tasks:
            if task.done() and task.exception():  # type: ignore
                raise task.exception()  # type: ignore
```

```
async def deploy_core(
    control_plane_config: ControlPlaneConfig,
    message_queue_config: BaseSettings,
    orchestrator_config: Optional[SimpleOrchestratorConfig] = None,
) -> None:
    orchestrator_config = orchestrator_config or SimpleOrchestratorConfig()

    message_queue_client = _get_message_queue_client(message_queue_config)

    control_plane = ControlPlaneServer(
        message_queue_client,
        SimpleOrchestrator(**orchestrator_config.model_dump()),
        **control_plane_config.model_dump(),
    )

    message_queue_task = None
    if isinstance(message_queue_config, SimpleMessageQueueConfig):
        message_queue_task = _deploy_local_message_queue(message_queue_config)

    control_plane_task = asyncio.create_task(control_plane.launch_server())

    # let services spin up
    await asyncio.sleep(1)

    # register the control plane as a consumer
    control_plane_consumer_fn = await control_plane.register_to_message_queue()

    consumer_task = asyncio.create_task(control_plane_consumer_fn())

    # let things sync up
    await asyncio.sleep(1)

    # let things run
    if message_queue_task:
        all_tasks = [control_plane_task, consumer_task, message_queue_task]
    else:
        all_tasks = [control_plane_task, consumer_task]

    shutdown_handler = _get_shutdown_handler(all_tasks)
    loop = asyncio.get_event_loop()
    while loop.is_running():
        await asyncio.sleep(0.1)
        signal.signal(signal.SIGINT, shutdown_handler)

        for task in all_tasks:
            if task.done() and task.exception():  # type: ignore
                raise task.exception()  # type: ignore
```

This function:

1. Sets up the message queue client
1. Creates the control plane server
1. Launches the message queue (if using SimpleMessageQueue)
1. Launches the control plane server
1. Registers the control plane as a consumer
1. Sets up a shutdown handler and keeps the event loop running
### deploy_workflow#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/30_manual_orchestration/#deploy_workflow)

The deploy_workflow function deploys a workflow as a service. Here's what it does:

```
deploy_workflow
```

```
async def deploy_workflow(
    workflow: Workflow,
    workflow_config: WorkflowServiceConfig,
    control_plane_config: ControlPlaneConfig,
) -> None:
    control_plane_url = control_plane_config.url

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{control_plane_url}/queue_config")
        queue_config_dict = response.json()

    message_queue_config = _get_message_queue_config(queue_config_dict)
    message_queue_client = _get_message_queue_client(message_queue_config)

    service = WorkflowService(
        workflow=workflow,
        message_queue=message_queue_client,
        **workflow_config.model_dump(),
    )

    service_task = asyncio.create_task(service.launch_server())

    # let service spin up
    await asyncio.sleep(1)

    # register to message queue
    consumer_fn = await service.register_to_message_queue()

    # register to control plane
    control_plane_url = (
        f"http://{control_plane_config.host}:{control_plane_config.port}"
    )
    await service.register_to_control_plane(control_plane_url)

    # create consumer task
    consumer_task = asyncio.create_task(consumer_fn())

    # let things sync up
    await asyncio.sleep(1)

    all_tasks = [consumer_task, service_task]

    shutdown_handler = _get_shutdown_handler(all_tasks)
    loop = asyncio.get_event_loop()
    while loop.is_running():
        await asyncio.sleep(0.1)
        signal.signal(signal.SIGINT, shutdown_handler)

        for task in all_tasks:
            if task.done() and task.exception():  # type: ignore
                raise task.exception()  # type: ignore
```

```
async def deploy_workflow(
    workflow: Workflow,
    workflow_config: WorkflowServiceConfig,
    control_plane_config: ControlPlaneConfig,
) -> None:
    control_plane_url = control_plane_config.url

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{control_plane_url}/queue_config")
        queue_config_dict = response.json()

    message_queue_config = _get_message_queue_config(queue_config_dict)
    message_queue_client = _get_message_queue_client(message_queue_config)

    service = WorkflowService(
        workflow=workflow,
        message_queue=message_queue_client,
        **workflow_config.model_dump(),
    )

    service_task = asyncio.create_task(service.launch_server())

    # let service spin up
    await asyncio.sleep(1)

    # register to message queue
    consumer_fn = await service.register_to_message_queue()

    # register to control plane
    control_plane_url = (
        f"http://{control_plane_config.host}:{control_plane_config.port}"
    )
    await service.register_to_control_plane(control_plane_url)

    # create consumer task
    consumer_task = asyncio.create_task(consumer_fn())

    # let things sync up
    await asyncio.sleep(1)

    all_tasks = [consumer_task, service_task]

    shutdown_handler = _get_shutdown_handler(all_tasks)
    loop = asyncio.get_event_loop()
    while loop.is_running():
        await asyncio.sleep(0.1)
        signal.signal(signal.SIGINT, shutdown_handler)

        for task in all_tasks:
            if task.done() and task.exception():  # type: ignore
                raise task.exception()  # type: ignore
```

This function:

1. Sets up the message queue client
1. Creates a WorkflowService with the provided workflow
1. Launches the service server
1. Registers the service to the message queue
1. Registers the service to the control plane
1. Sets up a consumer task for the service
1. Sets up a shutdown handler and keeps the event loop running
