from flask import Flask, request, jsonify
import os  # Handle environment variables for deployment

app = Flask(__name__)

# Store latest moisture data (temporary in-memory storage)
latest_data = {
    "moisture": None
}

@app.route('/upload', methods=['POST'])
def upload_data():
    global latest_data
    try:
        data = request.get_json()

        # Ensure data contains 'moisture' key
        if "moisture" not in data:
            return jsonify({"error": "Missing 'moisture' field"}), 400

        latest_data["moisture"] = data["moisture"]

        print(f"Received Moisture Data: {latest_data['moisture']}%")
        return jsonify({"status": "success"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/get-data', methods=['GET'])
def get_data():
    return jsonify(latest_data), 200

if __name__ == '_main_':
    port = int(os.environ.get('PORT', 8080))  # Use PORT from Render, fallback to 10000 for local testing
    app.run(host='0.0.0.0',port=port)
