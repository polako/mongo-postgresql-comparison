#-*- utf-8 -*-
import psycopg2
import datetime
      
def insert():   
    # Connect to an existing database
    conn = psycopg2.connect("dbname=testedb user=teste" )
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Pass data to fill a query placeholders and let Psycopg perform
    # the correct conversion (no more SQL injections!)    
    cur.execute("INSERT INTO testesc.usuario_grupo (nome, ativo) VALUES (%s, %s)", ("Administracao", True))    
    cur.execute("INSERT INTO testesc.usuario (nome, senha, datanascimento, sobre, ativo, id_grupo) VALUES (%s, %s, %s, %s, %s, %s)", ("Cristiano Politowski", "admin123", "1987-10-27", "Pesquisador e programador nas horas vagas.", "true",0))
    cur.execute("INSERT INTO testesc.pub_tipo (nome) VALUES (%s)", ("Novidade",))
    cur.execute("INSERT INTO testesc.publicacao (titulo, datapub, conteudo, id_usuario, id_pub_tipo) VALUES (%s, %s, %s, %s, %s)", ("Publicacao teste", datetime.datetime.utcnow(), "Bla bla bla...", 0, 0))
    cur.execute("INSERT INTO testesc.comentario (nome, email, datapub, conteudo, id_publicacao) VALUES (%s, %s, %s, %s, %s)", ("Fulano de Tal", "fulano@gmail.com", datetime.datetime.utcnow(), "First!", 0))    
    # Make the changes to the database persistent
    conn.commit()
    # Close communication with the database
    cur.close()
    conn.close()
    
def searchSimple():
    conn = psycopg2.connect("dbname=testedb user=teste" )
    cur = conn.cursor()
    cur.execute("SELECT * FROM testesc.publicacao WHERE testesc.publicacao.titulo LIKE 'Publicacao teste'")
    #print len(cur.fetchall())    
    cur.close()
    conn.close()
    
def searchComplex():
    conn = psycopg2.connect("dbname=testedb user=teste" )
    cur = conn.cursor()
    cur.execute("SELECT * FROM testesc.publicacao p, testesc.usuario u, testesc.usuario_grupo ug, testesc.pub_tipo pt,       testesc.comentario c WHERE p.id_usuario = u.id_usuario AND u.id_grupo = ug.id_usuario_grupo AND p.id_pub_tipo = pt.id_pub_tipo AND c.id_publicacao = p.id_publicacao AND p.datapub > %s AND p.datapub < %s AND pt.nome LIKE %s AND u.datanascimento > %s AND u.ativo = %s AND ug.nome = %s AND (SELECT count(*) FROM testesc.publicacao p, testesc.comentario c WHERE c.id_publicacao = p.id_publicacao ) >= 1 ORDER BY p.datapub" , (datetime.datetime(2013, 11, 12, 12), datetime.datetime(2015, 11, 12, 12), "Novidade", "1980-1-1", "True", "Administracao"))
    #print len(cur.fetchall())    
    cur.close()
    conn.close()   

if __name__ == '__main__':
    import timeit
    print(timeit.repeat(stmt="searchComplex()", setup="from __main__ import searchComplex", repeat=3, number=1000))
