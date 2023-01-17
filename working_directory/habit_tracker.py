"""
Author: Saba Konjaria
Created at: 18-Jan-2023
---------------------------------- Brief Description

    This program Does some basic manipulations to API. such as writing, deleting and creating
along with API call directly from Python. This is an example, how we can Track over the
habits, Note them up and do some daily analysis of it. Similarly, Program that I've made so far
if pretended to take some value and plot it on the graph. For Data analysis, Habit Tracking and some other reasons choosing of such approaches
while programming is so nice. This is just a bit part of a code

"""

import requests
from datetime import datetime

USERNAME = "myUsername"
TOKEN = "myToken"
GRAPHID = "nameOfTheGraph"
TODAY = datetime.now().strftime("%Y%m%d")


def delete_event() -> None:
    """
    This function updates the data for specific date
    :return: None
    """
    API_KEY = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}/{TODAY}"
    headers = {"X-USER-TOKEN": TOKEN}
    response = requests.post(url=API_KEY, headers=headers)


def update_event() -> None:
    """
    This function updates the data for specific date
    :return: None
    """
    API_KEY = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}/{TODAY}"
    headers = {"X-USER-TOKEN": TOKEN, }
    body = {"quantity": "-0.7"}
    requests.post(url=API_KEY, json=body, headers=headers)


def create_event():
    """
    this function creates a pixel to added onto the stage
    :return: None
    """
    API_KEY = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}"
    headers = {"X-USER-TOKEN": TOKEN, }
    body = dict(date=TODAY, quantity="19.0")
    requests.post(url=API_KEY, json=body, headers=headers)
