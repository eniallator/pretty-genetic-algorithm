import pytest
from pretty_genetic_algorithm.Creature import Creature
from pretty_genetic_algorithm.parameter.RangeParameter import RangeParameter


@pytest.fixture
def range_param():
    return RangeParameter(0.0, 3.0, 0.5, "range", "Range")


@pytest.fixture
def dna_config():
    return [
        RangeParameter(0.0, 3.0, 0.5, "a", "A"),
        RangeParameter(3.0, 6.0, 0.5, "b", "B"),
        RangeParameter(6.0, 9.0, 0.5, "c", "C"),
    ]


def test_similarity(dna_config):
    c1 = Creature(dna_config, [1, 4, 7])
    c2 = Creature(dna_config, [2, 5, 8])
    return c1.get_similarity(c2) == 3
