from flask import Flask, request
from flask_restful import Api, Resource
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPAuth, HTTPBasicAuth

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

# usuarios = {
#     'lucas': 'abcde',
#     'rafael': '123'
# }
# @auth.verify_password
# def verificaSenha1(usuario,senha):
#     return usuarios.get(usuario) == senha

@auth.verify_password
def verificaSenha2(login,password):
    try:
        usuario = Usuarios.query.filter_by(usuario=login, senha=password).first()
        if usuario.ativo:
            return True
        else:
            return False
    except:
        return False

def achaPessoa(id):
    return Pessoas.query.filter_by(id=id).first()

class Hello(Resource):
    def get(self):
        return 'Olá Mundo'

class Pessoa(Resource):
    def get(self, id):
            try:
                pessoa = achaPessoa(id)
                return {'id': pessoa.id, 'nome': pessoa.nome, 'idade': pessoa.idade}
            except AttributeError:
                return 'O id {} não foi encontrado'.format(id)

    # altera as informações de uma pessoa pelo id
    @auth.login_required
    def put(self,id):
        pessoa = achaPessoa(id)
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.salvar()
        return {'id': pessoa.id, 'nome': pessoa.nome, 'idade': pessoa.idade}

    # deleta pessoa pelo id
    @auth.login_required
    def delete(self,id):
        try:
            pessoa = achaPessoa(id)
            pessoa.deletar()
            return '{} foi deletado.'.format(pessoa.nome)
            # return {'id': pessoa.id, 'nome': pessoa.nome, 'idade': pessoa.idade} if pessoa else 'id {} não encontrado'.format(id)
        except AttributeError:
            return 'id {} não encontrado'.format(id)

class ListaPessoas(Resource):
    def get(self):
        listaPessoas = Pessoas.query.all()
        return [{'id': i.id, 'nome':i.nome, 'idade':i.idade} for i in listaPessoas]
    @auth.login_required()
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.salvar()
        return {'id':pessoa.id, 'nome':pessoa.nome, 'idade':pessoa.idade}

class Atividade(Resource):
    def get(self):
        listaAtividades = Atividades.query.all()
        return [{'id': i.id,'nome da atividade': i.nome,'nome da pessoa': i.pessoa.nome} for i in listaAtividades]
    
    @auth.login_required
    def put(self):
        dados = request.json
        atividade = Atividades.query.filter_by(id=dados['id']).first()
        if ('nome' in dados):
            atividade.nome = dados['nome']
        atividade.salvar()
        return { 'nome': atividade.nome }
        
    @auth.login_required
    def post(self):
        dados = request.json
        pessoa = achaPessoa(dados['pessoa_id'])
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.salvar()
        return {'id': atividade.id, 'nome da atividade': atividade.nome, 'nome da pessoa': pessoa.nome}


api.add_resource(Hello, '/')
api.add_resource(Pessoa, '/pessoa/<int:id>')
api.add_resource(ListaPessoas, '/pessoas')
api.add_resource(Atividade, '/atividades')

if (__name__ == "__main__"):
    app.run(debug=True)