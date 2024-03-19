-- Table: app.jsonic

-- DROP TABLE IF EXISTS app.jsonic;

CREATE TABLE IF NOT EXISTS app.jsonic
(
    id integer NOT NULL DEFAULT nextval('app.jsonic_id_seq'::regclass),
    payload jsonb NOT NULL,
    CONSTRAINT jsonic_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS app.jsonic
    OWNER to app_user;