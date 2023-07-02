from flask import Flask, jsonify
from api import api_bp

app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def home():
    return jsonify(message='API hit!')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')