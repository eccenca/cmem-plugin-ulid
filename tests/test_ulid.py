"""Plugin tests."""

import pytest

from cmem_plugin_ulid.ulid import URN_PREFIX, ULIDTransformPlugin


def test_execution() -> None:
    """Test execution"""
    # default case
    assert len(ULIDTransformPlugin().transform(inputs=[])) == 1

    # multiple values
    count = 2
    assert len(ULIDTransformPlugin(number_of_values=count).transform(inputs=[])) == count
    count = 3
    assert len(ULIDTransformPlugin(number_of_values=count).transform(inputs=[])) == count

    # as urn
    result = ULIDTransformPlugin(generate_urn=True).transform(inputs=[])
    assert len(result) == 1
    for _ in result:
        assert _.startswith(URN_PREFIX)


def test_fails() -> None:
    """Test fails."""
    # no inputs allowed
    with pytest.raises(ValueError, match=r"Plugin does not support processing input entities."):
        ULIDTransformPlugin().transform(inputs=[["2000-05-22", "2021-12-12", "1904-02-29"]])

    with pytest.raises(ValueError, match=r"Number of Values needs to be a positive integer."):
        ULIDTransformPlugin(number_of_values=-0).transform(inputs=[])
    with pytest.raises(ValueError, match=r"Number of Values needs to be a positive integer."):
        ULIDTransformPlugin(number_of_values=-1).transform(inputs=[])
