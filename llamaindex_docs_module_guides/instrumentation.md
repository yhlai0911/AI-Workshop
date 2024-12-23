# Instrumentation#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/observability/instrumentation/

# Instrumentation#

[#](https://docs.llamaindex.ai/en/stable/module_guides/observability/instrumentation/#instrumentation)

NOTE: The instrumentation module (available in llama-index v0.10.20 and later) is
meant to replace the legacy callbacks module. During the deprecation period,
the llama-index library supports both modules as a means to instrument your
LLM application. However, at some point after all of the existing integrations
have moved over to the new instrumentation module, we will no longer support
callbacks module.

```
instrumentation
```

```
callbacks
```

```
instrumentation
```

```
callbacks
```

The new instrumentation module allows for the instrumentation of llama-index
applications. In particular, one can handle events and track spans using both
custom logic as well as those offered in the module. Users can also define their
own events and specify where and when in the code logic that they should be emitted.
Listed below are the core classes as well as their brief description of the
instrumentation module:

```
instrumentation
```

```
llama-index
```

```
instrumentation
```

- Event — represents a single moment in time that a certain occurrence took place within the execution of the application’s code.
```
Event
```

- EventHandler — listen to the occurrences of Event's and execute code logic at these moments in time.
```
EventHandler
```

```
Event
```

- Span — represents the execution flow of a particular part in the application’s code and thus contains Event's.
```
Span
```

```
Event
```

- SpanHandler — is responsible for the entering, exiting, and dropping (i.e., early exiting due to error) of Span's.
```
SpanHandler
```

```
Span
```

- Dispatcher — emits Event's as well as signals to enter/exit/drop a Span to the appropriate handlers.
```
Dispatcher
```

```
Event
```

```
Span
```

## Using the Instrumentation Module for Observability#

[#](https://docs.llamaindex.ai/en/stable/module_guides/observability/instrumentation/#using-the-instrumentation-module-for-observability)

A core use case for instrumentation is observability. Our native instrumentation integrations with third-party partners allow you to get detailed traces across the entire call stack.

Check out our [observability guide](https://docs.llamaindex.ai/en/stable/module_guides/observability/) for more details on supported partners.

## Usage#

[#](https://docs.llamaindex.ai/en/stable/module_guides/observability/instrumentation/#usage)

Using the new instrumentation module involves 3 high-level steps.

```
instrumentation
```

1. Define a dispatcher
```
dispatcher
```

1. (Optional) Define and attach your EventHandler's to dispatcher
```
EventHandler
```

```
dispatcher
```

1. (Optional) Define and attach your SpanHandler to dispatcher
```
SpanHandler
```

```
dispatcher
```

Doing so, would result in the ability to handle events and obtain spans that have
been transmitted throughout the llama-index library and extension packages.

```
llama-index
```

For example, if I wanted to track every LLM call made in the library:

```
from typing import Dict, List

from llama_index.core.instrumentation.events.llm import (
    LLMChatEndEvent,
    LLMChatStartEvent,
    LLMChatInProgressEvent,
)


class ExampleEventHandler(BaseEventHandler):
    events: List[BaseEvent] = []

    @classmethod
    def class_name(cls) -> str:
        """Class name."""
        return "ExampleEventHandler"

    def handle(self, event: BaseEvent) -> None:
        """Logic for handling event."""
        print("-----------------------")
        # all events have these attributes
        print(event.id_)
        print(event.timestamp)
        print(event.span_id)

        # event specific attributes
        if isinstance(event, LLMChatStartEvent):
            # initial
            print(event.messages)
            print(event.additional_kwargs)
            print(event.model_dict)
        elif isinstance(event, LLMChatInProgressEvent):
            # streaming
            print(event.response.delta)
        elif isinstance(event, LLMChatEndEvent):
            # final response
            print(event.response)

        self.events.append(event)
        print("-----------------------")
```

```
from typing import Dict, List

from llama_index.core.instrumentation.events.llm import (
    LLMChatEndEvent,
    LLMChatStartEvent,
    LLMChatInProgressEvent,
)


class ExampleEventHandler(BaseEventHandler):
    events: List[BaseEvent] = []

    @classmethod
    def class_name(cls) -> str:
        """Class name."""
        return "ExampleEventHandler"

    def handle(self, event: BaseEvent) -> None:
        """Logic for handling event."""
        print("-----------------------")
        # all events have these attributes
        print(event.id_)
        print(event.timestamp)
        print(event.span_id)

        # event specific attributes
        if isinstance(event, LLMChatStartEvent):
            # initial
            print(event.messages)
            print(event.additional_kwargs)
            print(event.model_dict)
        elif isinstance(event, LLMChatInProgressEvent):
            # streaming
            print(event.response.delta)
        elif isinstance(event, LLMChatEndEvent):
            # final response
            print(event.response)

        self.events.append(event)
        print("-----------------------")
```

See the [full guide](https://docs.llamaindex.ai/en/stable/examples/instrumentation/instrumentation_observability_rundown/) on all events logged in LlamaIndex, or visit the [api reference](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/) for more details.

### Defining a custom EventHandler#

```
EventHandler
```

[#](https://docs.llamaindex.ai/en/stable/module_guides/observability/instrumentation/#defining-a-custom-eventhandler)

Users can create their own custom handlers by subclassing BaseEventHandler
and providing logic to the abstract method handle().

```
BaseEventHandler
```

```
handle()
```

```
from llama_index.core.instrumentation.event_handlers.base import (
    BaseEventHandler,
)


class MyEventHandler(BaseEventHandler):
    """My custom EventHandler."""

    @classmethod
    def class_name(cls) -> str:
        """Class name."""
        return "MyEventHandler"

    def handle(self, event: BaseEvent, **kwargs) -> Any:
        """Logic for handling event."""
        print(event.class_name())


my_event_handler = MyEventHandler()
```

```
from llama_index.core.instrumentation.event_handlers.base import (
    BaseEventHandler,
)


class MyEventHandler(BaseEventHandler):
    """My custom EventHandler."""

    @classmethod
    def class_name(cls) -> str:
        """Class name."""
        return "MyEventHandler"

    def handle(self, event: BaseEvent, **kwargs) -> Any:
        """Logic for handling event."""
        print(event.class_name())


my_event_handler = MyEventHandler()
```

After defining your handler, you can attach it to the desired dispatcher:

```
import llama_index.core.instrumentation as instrument

dispatcher = instrument.get_dispatcher(__name__)
dispatcher.add_event_handler(my_event_handler)
```

```
import llama_index.core.instrumentation as instrument

dispatcher = instrument.get_dispatcher(__name__)
dispatcher.add_event_handler(my_event_handler)
```

### Defining a custom Event#

```
Event
```

[#](https://docs.llamaindex.ai/en/stable/module_guides/observability/instrumentation/#defining-a-custom-event)

User can create their own custom events by subclassing BaseEvent. The
BaseEvent class comes with a timestamp as well as an id_ field. To add more
items to this event payload, simply add them in as new Fields (since they are
subclasses of pydantic.BaseModel).

```
BaseEvent
```

```
BaseEvent
```

```
timestamp
```

```
id_
```

```
Fields
```

```
pydantic.BaseModel
```

```
from llama_index.core.instrumentation.event.base import BaseEvent


class MyEvent(BaseEvent):
    """My custom Event."""

    new_field_1 = Field(...)
    new_field_2 = Field(...)
```

```
from llama_index.core.instrumentation.event.base import BaseEvent


class MyEvent(BaseEvent):
    """My custom Event."""

    new_field_1 = Field(...)
    new_field_2 = Field(...)
```

Once you have your custom event defined, you use a dispatcher to fire the event
at desired instances throughout your application’s code.

```
import llama_index.core.instrumentation as instrument

dispatcher = instrument.get_dispatcher(__name__)
dispatcher.event(MyEvent(new_field_1=..., new_field_2=...))
```

```
import llama_index.core.instrumentation as instrument

dispatcher = instrument.get_dispatcher(__name__)
dispatcher.event(MyEvent(new_field_1=..., new_field_2=...))
```

### Defining a custom Span#

```
Span
```

[#](https://docs.llamaindex.ai/en/stable/module_guides/observability/instrumentation/#defining-a-custom-span)

Span’s are like Event's in that they are both structured data classes.
Unlike Event's though, Span's as their name implies, span a duration of time
within the programs execution flow. You can define a custom Span to store any
information you would like.

```
Span
```

```
Event
```

```
Event
```

```
Span
```

```
Span
```

```
from typing import Any
from llama_index.core.bridge.pydantic import Field


class MyCustomSpan(BaseSpan):
    custom_field_1: Any = Field(...)
    custom_field_2: Any = Field(...)
```

```
from typing import Any
from llama_index.core.bridge.pydantic import Field


class MyCustomSpan(BaseSpan):
    custom_field_1: Any = Field(...)
    custom_field_2: Any = Field(...)
```

To handle your new Span type, you need to also define your custom SpanHandler
by subclassing the BaseSpanHandler class. Three abstract methods need to be
defined when subclass this base class, namely: new_span(), prepare_to_exit_span(),
and prepare_to_drop_span().

```
SpanHandler
```

```
BaseSpanHandler
```

```
new_span()
```

```
prepare_to_exit_span()
```

```
prepare_to_drop_span()
```

```
import inspect
from typing import Any, Dict, Optional
from llama_index.core.instrumentation.span.base import BaseSpan
from llama_index.core.instrumentation.span_handlers import BaseSpanHandler


class MyCustomSpanHandler(BaseSpanHandler[MyCustomSpan]):
    @classmethod
    def class_name(cls) -> str:
        """Class name."""
        return "MyCustomSpanHandler"

    def new_span(
        self,
        id_: str,
        bound_args: inspect.BoundArguments,
        instance: Optional[Any] = None,
        parent_span_id: Optional[str] = None,
        tags: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Optional[MyCustomSpan]:
        """Create a span."""
        # logic for creating a new MyCustomSpan
        pass

    def prepare_to_exit_span(
        self,
        id_: str,
        bound_args: inspect.BoundArguments,
        instance: Optional[Any] = None,
        result: Optional[Any] = None,
        **kwargs: Any,
    ) -> Any:
        """Logic for preparing to exit a span."""
        pass

    def prepare_to_drop_span(
        self,
        id_: str,
        bound_args: inspect.BoundArguments,
        instance: Optional[Any] = None,
        err: Optional[BaseException] = None,
        **kwargs: Any,
    ) -> Any:
        """Logic for preparing to drop a span."""
        pass
```

```
import inspect
from typing import Any, Dict, Optional
from llama_index.core.instrumentation.span.base import BaseSpan
from llama_index.core.instrumentation.span_handlers import BaseSpanHandler


class MyCustomSpanHandler(BaseSpanHandler[MyCustomSpan]):
    @classmethod
    def class_name(cls) -> str:
        """Class name."""
        return "MyCustomSpanHandler"

    def new_span(
        self,
        id_: str,
        bound_args: inspect.BoundArguments,
        instance: Optional[Any] = None,
        parent_span_id: Optional[str] = None,
        tags: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Optional[MyCustomSpan]:
        """Create a span."""
        # logic for creating a new MyCustomSpan
        pass

    def prepare_to_exit_span(
        self,
        id_: str,
        bound_args: inspect.BoundArguments,
        instance: Optional[Any] = None,
        result: Optional[Any] = None,
        **kwargs: Any,
    ) -> Any:
        """Logic for preparing to exit a span."""
        pass

    def prepare_to_drop_span(
        self,
        id_: str,
        bound_args: inspect.BoundArguments,
        instance: Optional[Any] = None,
        err: Optional[BaseException] = None,
        **kwargs: Any,
    ) -> Any:
        """Logic for preparing to drop a span."""
        pass
```

To make use of your new SpanHandler (and associated Span type), you simply need
to add it to your desired dispatcher.

```
import llama_index.core.instrumentation as instrument
from llama_index.core.instrumentation.span_handler import SimpleSpanHandler

dispatcher = (
    instrument.get_dispatcher()
)  # with no name argument, defaults to root

my_span_handler = MyCustomSpanHandler()
dispatcher.add_span_handler(my_span_handler)
```

```
import llama_index.core.instrumentation as instrument
from llama_index.core.instrumentation.span_handler import SimpleSpanHandler

dispatcher = (
    instrument.get_dispatcher()
)  # with no name argument, defaults to root

my_span_handler = MyCustomSpanHandler()
dispatcher.add_span_handler(my_span_handler)
```

### Entering/Exiting a Span#

```
Span
```

[#](https://docs.llamaindex.ai/en/stable/module_guides/observability/instrumentation/#enteringexiting-a-span)

To send a signal to SpanHandler's to enter/exit a Span, we use the span_enter(),
span_exit() methods, respectively. There is also span_drop() method that could
be used to handle cases where Span's are cut shorter than usual due to errors
within the covered code’s execution.

```
SpanHandler
```

```
Span
```

```
span_enter()
```

```
span_exit()
```

```
span_drop()
```

```
Span
```

```
import llama_index.core.instrumentation as instrument

dispatcher = instrument.get_dispatcher(__name__)


def func():
    dispatcher.span_enter(...)
    try:
        val = ...
    except:
        ...
        dispatcher.span_drop(...)
    else:
        dispatcher.span_exit(...)
        return val


# or, syntactic sugar via decorators


@dispatcher.span
def func():
    ...
```

```
import llama_index.core.instrumentation as instrument

dispatcher = instrument.get_dispatcher(__name__)


def func():
    dispatcher.span_enter(...)
    try:
        val = ...
    except:
        ...
        dispatcher.span_drop(...)
    else:
        dispatcher.span_exit(...)
        return val


# or, syntactic sugar via decorators


@dispatcher.span
def func():
    ...
```

### Making use of dispatcher hierarchy#

```
dispatcher
```

[#](https://docs.llamaindex.ai/en/stable/module_guides/observability/instrumentation/#making-use-of-dispatcher-hierarchy)

A similar hierarchy to that seen with the standard Python logging library and
its Logger class exists for dispatcher. Specifically, all dispatcher’s
except for the root dispatcher has a parent, and when handling events or span’s
can propagate them to its parent as well (this is the default behaviour). This
hierarchical method of handling events and spans allows for defining “global”
event handlers as well as “local” ones.

```
logging
```

```
Logger
```

```
dispatcher
```

```
dispatcher
```

```
dispatcher
```

Consider the project structure defined below. There are 3 dispatcher's: one at
the top-level of the project and then two others at the individual sub-modules
llama1 and llama2. With this setup, any EventHandler’s attached to the
project root’s dispatcher will be be subscribed to all Event's that occur in
the execution of code in llama1 and llama2. On the other hand, EventHandler's
defined in the respective llama<x> sub modules will only be subscribed to the
Event's that occur within their respective sub-module execution.

```
dispatcher
```

```
project
```

```
llama1
```

```
llama2
```

```
EventHandler
```

```
dispatcher
```

```
Event
```

```
llama1
```

```
llama2
```

```
EventHandler
```

```
llama<x>
```

```
Event
```

```
project
├── __init__.py  # has a dispatcher=instrument.get_dispatcher(__name__)
├── llama1
│   ├── __init__.py  # has a dispatcher=instrument.get_dispatcher(__name__)
│   └── app_query_engine.py
└── llama2
    ├── __init__.py  # has a dispatcher=instrument.get_dispatcher(__name__)
    └── app_query_engine.py
```

```
project
├── __init__.py  # has a dispatcher=instrument.get_dispatcher(__name__)
├── llama1
│   ├── __init__.py  # has a dispatcher=instrument.get_dispatcher(__name__)
│   └── app_query_engine.py
└── llama2
    ├── __init__.py  # has a dispatcher=instrument.get_dispatcher(__name__)
    └── app_query_engine.py
```

## Notebook Guides:#

[#](https://docs.llamaindex.ai/en/stable/module_guides/observability/instrumentation/#notebook-guides)

- [Basic Usage](https://docs.llamaindex.ai/en/stable/examples/instrumentation/basic_usage/)
- [Observing Model Calls](https://docs.llamaindex.ai/en/stable/examples/instrumentation/observe_api_calls/)
- [Observing All Events](https://docs.llamaindex.ai/en/stable/examples/instrumentation/instrumentation_observability_rundown/)
## API Reference#

[#](https://docs.llamaindex.ai/en/stable/module_guides/observability/instrumentation/#api-reference)

- [Instrumentation API Reference](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/)
