# pip install requests

import requests
import json

# Replace the URL with the actual URL of your Flask API
# http://127.0.0.1:5000

# server = "http://127.0.0.1:5000/"
# server = "https://customwheelsapi.atharvapawar.repl.co/"
server = "https://ffb9-35-185-185-55.ngrok-free.app/"
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

try:
    # Send the POST request
    response = requests.post(api_url, data=json_data, headers=headers)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

    # Print the response
    print("Response Code:", response.status_code)
    print("Response JSON:", response.json())

except requests.exceptions.RequestException as e:
    print(f"Error in request: {e}")


'''
chats examples:

curl -X POST -d "message=Hello" https://ccc7-35-185-185-55.ngrok-free.app/chat


'''