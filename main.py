from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST', 'HEAD'])
def webhook():
    if request.method == 'HEAD':
        return '', 200
    
    data = request.json
    print(f"Webhook recebido: {data}")
    
    return jsonify({"status": "ok"}), 200

@app.route('/', methods=['GET'])
def home():
    return "Webhook Trello OK", 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
