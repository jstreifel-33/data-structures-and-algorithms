import pytest
from code_challenges.stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter, Cat, Dog


def test_shelter_creation():
    shelter = AnimalShelter()
    assert shelter


def test_getting_cat(shelter_of_pets):
    animal = shelter_of_pets.dequeue('cat')

    assert isinstance(animal, Cat)
    assert animal.value == 'Garfield'


def test_getting_dog(shelter_of_pets):
    animal = shelter_of_pets.dequeue('dog')

    assert isinstance(animal, Dog)
    assert animal.value == 'Snoopy'


def test_preservation_of_queue(shelter_of_pets):
    shelter_of_pets.dequeue('cat')
    shelter_of_pets.dequeue('dog')
    animal = shelter_of_pets.dequeue('cat')

    assert isinstance(animal, Cat)
    assert animal.value == 'Tom'


def test_no_match_result(shelter_of_pets):
    animal = shelter_of_pets.dequeue('lizard')

    assert animal is None


def test_animal_shelter_empty():
    shelter = AnimalShelter()
    with pytest.raises(Exception) as e:
        shelter.dequeue('cat')

    assert str(e.value) == 'Animal Shelter is empty!'


@pytest.fixture
def shelter_of_pets():
    shelter = AnimalShelter()
    shelter.enqueue(Cat('Garfield'))
    shelter.enqueue(Cat('Tom'))
    shelter.enqueue(Dog('Snoopy'))
    shelter.enqueue(Cat('Nala'))
    shelter.enqueue(Dog('Clifford'))
    return shelter
