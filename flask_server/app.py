from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat/<input_chat>')
def chat(input_chat):
    # Extract color from the chat input (assuming the input is in the format "#RRGGBB")
    color_hex = input_chat.split(' ')[-1]
    color = int(color_hex[1:], 16)  # Convert hex to decimal

    # Call the JavaScript function to change the material color
    return f'<script>changeMaterialColor({color});</script>'

if __name__ == '__main__':
    app.run(debug=True)
