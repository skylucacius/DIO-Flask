from models import Pessoas, Atividades, salvar, session

def insere_pessoas(nome,idade):
    pessoa = Pessoas(nome=nome, idade=idade)
    # pessoa.save()
    salvar(pessoa)
    print(pessoa)

def insere_atividades(nome,id):
    atividade = Atividades(nome=nome, pessoa_id=id)
    # atividade.save()
    salvar(atividade)
    print(atividade)

def atualiza_atividades(nome):
    atividade = Atividades.query.filter_by(nome=nome).all()

def consulta_pessoas():
    # com scoped session
    # pessoa = Pessoas.query.filter(Pessoas.nome.in_(['Rafael'])).all()
    # pessoa = Pessoas.query.filter_by(nome='Rafael').all()
    pessoa = Pessoas.query.all()
    print(pessoa)

    # sem scoped session
    # for i in session.query(Pessoas):
    #     print(i)

def consulta_atividades():
    # com scoped session
    atividade = Atividades.query.all()
    print(atividade)

def atualiza_pessoas(id, nome, idade):
    pessoa = Pessoas.query.filter_by(id=id).first()
    pessoa.nome = nome
    pessoa.idade = idade

def deleta_pessoas(id):
    pessoa = Pessoas.query.filter_by(id=id).first()
    try:
        session.delete(pessoa)
        session.commit()
    except Exception as erro: 
        print('O id {} não foi encontrado.'.format(id))

    # deletar(pessoa)

if __name__ == "__main__":
    # insere_pessoas('Galeani',30)
    # insere_pessoas('Lucas',29)
    # insere_pessoas('José',20)
    # insere_atividades('volei',1)
    # insere_atividades('basquete',1)
    # insere_atividades('queimada',2)
    # atualiza_pessoas(2,'Mario',15)
    # deleta_pessoas(1)

    consulta_pessoas()
    consulta_atividades()

