# Copyright 2025 Amazon Inc

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import dataclasses

from nova_act.types.act_metadata import ActMetadata
from nova_act.types.errors import NovaActError


# Decorator for allowing optional messages to override the default messages while keeping metadata mandatory
def act_error_class(default_message: str):
    def decorator(cls):
        @dataclasses.dataclass(frozen=True, repr=False)
        class wrapped(ActError):
            _DEFAULT_MESSAGE = default_message

            def __init__(self, *, metadata: ActMetadata, message: str | None = None):
                super().__init__(metadata=metadata, message=message)
                wrapped.__name__ = cls.__name__

        wrapped.__qualname__ = cls.__qualname__
        return wrapped

    return decorator


"""
Base class for all Errors Occurring during act()
"""


@dataclasses.dataclass(frozen=True, repr=False)
class ActError(NovaActError):
    metadata: ActMetadata
    message: str = dataclasses.field(init=False)
    _DEFAULT_MESSAGE = "An error occurred during act()"

    def __init__(self, *, metadata: ActMetadata, message: str | None = None):
        final_message = message or self.__class__._DEFAULT_MESSAGE
        super().__init__(final_message)
        object.__setattr__(self, "metadata", metadata)
        object.__setattr__(self, "message", final_message)

    def __str__(self) -> str:
        # Format metadata string with indentation
        metadata_str = str(self.metadata).replace("\n", "\n    ")
        return (
            f"\n\n{self.__class__.__name__}(\n"
            f"    message = {self.message}\n"
            f"    metadata = {metadata_str}\n"
            f")"
            "\n\nPlease consider providing feedback: "
            "https://amazonexteu.qualtrics.com/jfe/form/SV_bd8dHa7Em6kNkMe"
        )


"""
Concrete Errors
"""


@act_error_class("The requested action was not possible")
class ActAgentError(ActError):
    pass


@act_error_class("I'm sorry, but I can't engage in unsafe or inappropriate actions. Please try a different request.")
class ActGuardrailsError(ActError):
    pass


@act_error_class("Timed out, you can modify the 'timeout' kwarg on the 'act' call")
class ActTimeoutError(ActError):
    pass


@act_error_class("Allowed Steps Exceeded")
class ActExceededMaxStepsError(ActError):
    pass


@act_error_class("Act Canceled")
class ActCanceledError(ActError):
    pass


@act_error_class("Failed to dispatch act")
class ActDispatchError(ActError):
    pass


@act_error_class("Internal Server Error")
class ActInternalServerError(ActError):
    pass


@act_error_class("Server Unavailable")
class ActServiceUnavailableError(ActError):
    pass


@act_error_class("NovaAct Client Error")
class ActClientError(ActError):
    pass


@act_error_class("Rate Limit Error")
class ActRateLimitExceededError(ActError):
    pass


@act_error_class("Failed to parse response")
class ActProtocolError(ActError):
    pass
