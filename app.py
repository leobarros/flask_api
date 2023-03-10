from flask import Flask, request, jsonify, g
import sqlite3

app = Flask(__name__)
DATABASE = 'produtos.db'
db = sqlite3.connect('produtos.db')
db.execute('''CREATE TABLE IF NOT EXISTS produtos
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INT NOT NULL);''')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# listar todos os produtos
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    db = get_db()
    produtos = db.execute('SELECT * FROM produtos').fetchall()
    return jsonify([dict(produto) for produto in produtos])

# # buscar um produto pelo ID
@app.route('/produtos/<int:produto_id>', methods=['GET'])
def buscar_produtos(produto_id):
    db = get_db()
    produto = db.execute('SELECT * FROM produtos WHERE id = ?', (produto_id,)).fetchone()
    return jsonify(dict(produto))

# Adicionar um novo produto
@app.route('/produtos', methods=['POST'])
def adicionar_produtos():
    novo_produto = request.get_json()
    nome = novo_produto['nome']
    preco = novo_produto['preco']
    quantidade = novo_produto['quantidade']
    db = get_db()
    db.execute('INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)', (nome, preco, quantidade))
    db.commit()
    return jsonify({'mensagem': 'Produto adicionado com sucesso!'})

# Atualizar um novo produto pelo ID
@app.route('/produtos/<int:produto_id>', methods=['PUT'])
def atualizar_produto(produto_id):
    produto_atualizado = request.get_json()
    nome = produto_atualizado['nome']
    preco = produto_atualizado['preco']
    quantidade = produto_atualizado['quantidade']
    db = get_db()
    db.execute('UPDATE produtos SET nome = ?, preco = ?, quantidade = ?, WHERE id = ?', (nome, preco, quantidade, produto_id))
    db.commit()
    return jsonify({'mensagem': 'Produto atualizado com sucesso!'})

# Deletar um produto pelo ID
@app.route('/produtos/<int:produto_id>', methods=['DELETE'])
def deletar_produtos(produto_id):
    db = get_db()
    db.execute('DELETE FROM produtos WHERE id = ?', (produto_id,))
    db.commit()
    return jsonify({'mensagem': 'Produto deletado com sucesso!'})

# servidor
if __name__ == '__main__':
    app.run(debug=True)