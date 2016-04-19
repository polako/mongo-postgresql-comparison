--todas as publicacoes entre a data X e Y que sejam do tipo Novidade de usuarios 
--nascidos apartir de XX que estejam ativos e que possua mais de 1 comentario ordenado por data
SELECT * FROM testesc.publicacao p,
testesc.usuario u, 
testesc.usuario_grupo ug, 
testesc.pub_tipo pt,
testesc.comentario c
WHERE 
p.id_usuario = u.id_usuario 
AND u.id_grupo = ug.id_usuario_grupo
AND p.id_pub_tipo = pt.id_pub_tipo
AND c.id_publicacao = p.id_publicacao
AND p.datapub > '1999-01-01' 
AND p.datapub < '2015-01-22'
AND pt.nome LIKE 'Tipo-teste'
AND u.datanascimento > '1980-10-27'
AND u.ativo = true
AND ug.nome = 'Teste'
AND (SELECT count(*) FROM testesc.publicacao p, testesc.comentario c
WHERE c.id_publicacao = p.id_publicacao ) >= 1
ORDER BY p.datapub


