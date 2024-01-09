# Sentencias para generar las tablas necesarias para la base de datos y  valores por defecto de algunas tablas 

```sql
-- public.status definition

-- Drop table

-- DROP TABLE public.status;

CREATE TABLE public.status (
	id int4 NOT NULL,
	nombre varchar NOT NULL,
	CONSTRAINT status_pk PRIMARY KEY (id)
);

-- Permissions

ALTER TABLE public.status OWNER TO desarrollo;
GRANT ALL ON TABLE public.status TO desarrollo;


-- public.autores definition

-- Drop table

-- DROP TABLE public.autores;

CREATE TABLE public.autores (
	id varchar NOT NULL,
	nombre varchar NOT NULL,
	apellido varchar NOT NULL,
	cantidad_libros int4 NULL,
	CONSTRAINT autores_pk PRIMARY KEY (id)
);

-- Permissions

ALTER TABLE public.autores OWNER TO desarrollo;
GRANT ALL ON TABLE public.autores TO desarrollo;


-- public.editoriales definition

-- Drop table

-- DROP TABLE public.editoriales;

CREATE TABLE public.editoriales (
	id varchar NOT NULL,
	nombre varchar NOT NULL,
	CONSTRAINT editoriales_pk PRIMARY KEY (id)
);

-- Permissions

ALTER TABLE public.editoriales OWNER TO desarrollo;
GRANT ALL ON TABLE public.editoriales TO desarrollo;


-- public.tipos_usuarios definition

-- Drop table

-- DROP TABLE public.tipos_usuarios;

CREATE TABLE public.tipos_usuarios (
	id int4 NOT NULL,
	nombre varchar NOT NULL,
	descripcion varchar NULL,
	CONSTRAINT tipos_usuarios_pk PRIMARY KEY (id)
);

-- Permissions

ALTER TABLE public.tipos_usuarios OWNER TO desarrollo;
GRANT ALL ON TABLE public.tipos_usuarios TO desarrollo;


-- public.categorias definition

-- Drop table

-- DROP TABLE public.categorias;

CREATE TABLE public.categorias (
	id int4 NOT NULL,
	nombre varchar NULL,
	CONSTRAINT categorias_pk PRIMARY KEY (id)
);

-- Permissions

ALTER TABLE public.categorias OWNER TO desarrollo;
GRANT ALL ON TABLE public.categorias TO desarrollo;


-- public."user" definition

-- Drop table

-- DROP TABLE public."user";

CREATE TABLE public."user" (
	ci varchar NOT NULL,
	nombre varchar NULL,
	apellido varchar NULL,
	correo varchar NULL,
	tlf varchar NULL,
	foto_perfil varchar NULL,
	id_tipo_user int4 NOT NULL,
	user_name varchar NOT NULL,
	"password" varchar NOT NULL,
	"token" varchar NULL,
	id_status varchar NOT NULL,
	CONSTRAINT user_pk PRIMARY KEY (ci),
	CONSTRAINT user_fk FOREIGN KEY (id_tipo_user) REFERENCES public.tipos_usuarios(id)
);

-- Permissions

ALTER TABLE public."user" OWNER TO desarrollo;
GRANT ALL ON TABLE public."user" TO desarrollo;


-- public.libros definition

-- Drop table

-- DROP TABLE public.libros;

CREATE TABLE public.libros (
	id varchar NOT NULL,
	titulo varchar NOT NULL,
	id_autor varchar NULL,
	id_categoria int4 NULL,
	id_status int4 NULL,
	f_publicacion timestamp NOT NULL,
	id_user_publish varchar NULL,
	id_editorial varchar NOT NULL,
	descargas int8 NULL,
	archivo_nombre varchar NOT NULL,
	CONSTRAINT libros_pk PRIMARY KEY (id),
	CONSTRAINT libros_un UNIQUE (archivo_nombre),
	CONSTRAINT libros_fk FOREIGN KEY (id_status) REFERENCES public.status(id),
	CONSTRAINT libros_fk_autor FOREIGN KEY (id_autor) REFERENCES public.autores(id),
	CONSTRAINT libros_fk_categorias FOREIGN KEY (id_categoria) REFERENCES public.categorias(id),
	CONSTRAINT libros_fk_editorial FOREIGN KEY (id_editorial) REFERENCES public.editoriales(id),
	CONSTRAINT libros_fk_user_publish FOREIGN KEY (id_user_publish) REFERENCES public."user"(ci)
);

-- Permissions

ALTER TABLE public.libros OWNER TO desarrollo;
GRANT ALL ON TABLE public.libros TO desarrollo;


-- public.reacciones definition

-- Drop table

-- DROP TABLE public.reacciones;

CREATE TABLE public.reacciones (
	id_libro varchar NOT NULL,
	id_user varchar NOT NULL,
	fecha timestamp NULL,
	CONSTRAINT reacciones_fk FOREIGN KEY (id_user) REFERENCES public."user"(ci),
	CONSTRAINT reacciones_fk_libros FOREIGN KEY (id_libro) REFERENCES public.libros(id)
);

-- Permissions

ALTER TABLE public.reacciones OWNER TO desarrollo;
GRANT ALL ON TABLE public.reacciones TO desarrollo;
/**********************
 * valoreds de status *
 **********************/
INSERT INTO public.status (id, nombre) VALUES(1, 'activo');
INSERT INTO public.status (id, nombre) VALUES(2, 'inactivo');
INSERT INTO public.status (id, nombre) VALUES(3, 'bajo revision');
INSERT INTO public.status (id, nombre) VALUES(4, 'declinado');


/****************************
 * valoreds de tipos_usuario*
 ****************************/
INSERT INTO public.tipos_usuarios (id, nombre, descripcion) VALUES(1, 'Estudiante', NULL);
INSERT INTO public.tipos_usuarios (id, nombre, descripcion) VALUES(2, 'Profesor', NULL);
INSERT INTO public.tipos_usuarios (id, nombre, descripcion) VALUES(3, 'Super Usuario', NULL);

```