import requests
import json


def print_response(my_url, parameter):
    """
    Get and print response
    @param my_url: a substring from the request for that route
    @param parameter: that field which is printed
    """
    response = requests.get("http://127.0.0.1:8000/countries" + my_url)
    json_response = response.json()
    for country in json_response:
        data = {
            "id": country["pk"],
            "name": country["fields"]["name"],
            parameter: country["fields"][parameter]
        }
        print(json.dumps(data, indent=3))


def run_api():
    while True:
        client_request = input()
        if client_request == "top 10 tari dupa densitate":
            print_response("/top-10-countries-density_per_km2", "density_per_km2")
        if client_request == "top 10 tari dupa population":
            print_response("/top-10-countries-population", "population")
        if client_request == "lista tari cu limba engleza":
            print_response("/language-english", "languages")
        if client_request == "lista tari cu UTC+1":
            print_response("/time-zone/UTC+1", "time_zone")
        if client_request == "lista tari monarhice":
            print_response("/government-monarchy", "government")
        if client_request == "lista tarilor din lume":
            response = requests.get("http://127.0.0.1:8000/countries/")
            data = response.json()
            print(json.dumps(data, indent=4))
        if client_request == 'exit':
            return


if __name__ == "__main__":
    run_api()
