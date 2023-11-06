from flask import Flask, request, render_template, redirect
from mysql.connector import connect, Error

app = Flask(__name__)

def mysql_connection(host, user, passwd, database=None):
    try:
        connection = connect(
            host = host,
            user = user,
            passwd = passwd,
            database = database
        )
        return connection
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

connection = mysql_connection('localhost', 'root', 'root', 'cafe')
cursor = connection.cursor()
    
@app.route('/')
def formulario():
    return render_template('Login.html')

@app.route('/processar', methods=['POST'])
def processar_formulario():
    usuario = request.form['usuario']
    senha = request.form['senha']
    cursor.execute("SELECT * FROM usuario WHERE usuario = %s", (usuario,))
    resultado = cursor.fetchone()
    if(resultado != None and resultado[1] == senha):
        return render_template('GerenciarProdutos.html')
    else:
        return render_template('Login.html')

@app.route('/cadastrar', methods=['POST'])
def adicionar_produto():
    nome = request.form.get('nome')
    id = request.form.get('id')
    preco = request.form.get('preco')
    imagem = request.form.get('imagem')
    cursor.execute("INSERT INTO produtos (nome, id, preco, imagem) VALUES (%s, %s, %s, %s)", (nome, id, preco, imagem))
    connection.commit()
    return render_template('Cardapio.html')

@app.route('/editar', methods=['POST'])
def editar_produto():
    nome = request.form.get('nome')
    id = request.form.get('id')
    preco = request.form.get('preco')
    imagem = request.form.get('imagem')
    cursor.execute("UPDATE produtos SET nome = %s, preco = %s, imagem = %s WHERE id = %s", (nome, preco, imagem, id,))
    connection.commit()
    return render_template('Cardapio.html')

@app.route('/deletar')
def deletar_produto():
    id = request.form.get('id')
    cursor.execute("DELETE FROM produtos WHERE id = %s")
    connection.commit()
    return render_template('Cardapio.html')

if __name__ == '__main__':
    app.run(debug=True)