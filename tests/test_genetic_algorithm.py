import pytest

from .fixtures import dna_config

from pretty_genetic_algorithm import PrettyGeneticAlgorithm
from pretty_genetic_algorithm import Creature


def test_init(dna_config):
    ga = PrettyGeneticAlgorithm(3, 5, dna_config)
    assert len(ga.species) == 3
    assert all(len(species) == 5 for species in ga.species)


def measure_fitness(c):
    target_sum = 13
    return -abs(c.a + c.b + c.c - target_sum)


def test_cache_fitness(dna_config):
    ga = PrettyGeneticAlgorithm(3, 5, dna_config, silent=True)

    times_executed = [0]

    @ga.cache_fitness
    def cached_measure_fitness(c, verbose=False):
        times_executed[0] += 1
        return measure_fitness(c)

    creature = Creature(dna_config, dna=(1, 4, 7))
    assert times_executed[0] == 0

    cached_measure_fitness(creature)
    assert times_executed[0] == 1

    cached_measure_fitness(creature)
    assert times_executed[0] == 1


def test_evolve_not_silent(dna_config):
    ga = PrettyGeneticAlgorithm(3, 5, dna_config)
    assert len(ga.evolve(2, measure_fitness)) == 2


def test_multiple_evolve(dna_config):
    ga = PrettyGeneticAlgorithm(3, 5, dna_config, silent=True)
    history = ga.evolve(2, measure_fitness)

    assert len(history) == 2
    assert all(len(all_species) == 3 for all_species in history)
    assert all(len(species) == 5 for all_species in history for species in all_species)

    history = ga.evolve(3, measure_fitness)

    assert len(history) == 5
    assert all(len(all_species) == 3 for all_species in history)
    assert all(len(species) == 5 for all_species in history for species in all_species)


def test_evolve_mating_mutation(dna_config):
    ga = PrettyGeneticAlgorithm(3, 5, dna_config, silent=True)
    assert (
        len(
            ga.evolve(2, measure_fitness, mutate=PrettyGeneticAlgorithm.mating_mutation)
        )
        == 2
    )


def test_evolve_choose_mate_simple_random(dna_config):
    ga = PrettyGeneticAlgorithm(3, 5, dna_config, silent=True)
    assert (
        len(
            ga.evolve(
                2, measure_fitness, choose_mate=PrettyGeneticAlgorithm.simple_random
            )
        )
        == 2
    )


def test_evolve_choose_mate_spatial_similarity(dna_config):
    ga = PrettyGeneticAlgorithm(3, 5, dna_config, silent=True)
    assert (
        len(
            ga.evolve(
                2,
                measure_fitness,
                choose_mate=PrettyGeneticAlgorithm.spatial_similarity,
            )
        )
        == 2
    )


def test_evolve_choose_mate_weighted_random(dna_config):
    ga = PrettyGeneticAlgorithm(3, 5, dna_config, silent=True)
    assert (
        len(
            ga.evolve(
                2,
                measure_fitness,
                choose_mate=PrettyGeneticAlgorithm.weighted_random,
                choose_mate_args=(measure_fitness,),
            )
        )
        == 2
    )


def test_evolve_choose_mate_choose_next(dna_config):
    ga = PrettyGeneticAlgorithm(3, 5, dna_config, silent=True)
    assert (
        len(
            ga.evolve(
                2,
                measure_fitness,
                choose_mate=PrettyGeneticAlgorithm.choose_next,
            )
        )
        == 2
    )


def test_best(dna_config):
    ga = PrettyGeneticAlgorithm(3, 5, dna_config, silent=True)
    history = ga.evolve(2, measure_fitness)
    assert ga.best()[0] == max(max(species) for species in history[-1])


serialised_species = "[[[0, 3, 6], [0.5, 3.5, 6.5], [1, 4, 7]], [[1.5, 4.5, 7.5], [2, 5, 8], [2.5, 5.5, 8.5]]]"
deserialised_species = lambda dna_config: [
    [
        Creature(dna_config, dna=(0, 3, 6)),
        Creature(dna_config, dna=(0.5, 3.5, 6.5)),
        Creature(dna_config, dna=(1, 4, 7)),
    ],
    [
        Creature(dna_config, dna=(1.5, 4.5, 7.5)),
        Creature(dna_config, dna=(2, 5, 8)),
        Creature(dna_config, dna=(2.5, 5.5, 8.5)),
    ],
]


def test_serialise_dna_data(dna_config):
    ga = PrettyGeneticAlgorithm(2, 3, dna_config, silent=True)
    ga.species = deserialised_species(dna_config)

    assert ga.serialise_dna_data() == serialised_species


def test_deserialise_dna_data(dna_config):
    ga = PrettyGeneticAlgorithm.deserialise_dna_data(
        serialised_species, 2, 3, dna_config, silent=True
    )
    assert ga.species == deserialised_species(dna_config)
