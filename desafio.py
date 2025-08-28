from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    telefone = Column(String(50))
    email = Column(String(50))
    endereco = Column(String(50))

class Produto(Base):
    __tablename__ = 'produtos'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    descricao = Column(String(50))
    preco = Column(String(50))
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))

    fornecedor = relationship('Fornecedor')

# Conectar ao SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#   Inserindo fornecedores
try:

    with Session() as session:

        #   Criando uma lista de objetos da classe Fornecedor
        fornecedores = [
            Fornecedor(nome="Fornecedor A", telefone="12345678", email="contato@a.com", endereco="Endereço A"),
            Fornecedor(nome="Fornecedor B", telefone="87654321", email="contato@b.com", endereco="Endereço B"),
            Fornecedor(nome="Fornecedor C", telefone="12348765", email="contato@c.com", endereco="Endereço C"),
            Fornecedor(nome="Fornecedor D", telefone="56781234", email="contato@d.com", endereco="Endereço D"),
            Fornecedor(nome="Fornecedor E", telefone="43217865", email="contato@e.com", endereco="Endereço E")
        ]

        #   Usando um só comando pra adicionar toda a lista ao banco de dados
        session.add_all(fornecedores)
        session.commit()

except SQLAlchemyError as e:
    print(f'Erro ao inserir fornecedores: {e}')


#   Inserindo produtos

try:

    with Session() as session:

        #   Criando uma lista de objetos da classe Fornecedor
        produtos = [
            Produto(nome="Produto 1", descricao="Descrição do Produto 1", preco=100, fornecedor_id=1),
            Produto(nome="Produto 2", descricao="Descrição do Produto 2", preco=200, fornecedor_id=2),
            Produto(nome="Produto 3", descricao="Descrição do Produto 3", preco=300, fornecedor_id=3),
            Produto(nome="Produto 4", descricao="Descrição do Produto 4", preco=400, fornecedor_id=4),
            Produto(nome="Produto 5", descricao="Descrição do Produto 5", preco=500, fornecedor_id=5)
        ]

        session.add_all(produtos)
        session.commit()

except SQLAlchemyError as e:
    print(f'Erro ao inserir produtos: {e}')