#-*- latin-1 -*-
from pymongo import MongoClient
import datetime
    
def insert():   
    # create a MongoClient to the running mongod instance
    #connect on the default host and port or specify
    client = MongoClient('localhost', 27017)    
    #Or use the MongoDB URI format:
    #client = MongoClient('mongodb://localhost:27017/')

    #A single instance of MongoDB can support multiple independent databases
    db = client.testedb
    
    #A collection is a group of documents stored in MongoDB (TABLE)
    #collection = db.test_collection    
    
    #Data in MongoDB is represented (and stored) using JSON-style documents. 
    #In PyMongo we use dictionaries to represent documents.
    publicacao = {
    "publicacao": {
        "titulo": "Publicacao teste",
        "datapub": datetime.datetime.utcnow(),
        "conteudo": "Bla bla bla...",
        "tipo": "Novidade",
        "usuario": {
            "nome": "Cristiano Politowski",
            "senha": "admin123",
            "datanascimento": "1987-10-27",
            "sobre": "Pesquisador e programador nas horas vagas.",
            "ativo": "True",
            "grupo": {
                "nome": "Administracao",
                "ativo": "True"
            }
        },
        "comentario": [
            {
                "nome": "Fulano de Tal",
                "email": "fulano@gmail.com",
                "datapub": datetime.datetime.utcnow(),
                "conteudo": "First!"
            }
        ]}
    }
        
    #To insert a document into a collection we can use the insert() method:
    publicacoes = db.publicacoes
    pub_id = publicacoes.insert(publicacao) #resgata o id        
    
    #Disconnecting will close all underlying sockets in the connection pool. 
    #If this instance is used again it will be automatically re-opened. 
    client.close()
    
def searchSimple():
    client = MongoClient('localhost', 27017) 
    db = client.testedb
    publicacoes = db.publicacoes
    publicacoes.find({"publicacao.titulo":"Publicacao teste"})        
    client.close()
    
def searchComplex():
    client = MongoClient('localhost', 27017) 
    db = client.testedb
    publicacoes = db.publicacoes
    publicacoes.find({"publicacao.datapub": {"$gt": datetime.datetime(2013, 11, 12, 12)}, "publicacao.datapub": {"$lt": datetime.datetime(2015, 11, 12, 12)}, "publicacao.tipo": "Novidade", "publicacao.usuario.datanascimento" : {"$gte": "1980-1-1"}, "publicacao.usuario.ativo":"True", "publicacao.usuario.grupo.nome":"Administracao", "publicacao.comentario":{ "$size": 1 }}).sort("publicacao.datapub")
    client.close()
    
if __name__ == '__main__':
    import timeit
    print(timeit.repeat(stmt="searchComplex()", setup="from __main__ import searchComplex", repeat=3, number=100000 ))
