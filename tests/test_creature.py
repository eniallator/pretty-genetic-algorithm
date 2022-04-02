from .fixtures import dna_config

from pretty_genetic_algorithm import Creature


def test_similarity(dna_config):
    c1 = Creature(dna_config, [1, 4, 7])
    c2 = Creature(dna_config, [2, 5, 8])
    assert c1.get_similarity(c2) == 3
