# pip install Flask Flask-CORS


from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json  # Assuming the incoming data is in JSON format
        # print("Received data:", data)

        print("Received User data:", data['user'])
        print("Received Message data:", data['message'])

        colorPalate = ["orange", "dark orange", "blue", "red", "white"]

        for index, item in enumerate(colorPalate):
            if item in data['message']:
                selectedcolor = index

        # Add your processing logic here if needed

        response_data = {
            "message": "Data received successfully",
            "color_select": [selectedcolor, 0, 0, 0]  # body color, mirror, wheel, caliber
                         }
        return jsonify(response_data)

    except Exception as e:
        error_message = {"error": str(e)}
        return jsonify(error_message), 400  # Return a 400 status code for bad requests

if __name__ == '__main__':
    app.run(debug=True)
'''
Received data: {'user': 'John Doe', 'message': 'Hello, Flask API!'}

["orange", "dark orange", "blue", "red", "white"]

0:orange
1:dark orange
2:blue
3:red
4:white

0:orange
1:dark orange
2:blue
3:red
4:white

body, mirror, wheel, caliber
'''