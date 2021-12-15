import pytest
from code_challenges.stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter, Cat, Dog


def test_shelter_creation():
    shelter = AnimalShelter()
    assert shelter


@pytest.fixture
def shelter_of_pets():
    shelter = AnimalShelter()
    shelter.enqueue(Cat('Garfield'))
    shelter.enqueue(Cat('Tom'))
    shelter.enqueue(Dog('Snoopy'))
    shelter.enqueue(Cat('Nala'))
    shelter.enqueue(Dog('Clifford'))
    return shelter
