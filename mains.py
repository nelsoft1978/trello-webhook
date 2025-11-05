from flask import Flask, request, jsonify
import os

app = Flask(name)

Mapeamento: usuário Trello → número WhatsApp
USUARIOS = {
    "emmanoelmiranda": "+5581991773444",
  "policarpodefreitas": "+5581999777102",
  "gustavoandrade271": "+5581999760491",
  "aluisiodesousasantosneto1": "+5581997307211",
  "wirlasouza22": "+5581998805706",
    Adiciona mais usuários aqui
}

@app.route('/webhook', methods=['POST', 'HEAD'])
def trello_webhook():
    Trello envia HEAD pra validar webhook
    if request.method == 'HEAD':
        return '', 200
    
    data = request.json
    action_type = data.get('action', {}).get('type')
    
    Detecta quando alguém é atribuído a um card
    if action_type == 'addMemberToCard':
        card_name = data['action']['data']['card']['name']
        board_name = data['action']['data']['board']['name']
        member = data['action']['memberCreator']['username']
        assigned = data['action']['member']['username']
        
        print(f"Card: {card_name}")
        print(f"Quadro: {board_name}")
        print(f"Atribuído: {assigned}")
        
        if assigned in USUARIOS:
            numero = USUARIOS[assigned]
            mensagem = f"Você foi atribuído ao card '{card_name}' no quadro '{board_name}'"
            print(f"Enviando WhatsApp para {numero}: {mensagem}")...

(Message continues - ask me for more)
