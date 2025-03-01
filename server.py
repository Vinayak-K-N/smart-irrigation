from flask import Flask, request, jsonify

app = Flask(__name__)

# Store latest sensor data (temporary in-memory storage)
latest_data = {
    "moisture": None,
    "temperature": None,
    "humidity": None
}

@app.route('/upload', methods=['POST'])
def upload_data():
    global latest_data
    data = request.get_json()
    latest_data.update({
        "moisture": data.get('moisture'),
        "temperature": data.get('temperature'),
        "humidity": data.get('humidity')
    })
    print(f"Received Data: {latest_data}")
    return jsonify({"status": "success"}), 200

@app.route('/get-data', methods=['GET'])
def get_data():
    return jsonify(latest_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
