'''response codes:  404 - not found
                    401 - not authorised
                    informational responses (100-199)
                    successful responses (200-299)
                    redirection messages (300-399)
                    client error response (400-499)
                    server error response (500-599)'''

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
        
# response object has an attribute of status code, so
    if response.status_code == 200: # 200 means response is OK
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to get data, error code {response.status_code}")

pokemon_name = input("Enter your favourite pokemon's name: ")
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info: #True
    print(f"Name : {pokemon_info["name"].capitalize()}")
    print(f"Height : {pokemon_info["height"]} feet")
    print(f"Weight : {pokemon_info["weight"]} kilos")
    print(f"Serial number : {pokemon_info["id"]}")