from flask import Flask, request, jsonify
import os

app = Flask(name)

@app.route('/webhook', methods=['POST', 'HEAD'])
def webhook():
    if request.method == 'HEAD':
        return '', 200
    
    data = request.json
    print(f"Webhook recebido: {data}")
    
    Aqui você processa os eventos do Trello
    Por enquanto só loga
    
    return jsonify({"status": "ok"}), 200

if name == 'main':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
