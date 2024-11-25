from flask import Flask, request, jsonify

app = Flask(__name__)
missions = []

@app.route('/mission', methods=['POST'])
def post_mission():
    data = request.json
    missions.append(data)
    return jsonify({"status": "success", "message": "Mission received"}), 201

@app.route('/mission', methods=['GET'])
def get_mission():
    return jsonify(missions), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
