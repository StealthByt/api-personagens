from flask import Flask, jsonify, request

app = Flask(__name__)
class Personagem:
    def __init__(self, nome, descricao, link_imagem, programa, animador):
        self.nome = nome
        self.descricao = descricao
        self.link_imagem = link_imagem
        self.programa = programa
        self.animador = animador

# Criando instâncias de personagens
mickey = Personagem("Mickey Mouse", "Rato antropomórfico", "https://wallpapers.com/images/hd/mickey-mouse-disney-z87kwkhqxqipcwh1.jpg", "Disney", "Walt Disney")
pateta = Personagem("Pateta", "Cão antropomórfico", "https://img.olhardigital.com.br/wp-content/uploads/2021/05/Pateta.jpg", "Disney", "Walt Disney")

personagens = [mickey, pateta]

@app.route('/characters/', methods=['GET', 'POST'])
def characters():
    if request.method == 'GET':
        return jsonify([personagem.__dict__ for personagem in personagens])
    elif request.method == 'POST':
        data = request.json
        nome = data.get('nome')
        descricao = data.get('descricao')
        link_imagem = data.get('link_imagem')
        programa = data.get('programa')
        animador = data.get('animador')
        novo_personagem = Personagem(nome, descricao, link_imagem, programa, animador)
        personagens.append(novo_personagem)
        return jsonify(novo_personagem.__dict__), 201

if __name__ == '__main__':
    app.run(debug=True)