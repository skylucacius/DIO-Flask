from flask_restful import Resource

lista_tarefas = ['Product Owner', 'backend', 'DevOps', 'frontend', 'UI/UX', 'Product Manager', 'DBA']

class Tarefas(Resource):
    def get(self):
        return lista_tarefas