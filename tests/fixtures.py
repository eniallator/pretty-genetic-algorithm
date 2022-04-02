import pytest

from pretty_genetic_algorithm.parameter.RangeParameter import RangeParameter


@pytest.fixture
def dna_config():
    return [
        RangeParameter(0.0, 3.0, 0.5, "a", "A"),
        RangeParameter(3.0, 6.0, 0.5, "b", "B"),
        RangeParameter(6.0, 9.0, 0.5, "c", "C"),
    ]
