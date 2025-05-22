from flask import Flask, request, jsonify, send_from_directory
import json

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'admin.html')

@app.route('/display')
def display():
    return send_from_directory('.', 'emmaus_display.html')

@app.route('/data')
def get_data():
    with open('data.json', 'r') as f:
        return jsonify(json.load(f))

@app.route('/update', methods=['POST'])
def update_data():
    content = request.json
    with open('data.json', 'w') as f:
        json.dump({"montant": content['montant']}, f)
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)