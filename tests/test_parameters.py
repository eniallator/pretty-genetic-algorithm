from pretty_genetic_algorithm.parameter import RangeParameter
from pretty_genetic_algorithm.parameter import BaseParameter


def test_range():
    expected_values = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5]
    param = RangeParameter(0.0, 3.0, 0.5, "_")
    assert param.values == expected_values


def test_label_and_alias():
    param = BaseParameter([], "foo", "bar")
    assert param.alias == "foo"
    assert param.label == "bar"
