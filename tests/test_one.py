from tests.conftest import get_real_asteroids_count, get_hazardous_asteroids, get_kilometer_diameter, \
                           get_name_all_asteroids


def test_name(start):
    name = get_name_all_asteroids(start)
    print(name)


def test_count_asteroids(start):
    count_asteroids = start["contextWrites"]["to"]["element_count"]
    all_asteroid = get_real_asteroids_count(start)
    assert all_asteroid == count_asteroids


def test_not_hazardous_asteroid(start):
    hazardous_asteroids = get_hazardous_asteroids(start)
    assert True in hazardous_asteroids


def test_diameter_asteroid(start):
    assert get_kilometer_diameter(start) is True
