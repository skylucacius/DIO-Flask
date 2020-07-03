from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
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
        return '\n' + 'Pessoa: ' + str(self.id) + self.nome + str(self.idade)


class Atividades(base, Metodos):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship('Pessoas')

    # pessoa = relationship('Pessoas', back_populates='atividades')
    def __repr__(self):
        return '\n' + 'Atividade: ' + str(self.id) + self.nome + str(self.pessoa_id)

    # def save(self):
    #     session.add(self)
    #     session.commit()


def init_db():
    base.metadata.create_all(engine)
    
init_db()
