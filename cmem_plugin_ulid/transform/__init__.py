"""lifetime(age) transform plugin module"""
from typing import Sequence

from cmem_plugin_base.dataintegration.description import (
    Plugin,
)
from cmem_plugin_base.dataintegration.plugins import TransformPlugin
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
    ],
)
class ULIDTransformPlugin(TransformPlugin):
    """ULID Transform Plugin"""

    def transform(self, inputs: Sequence[Sequence[str]]) -> Sequence[str]:
        result = []
        if len(inputs) != 0:
            for collection in inputs:
                result += [f"{ULID()}" for _ in collection]
        if len(result) == 0:
            result += [f"{ULID()}"]
        return result
