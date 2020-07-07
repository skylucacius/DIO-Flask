from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///atividades.db", convert_unicode=True)
base = declarative_base()
# Usando scoped session
session = scoped_session(sessionmaker(bind=engine))
base.query = session.query_property()
# Sem scoped session
# Session = sessionmaker(bind=engine); session = Session()
class Metodos():
    def salvar(self):
        session.add(self)
        session.commit()

    def deletar(self):
        session.delete(self)
        session.commit()
            
# Uma pessoa pode fazer várias atividades. 1-N
class Pessoas(base, Metodos):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String, index=True)
    idade = Column(Integer)
    atividade = relationship('Atividades')

    def __repr__(self):
        return 'Pessoa: ' + str(self.id) + self.nome + str(self.idade)


class Atividades(base, Metodos):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    id_pessoa = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship('Pessoas')

    def __repr__(self):
        return 'Atividade: ' + str(self.id) + ' Nome: ' + self.nome + ' id da pessoa: ' + str(self.id_pessoa) + ' nome da pessoa: ' + str(self.pessoa.nome)
        #  + str(self.pessoa.nome)

class Usuarios(base, Metodos):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    usuario = Column(String)
    senha = Column(String)
    ativo = Column(Boolean)

    def __repr__(self):
        return 'Usuário: ' + self.usuario + ' Senha: ' + self.senha + ' ativo: ' + ('sim' if self.ativo else 'não')

def init_db():
    base.metadata.create_all(engine)
    
init_db()
