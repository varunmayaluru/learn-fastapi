import requests

def post_item():
    url = 'http://127.0.0.1:8000/items/'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    data = {
        "name": "item1001",
        "description": "Sutures",
        "price": 10.25,
        "tax": 0.20
    }

    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the JSON response if needed
    else:
        return f"Request failed with status code {response.status_code}"

# Example usage:
response_data = post_item()
print(response_data)


# df = requests.post("https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv")

# print(df.json)
