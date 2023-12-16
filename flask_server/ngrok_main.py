from flask_ngrok import run_with_ngrok
from flask import Flask, request



# Start flask app and set to ngrok
app = Flask(__name__)
run_with_ngrok(app)



@app.route('/llm_chat', methods=['POST'])
def generate_image():
    prompt = request.form['prompt-input']
    print(f"Generating an response for {prompt}")

    print("Sending image ...")
    response_data = {
    "message": "Data received successfully",
    "color_select": [selectedcolor, 0, 0, 0]  # body color, mirror, wheel, caliber
                    }
    return jsonify(response_data)
#   return render_template('index.html', generated_image=img_str)


if __name__ == '__main__':
    app.run()

'''
pip install pyngrok
pip install flask_ngrok

!pip install pyngrok
!pip install flask_ngrok
'''