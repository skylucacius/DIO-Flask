from flask import Flask
app = Flask(__name__)

@app.route('/numero/<numero>')
def mostra_numero(numero):
    return '<h2>Hello World!</h2>. O número escolhido é: ' + numero

@app.route('/', methods = [ 'get', 'post'])
def rota_padrao():
    return {'nome':'lucas','profissão':'estudante'}

if __name__ == '__main__':
    app.run()
