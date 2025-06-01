from flask import Flask, request, jsonify, render_template
import random
import string

app = Flask(__name__)

parcels = {}

def generate_tracking_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    data = request.json
    track_code = generate_tracking_code()
    parcels[track_code] = data
    return jsonify({"track_code": track_code})

@app.route('/track/<track_code>', methods=['GET'])
def track(track_code):
    parcel = parcels.get(track_code)
    if parcel:
        return jsonify(parcel)
    return jsonify({"error": "Трек-код не найден"}), 404

if __name__ == '__main__':
    app.run(debug=True)
