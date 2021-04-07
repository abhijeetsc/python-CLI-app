import fire
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

    url = f"https://services.odata.org/TripPinRESTierService/{API_KEY}/People"

    form_data = {
        '@odata.type': 'Microsoft.OData.SampleService.Models.TripPin.Person',
        'UserName': 'abhijeet123',
        'FirstName': 'Abhijeet',
        'LastName': 'Chouhan',
        'Emails': [
            'abhijeet@example.com'
        ],
        'AddressInfo': [
            {
                'Address': '23 Suffolk Ln.',
                'City': {
                    'Name': 'Boise',
                    'CountryRegion': 'United States',
                    'Region': 'NW'
                }
            }
        ]
    }

    headers_data = {
        'OData-Version': '4.0',
        'Content-Type': 'application/json;odata.metadata=minimal',
        'Accept': 'application/json',
    }

    response = requests.post(url, data=form_data, headers=headers_data)
    print(response.status_code)
    print(response.text)


def user_detail(id):
    """ To get details of a user via Id(USerName) """
    url = f"https://services.odata.org/v4/TripPinServiceRW/{API_KEY}/People('{id}')"
    response = requests.get(url)
    print(f"HTTP {response.status_code}\n")
    if response.status_code == 200:
        pp.pprint(response.json())
    else:
        print("User does not exist")


if __name__ == '__main__':
    # converting our function in a Command Line Interface (CLI).
    fire.Fire()
