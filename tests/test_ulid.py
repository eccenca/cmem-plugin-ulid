"""Plugin tests."""
import pytest

from cmem_plugin_ulid.transform import ULIDTransformPlugin, URN_PREFIX


def test_execution():
    """Test execution"""
    # default case
    assert len(ULIDTransformPlugin().transform(inputs=[])) == 1

    # multiple values
    assert len(ULIDTransformPlugin(number_of_values=2).transform(inputs=[])) == 2
    assert len(ULIDTransformPlugin(number_of_values=3).transform(inputs=[])) == 3

    # as urn
    result = ULIDTransformPlugin(generate_urn=True).transform(inputs=[])
    assert len(result) == 1
    for _ in result:
        assert _.startswith(URN_PREFIX)


def test_fails():
    """Test fails."""
    # no inputs allowed
    with pytest.raises(ValueError):
        ULIDTransformPlugin().transform(
            inputs=[["2000-05-22", "2021-12-12", "1904-02-29"]]
        )

    with pytest.raises(ValueError):
        ULIDTransformPlugin(number_of_values=-0).transform(inputs=[])
    with pytest.raises(ValueError):
        ULIDTransformPlugin(number_of_values=-1).transform(inputs=[])
