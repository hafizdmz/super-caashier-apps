-- This script was generated by the ERD tool in pgAdmin 4.
-- Please log an issue at https://redmine.postgresql.org/projects/pgadmin4/issues/new if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE IF NOT EXISTS public.transactions
(
    trans_id integer NOT NULL DEFAULT nextval('transactions_trans_id_seq'::regclass),
    item_name character varying COLLATE pg_catalog."default",
    item_qty integer,
    item_price integer,
    total_price integer,
    discount integer,
    disc_price integer,
    CONSTRAINT transactions_pkey PRIMARY KEY (trans_id)
);
END;