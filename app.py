from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_plan():
    data = request.get_json()
    rooms = data['rooms']

    plan = "Generated AutoCAD Plan:\n"
    for room in rooms:
        plan += f"- {room['name']}: {room['length']}m x {room['width']}m at ({room['x']}, {room['y']})\n"

    return jsonify({'plan': plan})

if __name__ == '__main__':
    app.run(debug=True)
