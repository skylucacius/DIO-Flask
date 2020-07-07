from models import Pessoas, Atividades, session, Usuarios

def insere_pessoa(nome,idade):
    pessoa = Pessoas(nome=nome, idade=idade)
    pessoa.salvar()

def insere_atividade(nome,id):
    atividade = Atividades(nome=nome, id_pessoa=id)
    atividade.salvar()

def insere_usuario(usuario,senha,ativo):
       usuario = Usuarios(usuario=usuario,senha=senha, ativo=ativo)
       usuario.salvar()

def consulta_pessoas():
    # com scoped session
    # pessoa = Pessoas.query.filter(Pessoas.nome.in_(['Rafael'])).all()
    # pessoa = Pessoas.query.filter_by(nome='Rafael').all()
    pessoas = Pessoas.query.all()
    print ([pessoa for pessoa in pessoas])

    # sem scoped session
    # for i in session.query(Pessoas):
    #     print(i)

def consulta_atividades():
    # com scoped session
    atividades = Atividades.query.all()
    print([atividade for atividade in atividades])
    # for atividade in atividades:
    #     print(atividade)

def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print ([usuario for usuario in usuarios])

def atualiza_pessoa(id, nome, idade):
    pessoa = Pessoas.query.filter_by(id=id).first()
    pessoa.nome = nome
    pessoa.idade = idade

def atualiza_atividade(nome):
    atividade = Atividades.query.filter_by(nome=nome).all()

def deleta_pessoa(id):
    try:
        pessoa = Pessoas.query.filter_by(id=id).first()
        session.delete(pessoa)
        session.commit()
    except Exception as erro: 
        print('O id {} não foi encontrado.'.format(id))

def deleta_atividade(id):
    try:
        atividade = Atividades.query.filter_by(id=id).first()
        session.delete(atividade)
        session.commit()
    except Exception as erro: 
        print('O id {} não foi encontrado.'.format(id))

def deleta_usuario(id):
    try:
        usuario = Usuarios.query.filter_by(id=id).first()
        session.delete(usuario)
        session.commit()
    except Exception as erro: 
        print('O id {} não foi encontrado.'.format(id))

def deleta_pessoas():
    pessoas = Pessoas.query.all()
    for pessoa in pessoas:
        deleta_pessoa(pessoa.id)

def deleta_atividades():
    atividades = Atividades.query.all()
    for atividade in atividades:
        deleta_atividade(atividade.id)

def deleta_usuarios():
    usuarios = Usuarios.query.all()
    for usuario in usuarios:
        deleta_usuario(usuario.id)

if __name__ == "__main__":
    # insere_pessoa('Galeani',30)
    # insere_pessoa('Lucas',29)
    # insere_pessoa('José',20)
    # insere_atividade('volei',1)
    # insere_atividade('basquete',1)
    # insere_atividade('queimada',2)
    # insere_usuario('lucas','12', 1)
    # insere_usuario('rafael','13', 0)

    # atualiza_pessoa(2,'Mario',15)
    # deleta_pessoa(1)
    # deleta_pessoas()
    # deleta_atividades()
    # deleta_usuarios()

    # consulta_pessoas()
    # consulta_atividades()
    consulta_usuarios()
