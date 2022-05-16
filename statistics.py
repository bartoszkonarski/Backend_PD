import requests


def get_drivers_standings(year):
    url = f"http://ergast.com/api/f1/{year}/driverStandings.json"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).json()
    standings = response['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
    data = []
    place = 1
    for standing in standings:
        driver = {
            'No' : place,
            'Name' : standing['Driver']['givenName'],
            'Surname': standing['Driver']['familyName'],
            'URL': standing['Driver']['url'],
            'Points': standing['points'],
            'Team' : standing['Constructors'][0]['name']
        }
        data.append(driver)
        place += 1

    return data

def get_teams_standings(year):
    url = f"http://ergast.com/api/f1/{year}/constructorStandings.json"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).json()
    standings = response['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']
    data = []
    place = 1
    for standing in standings:
        team = {
            'No' : place,
            'Name' : standing['Constructor']['name'],
            'URL': standing['Constructor']['url'],
            'Points': standing['points'],
        }
        data.append(team)
        place += 1

    return(data)

get_teams_standings(2022)