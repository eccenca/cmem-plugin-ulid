"""lifetime(age) transform plugin module"""
from typing import Sequence

from cmem_plugin_base.dataintegration.description import (
    Plugin, PluginParameter,
)
from cmem_plugin_base.dataintegration.plugins import TransformPlugin
from cmem_plugin_base.dataintegration.types import IntParameterType
from ulid import ULID


@Plugin(
    label="ULID",
    plugin_id="cmem-plugin-ulid",
    description="Generate a ULID from a random number, and the current time.",
    documentation="""
This ulid transform operator generates random lexicographically sortable ulid.

Generates random ULID, based on length of inputs, if their are no inputs.
then it will generate one ULID.

""",
    parameters=[
        PluginParameter(
            name="number_of_values",
            label="Number of Values",
            description="The number of ULIDs to generate.",
            default_value=1,
            param_type=IntParameterType()
        ),

    ],
)
class ULIDTransformPlugin(TransformPlugin):
    """ULID Transform Plugin"""

    def __init__(self, number_of_values=1):
        if number_of_values < 1:
            raise ValueError("Number of Values needs to be a positive integer.")

        self.number_of_values = number_of_values

    def transform(self, inputs: Sequence[Sequence[str]]) -> Sequence[str]:
        result = []
        for _ in range(self.number_of_values):
            result += [f"{ULID()}"]
        return result
