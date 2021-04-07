import fire
import json
import pprint
import requests

pp = pprint.PrettyPrinter(indent=4)

API_KEY = '(S(soqbcshubhfoukdhx3mzfmon))'


def user_filter(firstname):
    """ To filter the data based on the 'FirstName' filter """

    url = f"https://services.odata.org/TripPinRESTierServicse/{API_KEY}/People?$filter=FirstName eq '{firstname}'"
    response = requests.get(url)

    print(f"HTTP {response.status_code}\n")
    if response.status_code == 200:
        pp.pprint(response.json())
    else:
        print("Some error occured.")


def create_user():
    """ To create a new user """

    with open('new_user.json') as json_file:
        dict_data = json.load(json_file)

    url = f"https://services.odata.org/TripPinRESTierService/{API_KEY}/People"

    payload = str(dict_data)

    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.post(url, data=payload, headers=headers)

    print(f"HTTP {response.status_code}\n")
    pp.pprint(response.json())


def user_detail(id):
    """ To get details of a user via Id(USerName) """
    url = f"https://services.odata.org/TripPinRESTierService/{API_KEY}/People('{id}')"

    response = requests.get(url)
    print(f"HTTP {response.status_code}\n")
    if response.status_code == 200:
        pp.pprint(response.json())
    else:
        print("User does not exist")


if __name__ == '__main__':
    # converting our function in a Command Line Interface (CLI).
    fire.Fire()
