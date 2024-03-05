# Microservice for Processing JSON Data
This microservice retrieves specific data from a JSON file. It is designed to return a list of moves for a given Pokémon name from a predefined JSON dataset.

## Features
Retrieve data for a specified Pokémon name via a RESTful API.
## Getting Started
The following instructions will provide guidance on how to use the microservice.

## Prerequisites
None. The microservice uses a predefined JSON file for data retrieval.
Using the Microservice
To retrieve data for a specific Pokémon, send a request with the Pokémon's name. The service will return a list of moves associated with that Pokémon.

## Python GET Example:

```python
Copy code
import requests

url = 'https://cs361-get-json-key-micro-0d1965251b55.herokuapp.com/pokemon/Bulbasaur'  # Replace with the actual URL of your microservice

response = requests.get(url)

if response.status_code == 200:
    print(response.json())  # Prints the list of moves for "Bulbasaur"
else:
    print("Error:", response.text)

```


## Output
The microservice will return a JSON list of moves associated with the specified Pokémon name. If the Pokémon name does not exist in the dataset, an error message will be returned.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
