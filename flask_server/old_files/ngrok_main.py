from flask_ngrok import run_with_ngrok
from flask import Flask, request, jsonify

# Start flask app and set to ngrok
app = Flask(__name__)
run_with_ngrok(app)


@app.route('/chat', methods=['POST'])
def generate_image():
    prompt = request.form['message']
    print(f"Generating an response for {prompt}")

    # colorPalate = ["orange", "dark orange", "blue", "red", "white"]

    
    response_data = {
        "message": "Data received successfully",
        "color_select": [1, 0, 0, 0],  # body color, mirror, wheel, caliber
        "chat_response": "llm_response",
                    }
    
    return jsonify(response_data)


if __name__ == '__main__':
    app.run()

'''
pip install pyngrok
pip install flask_ngrok

!pip install pyngrok
!pip install flask_ngrok
'''