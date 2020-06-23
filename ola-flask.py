from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/numero/<numero>')
def mostra_numero(numero):
    return '<h2>Hello World!</h2>. O número escolhido é: ' + numero

@app.route('/', methods = [ 'get', 'post'])
def rota_padrao():
    return {'nome':'lucas','profissão':'estudante'}

@app.route('/soma', methods=['get','post'])
def somar():
    # Também pode ser feito da seguinte forma
    # dados = request.get_json(force=True)
    # return str(sum(dados['valores']))

    if request.method == 'post':
        dados = json.loads(request.data)
        soma = sum(dados['valores'])
    else:
        soma = 10 + 10
    return {'total': soma}
    


if __name__ == '__main__':
    app.run()
