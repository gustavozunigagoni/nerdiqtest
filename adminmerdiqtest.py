# Aplicacion que tiene funciones administrativas y de inicializacion de sistema

import config as cf
from database import dbproc

def initdb():
    # Cracion de tabla de usuarios
    script= """
 -- Table: public.users

-- Table: public.users

DROP TABLE IF EXISTS public.users;

CREATE TABLE IF NOT EXISTS public.users
(
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    email character varying(255) COLLATE pg_catalog."default" NOT NULL,
    nombre character varying(255) COLLATE pg_catalog."default" NOT NULL,
    estado smallint NOT NULL,
    created_date timestamp without time zone,
    update_date timestamp without time zone,
    rol smallint,
    password character varying(255) COLLATE pg_catalog."default",
    token character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT users_pkey PRIMARY KEY (id),
    CONSTRAINT users_email_key UNIQUE (email)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users
    OWNER to posgres;
-- Index: idx_email

-- DROP INDEX IF EXISTS public.idx_email;

CREATE INDEX IF NOT EXISTS idx_email
    ON public.users USING btree
    (email COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
    """

    resultado = dbproc.dbexec("Creacion de tabla de users",script)

    script= f"""

INSERT INTO public.users(
	email, nombre, estado, rol, password)
	VALUES ('{cf.user_admin}', 'Admin', 1, 1, '{cf.encriptar_password(cf.user_pass)}');

"""
    resultado = dbproc.dbexec("Creacion de usuario administrativo de nerdiqtest",script)


if __name__ == "__main__":
    initdb()







