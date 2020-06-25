from flask import Flask, request
from flask_restful import Resource, Api
import json
from tarefas import Tarefas

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return 'Hello World'

tarefas = [
    {'id': 0,'responsável': 'Mário', 'tarefas': ['Product Owner'], 'status': 'ativa'},
    # {'id': 1,'responsável': 'Luigi', 'tarefas': ['backend', 'BDR', 'DevOps'], 'status': 'ativa'},
    # {'id': 2,'responsável': 'Bowser', 'tarefas': ['frontend', 'UI/UX'], 'status': 'inativa'},
    {'id': 3,'responsável': 'Peach', 'tarefas': ['frontend'], 'status': 'ativa'}
]

class Tarefa(Resource):
    def get(self):
        try: #se houver campo id, tenta buscá-lo. Se não for encontrado, informa que não foi encontrado
            dados = json.loads(request.data)
            for i in range(len(tarefas)):
                if dados['id'] == tarefas[i]['id']:
                    return tarefas[i]
            return 'id não encontrado'
        except:
            return tarefas
    
    def post(self):
        dados = json.loads(request.data)
        for i in range(len(tarefas)):
            if tarefas[i]['id'] != i:
                dados['id'] = i
                tarefas.insert(i,dados)
                return dados
        dados['id'] = len(tarefas)
        tarefas.append(dados)
        return dados
    
    def put(self):
        dados = json.loads(request.data)
        for i in range(len(tarefas)): # faz uma busca sequencial até encontrar o id a ser alterado
            if tarefas[i]['id'] == dados['id']:
                tarefas[i]['status'] = dados['status']
                return tarefas[i]
        return 'id não encontrado'
    
    def delete(self):
        dados = json.loads(request.data)
        for i in range(len(tarefas)): # faz uma busca sequencial até encontrar o id a ser deletado
            if tarefas[i]['id'] == dados['id']:
                return tarefas.pop(i)
        return 'id não encontrado'


api.add_resource(Home,'/')
api.add_resource(Tarefa,'/tarefa')
api.add_resource(Tarefas, '/tarefas')

if __name__ == "__main__":
    app.run()

