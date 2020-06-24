from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/numero/<numero>')
def mostra_numero(numero):
    return '<h2>Hello World!</h2>. O número escolhido é: ' + numero

@app.route('/', methods = [ 'get', 'post'])
def rota_padrao():
    return {'nome':'lucas','profissão':'estudante'}

@app.route('/soma', methods=['GET','POST'])
def somar():
    # Também pode ser feito da seguinte forma
    # dados = request.get_json(force=True)
    # return str(sum(dados['valores']))

    if request.method == 'POST':
        dados = json.loads(request.data)
        soma = sum(dados['valores'])
    else:
        soma = 10 + 10
    return {'total': soma}
    
desenvolvedores = [
    {'id': 0,
    'nome' : 'Rafael Galleani',
    'habilidades': ['Django','Flask']},

    {'id': 1,
    'nome': 'Lucas',
    'habilidades': ['Python', 'Javascript']}
]

@app.route('/dev/<int:id>', methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    metodo = request.method
    
    try:
        if metodo == 'GET':
            return desenvolvedores[id]
        elif metodo == 'PUT':
            desenvolvedores[id] = json.loads(request.data)
        elif metodo == 'DELETE':
            desenvolvedores.pop(id)
        return 'ok'
    except IndexError:
        return {'erro: ': 'O registro de id {} não existe'.format(id)}
    except Exception as erro:
        return {'erro: ': str(erro)}


@app.route('/dev/',methods=['GET','POST'])
def developer():
    metodo = request.method

    if metodo == 'POST':
        dados = json.loads(request.data)
        dados['id'] = len(desenvolvedores)
        desenvolvedores.append(dados)

    elif metodo == 'GET':
        return jsonify(desenvolvedores)
    return 'ok'

tarefas = [
    {'id': 0,'responsável': 'Mário', 'tarefas': ['Product Owner'], 'status': 'ativa'},
    # {'id': 1,'responsável': 'Luigi', 'tarefas': ['backend', 'BDR', 'DevOps'], 'status': 'ativa'},
    # {'id': 2,'responsável': 'Bowser', 'tarefas': ['frontend', 'UI/UX'], 'status': 'inativa'},
    {'id': 3,'responsável': 'Peach', 'tarefas': ['frontend'], 'status': 'ativa'}
]

@app.route('/tarefas', methods=['GET','POST','PUT','DELETE'])
def tarefa():
    metodo = request.method
    try:
        if metodo == 'GET':
            try: #se houver campo id, tenta buscá-lo. Se não for encontrado, informa que não foi encontrado
                dados = json.loads(request.data)
                for i in range(len(tarefas)):
                    if dados['id'] == tarefas[i]['id']:
                        return tarefas[i]
                return 'id não encontrado'
            except:
                return jsonify(tarefas)
        else:
            dados = json.loads(request.data)
            if metodo == 'POST':
                for i in range(len(tarefas)):
                    if tarefas[i]['id'] != i:
                        dados['id'] = i
                        tarefas.insert(i,dados)
                        return dados
                dados['id'] = len(tarefas)
                tarefas.append(dados)
                return dados
            elif metodo == 'PUT':
                for i in range(len(tarefas)): # faz uma busca sequencial até encontrar o id a ser alterado
                    if tarefas[i]['id'] == dados['id']:
                        tarefas[i]['status'] = dados['status']
                        return tarefas[i]
                return 'id não encontrado'
            elif metodo == 'DELETE':
                for i in range(len(tarefas)): # faz uma busca sequencial até encontrar o id a ser deletado
                    if tarefas[i]['id'] == dados['id']:
                        return tarefas.pop(i)
                return 'id não encontrado'
    except IndexError:
        return 'Erro de índice: índice não encontrado'
    except Exception as erro: #o programa não deverá chegar até aqui
        return str(erro)

if __name__ == '__main__':
    app.run()
