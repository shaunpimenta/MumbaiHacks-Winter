# pip install requests

import requests
import json

# Replace the URL with the actual URL of your Flask API
# http://127.0.0.1:5000

# server = "http://127.0.0.1:5000/"
server = "https://customwheelsapi.atharvapawar.repl.co/"
api_url = f'{server}chat'

# Sample data to send in the POST request
data = {
    'user': 'John Doe',
    'message': 'Hello, Flask API!'
}

# Convert data to JSON format
json_data = json.dumps(data)

# Set the headers to indicate that you are sending JSON data
headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post(api_url, data=json_data, headers=headers)

# Print the response
print("Response Code:", response.status_code)
print("Response JSON:", response.json())
