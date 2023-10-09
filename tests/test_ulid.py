"""Plugin tests."""

from cmem_plugin_ulid.transform import ULIDTransformPlugin


def test_transform_execution_with_optional_input():
    """Test Lifetime with optional input"""
    result = ULIDTransformPlugin().transform(inputs=[])
    assert len(result) == 1


def test_transform_execution_with_inputs():
    """Test Lifetime with sequence of inputs."""
    result = ULIDTransformPlugin().transform(
        inputs=[["2000-05-22", "2021-12-12", "1904-02-29"]]
    )
    assert len(result) == 3
