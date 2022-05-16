import requests


def get_drivers_standings(year):
    url = f"http://ergast.com/api/f1/{year}/driverStandings.json"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

def get_teams_standings(year):
    url = f"http://ergast.com/api/f1/{year}/constructorStandings.json"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

def get_race_result(year,round):
    url = f"http://ergast.com/api/f1/{year}/{round}/results"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)