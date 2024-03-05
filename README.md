# Microservice for Processing JSON Data
This microservice retrieves specific data from a JSON file, specifically designed to return a list of moves for a given Pokémon name from a predefined JSON dataset.

## Features
Retrieve data for a specified Pokémon name via a RESTful API.
## Getting Started
These instructions will guide you on how to interact with the microservice.

## Prerequisites
No prerequisites are required as the microservice uses a predefined JSON file for data retrieval.
## Communication Contract
To ensure reliable interaction with the microservice, please adhere to the following communication contract. This contract outlines how to request and receive data programmatically.

## Requesting Data
To request data from the microservice, you need to send a HTTP GET request to the endpoint with the Pokémon's name. The endpoint follows the pattern /pokemon/{pokemon_name}, where {pokemon_name} is the name of the Pokémon you're interested in.

## Example Request:

Here is how you can request data for "Bulbasaur":

```python
import requests
```

# Endpoint URL
url = 'https://cs361-get-json-key-micro-0d1965251b55.herokuapp.com/pokemon/Bulbasaur'

# Send GET request
response = requests.get(url)
## Receiving Data
The microservice responds with a JSON payload containing a list of moves associated with the requested Pokémon name. If successful, the HTTP status code 200 OK is returned along with the data. If the requested Pokémon name does not exist in the dataset, the microservice will return an HTTP status code 404 Not Found with an error message.

## Example Response:

For a successful request, you might receive a response like this:

```json
[
    "tackle",
    "growl",
    "leech seed",
    "vine whip"
]
```

In case of an error (e.g., Pokémon not found), the response might look like:

```json
{
    "error": "Pokémon 'Bulbasaur' not found"
}
```
## Using the Microservice
To retrieve data for a specific Pokémon, follow the example provided in the "Requesting Data" section. This service will return a list of moves associated with that Pokémon.

Python GET Example:

```python
import requests

# Replace with the actual URL of your microservice
url = 'https://cs361-get-json-key-micro-0d1965251b55.herokuapp.com/pokemon/Bulbasaur'

response = requests.get(url)

if response.status_code == 200:
    print(response.json())  # Prints the list of moves for "Bulbasaur"
else:
    print("Error:", response.text)

```


## Output
The microservice returns a JSON list of moves associated with the specified Pokémon name. If the Pokémon name does not exist in the dataset, an error message will be returned.

## UML Sequence Diagram



## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
