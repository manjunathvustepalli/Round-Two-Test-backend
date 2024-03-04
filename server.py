from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["*"])

@app.post("/api/csv/v1")
def upload_csv():
    if 'file' not in request.files:
        return jsonify({"message": "No file part in the request"}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({"message": "No file selected for uploading"}), 400

    if not file.filename.endswith('.csv'):
        return jsonify({"message": "File is not a CSV"}), 400
    file.save("uploads/" + file.filename)

    return jsonify({"message": "CSV uploaded successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=4545)
