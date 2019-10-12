import requests
import pytest
from tests.utils import all_dates
from tests.constants import URL, PAYLOAD, HEADERS

@pytest.fixture(scope="module")
def start(request):
    response = requests.request("POST", URL, data=PAYLOAD, headers=HEADERS).json()
    return response


def get_name_all_asteroids(start):
    days = all_dates()
    names = []
    for day in days:
        week = start["contextWrites"]["to"]["near_earth_objects"][day]
        for i in range(0, len(week)):
            name = start["contextWrites"]["to"]["near_earth_objects"][day][i]["name"]
            names.append(name)
    return names


def get_real_asteroids_count(start):
    real_count_asteroid = []
    days = all_dates()
    for day in days:
        real_count_asteroid_week = start["contextWrites"]["to"]["near_earth_objects"][day]
        real_count_asteroid.append(len(real_count_asteroid_week))
    count = sum(real_count_asteroid)
    return count


def get_hazardous_asteroids(start):
    days = all_dates()
    hazardous = []
    for day in days:
        week = start["contextWrites"]["to"]["near_earth_objects"][day]
        for i in range(0, len(week)):
            hazardous_p = start["contextWrites"]["to"]["near_earth_objects"][day][i][
                "is_potentially_hazardous_asteroid"]
            hazardous.append(hazardous_p)
    return hazardous


def get_kilometer_diameter(start):
    days = all_dates()
    for day in days:
        week = start["contextWrites"]["to"]["near_earth_objects"][day]
        for i in range(0, len(week)):
            diameter = start["contextWrites"]["to"]["near_earth_objects"][day][i]["estimated_diameter"]["kilometers"]["estimated_diameter_max"]
            if diameter > 1:
                return True
