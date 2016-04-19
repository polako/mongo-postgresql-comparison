CREATE TABLE testesc.usuario_grupo
(
  id_usuario_grupo serial NOT NULL,
  nome character varying(255),
  ativo boolean,
  CONSTRAINT usuario_grupo_pkey PRIMARY KEY (id_usuario_grupo)
)
;
CREATE TABLE testesc.usuario
(
  id_usuario serial NOT NULL,
  nome character varying(255),
  senha character varying(255),
  datanascimento date,
  sobre character varying(255),
  ativo boolean,
  id_grupo integer,
  CONSTRAINT usuario_pkey PRIMARY KEY (id_usuario),
  CONSTRAINT usuario_id_grupo_fkey FOREIGN KEY (id_grupo)
      REFERENCES testesc.usuario_grupo (id_usuario_grupo) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
;
CREATE TABLE testesc.pub_tipo
(
  id_pub_tipo serial NOT NULL,
  nome character varying(255),
  CONSTRAINT pub_tipo_pkey PRIMARY KEY (id_pub_tipo)
)
;
CREATE TABLE testesc.publicacao
(
  id_publicacao serial NOT NULL,
  titulo character varying(255),
  datapub date,
  conteudo character varying(20000), 
  id_usuario integer,
  id_pub_tipo integer,
  CONSTRAINT publicacao_pkey PRIMARY KEY (id_publicacao),
  CONSTRAINT publicacao_id_usuario_fkey FOREIGN KEY (id_usuario)
      REFERENCES testesc.usuario (id_usuario) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT publication_tipo_fkey FOREIGN KEY (id_pub_tipo)
      REFERENCES testesc.pub_tipo (id_pub_tipo) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
;
CREATE TABLE testesc.comentario
(
  id_comentario serial NOT NULL,
  nome character varying(255),
  email character varying(255),
  datapub date, -- 
  conteudo character varying(1000),
  publicacao integer,
  CONSTRAINT comentario_pkey PRIMARY KEY (id_comentario),
  CONSTRAINT comentario_publicacao_fkey FOREIGN KEY (publicacao)
      REFERENCES testesc.publicacao (id_publicacao) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)

