--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4 (Ubuntu 12.4-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: catalogs; Type: TABLE; Schema: public; Owner: mrkrap
--

CREATE TABLE public.catalogs (
    id integer NOT NULL,
    name character varying(255)
);


ALTER TABLE public.catalogs OWNER TO mrkrap;

--
-- Name: catalogs_id_seq; Type: SEQUENCE; Schema: public; Owner: mrkrap
--

CREATE SEQUENCE public.catalogs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.catalogs_id_seq OWNER TO mrkrap;

--
-- Name: catalogs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mrkrap
--

ALTER SEQUENCE public.catalogs_id_seq OWNED BY public.catalogs.id;


--
-- Name: discounts; Type: TABLE; Schema: public; Owner: mrkrap
--

CREATE TABLE public.discounts (
    id integer NOT NULL,
    user_id integer,
    product_id integer,
    discount double precision,
    started_at date,
    finished_at date,
    created_at date DEFAULT CURRENT_TIMESTAMP,
    updated_at date DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.discounts OWNER TO mrkrap;

--
-- Name: discounts_id_seq; Type: SEQUENCE; Schema: public; Owner: mrkrap
--

CREATE SEQUENCE public.discounts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.discounts_id_seq OWNER TO mrkrap;

--
-- Name: discounts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mrkrap
--

ALTER SEQUENCE public.discounts_id_seq OWNED BY public.discounts.id;


--
-- Name: orders; Type: TABLE; Schema: public; Owner: mrkrap
--

CREATE TABLE public.orders (
    id integer NOT NULL,
    user_id integer,
    created_at date DEFAULT CURRENT_TIMESTAMP,
    updated_at date DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.orders OWNER TO mrkrap;

--
-- Name: orders_id_seq; Type: SEQUENCE; Schema: public; Owner: mrkrap
--

CREATE SEQUENCE public.orders_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.orders_id_seq OWNER TO mrkrap;

--
-- Name: orders_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mrkrap
--

ALTER SEQUENCE public.orders_id_seq OWNED BY public.orders.id;


--
-- Name: orders_products; Type: TABLE; Schema: public; Owner: mrkrap
--

CREATE TABLE public.orders_products (
    id integer NOT NULL,
    order_id integer,
    product_id integer,
    total integer DEFAULT 1,
    created_at date DEFAULT CURRENT_TIMESTAMP,
    updated_at date DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.orders_products OWNER TO mrkrap;

--
-- Name: orders_products_id_seq; Type: SEQUENCE; Schema: public; Owner: mrkrap
--

CREATE SEQUENCE public.orders_products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.orders_products_id_seq OWNER TO mrkrap;

--
-- Name: orders_products_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mrkrap
--

ALTER SEQUENCE public.orders_products_id_seq OWNED BY public.orders_products.id;


--
-- Name: products; Type: TABLE; Schema: public; Owner: mrkrap
--

CREATE TABLE public.products (
    id integer NOT NULL,
    name character varying(255),
    description text,
    price numeric(11,2),
    catalog_id integer,
    created_at date DEFAULT CURRENT_TIMESTAMP,
    updated_at date DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.products OWNER TO mrkrap;

--
-- Name: products_id_seq; Type: SEQUENCE; Schema: public; Owner: mrkrap
--

CREATE SEQUENCE public.products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_id_seq OWNER TO mrkrap;

--
-- Name: products_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mrkrap
--

ALTER SEQUENCE public.products_id_seq OWNED BY public.products.id;


--
-- Name: storehouses; Type: TABLE; Schema: public; Owner: mrkrap
--

CREATE TABLE public.storehouses (
    id integer NOT NULL,
    name character varying(255),
    created_at date DEFAULT CURRENT_TIMESTAMP,
    updated_at date DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.storehouses OWNER TO mrkrap;

--
-- Name: storehouses_id_seq; Type: SEQUENCE; Schema: public; Owner: mrkrap
--

CREATE SEQUENCE public.storehouses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.storehouses_id_seq OWNER TO mrkrap;

--
-- Name: storehouses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mrkrap
--

ALTER SEQUENCE public.storehouses_id_seq OWNED BY public.storehouses.id;


--
-- Name: storehouses_products; Type: TABLE; Schema: public; Owner: mrkrap
--

CREATE TABLE public.storehouses_products (
    id integer NOT NULL,
    storehouse_id integer,
    product_id integer,
    value integer,
    created_at date DEFAULT CURRENT_TIMESTAMP,
    updated_at date DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.storehouses_products OWNER TO mrkrap;

--
-- Name: storehouses_products_id_seq; Type: SEQUENCE; Schema: public; Owner: mrkrap
--

CREATE SEQUENCE public.storehouses_products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.storehouses_products_id_seq OWNER TO mrkrap;

--
-- Name: storehouses_products_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mrkrap
--

ALTER SEQUENCE public.storehouses_products_id_seq OWNED BY public.storehouses_products.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: mrkrap
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying(255),
    birthday_at date,
    created_at date DEFAULT CURRENT_TIMESTAMP,
    updated_at date DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.users OWNER TO mrkrap;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: mrkrap
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO mrkrap;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mrkrap
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: catalogs id; Type: DEFAULT; Schema: public; Owner: mrkrap
--

ALTER TABLE ONLY public.catalogs ALTER COLUMN id SET DEFAULT nextval('public.catalogs_id_seq'::regclass);


--
-- Name: discounts id; Type: DEFAULT; Schema: public; Owner: mrkrap
--

ALTER TABLE ONLY public.discounts ALTER COLUMN id SET DEFAULT nextval('public.discounts_id_seq'::regclass);


--
-- Name: orders id; Type: DEFAULT; Schema: public; Owner: mrkrap
--

ALTER TABLE ONLY public.orders ALTER COLUMN id SET DEFAULT nextval('public.orders_id_seq'::regclass);


--
-- Name: orders_products id; Type: DEFAULT; Schema: public; Owner: mrkrap
--

ALTER TABLE ONLY public.orders_products ALTER COLUMN id SET DEFAULT nextval('public.orders_products_id_seq'::regclass);


--
-- Name: products id; Type: DEFAULT; Schema: public; Owner: mrkrap
--

ALTER TABLE ONLY public.products ALTER COLUMN id SET DEFAULT nextval('public.products_id_seq'::regclass);


--
-- Name: storehouses id; Type: DEFAULT; Schema: public; Owner: mrkrap
--

ALTER TABLE ONLY public.storehouses ALTER COLUMN id SET DEFAULT nextval('public.storehouses_id_seq'::regclass);


--
-- Name: storehouses_products id; Type: DEFAULT; Schema: public; Owner: mrkrap
--

ALTER TABLE ONLY public.storehouses_products ALTER COLUMN id SET DEFAULT nextval('public.storehouses_products_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: mrkrap
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: catalogs; Type: TABLE DATA; Schema: public; Owner: mrkrap
--

COPY public.catalogs (id, name) FROM stdin;
1	Процессоры
2	Материнские платы
3	Видеокарты
4	Жесткие диски
5	Оперативная память
\.


--
-- Data for Name: discounts; Type: TABLE DATA; Schema: public; Owner: mrkrap
--

COPY public.discounts (id, user_id, product_id, discount, started_at, finished_at, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: mrkrap
--

COPY public.orders (id, user_id, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: orders_products; Type: TABLE DATA; Schema: public; Owner: mrkrap
--

COPY public.orders_products (id, order_id, product_id, total, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: mrkrap
--

COPY public.products (id, name, description, price, catalog_id, created_at, updated_at) FROM stdin;
1	Intel Core i3-8100	Процессор для настольных персональных компьютеров, основанных на платформе Intel.	7890.00	1	2021-08-08	2021-08-08
2	Intel Core i5-7400	Процессор для настольных персональных компьютеров, основанных на платформе Intel.	12700.00	1	2021-08-08	2021-08-08
3	AMD FX-8320E	Процессор для настольных персональных компьютеров, основанных на платформе AMD.	4780.00	1	2021-08-08	2021-08-08
4	AMD FX-8320	Процессор для настольных персональных компьютеров, основанных на платформе AMD.	7120.00	1	2021-08-08	2021-08-08
5	ASUS ROG MAXIMUS X HERO	Материнская плата ASUS ROG MAXIMUS X HERO, Z370, Socket 1151-V2, DDR4, ATX	19310.00	2	2021-08-08	2021-08-08
6	Gigabyte H310M S2H	Материнская плата Gigabyte H310M S2H, H310, Socket 1151-V2, DDR4, mATX	4790.00	2	2021-08-08	2021-08-08
7	MSI B250M GAMING PRO	Материнская плата MSI B250M GAMING PRO, B250, Socket 1151, DDR4, mATX	5060.00	2	2021-08-08	2021-08-08
\.


--
-- Data for Name: storehouses; Type: TABLE DATA; Schema: public; Owner: mrkrap
--

COPY public.storehouses (id, name, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: storehouses_products; Type: TABLE DATA; Schema: public; Owner: mrkrap
--

COPY public.storehouses_products (id, storehouse_id, product_id, value, created_at, updated_at) FROM stdin;
1	\N	\N	0	2021-08-08	2021-08-08
2	\N	\N	2500	2021-08-08	2021-08-08
3	\N	\N	0	2021-08-08	2021-08-08
4	\N	\N	30	2021-08-08	2021-08-08
5	\N	\N	500	2021-08-08	2021-08-08
6	\N	\N	1	2021-08-08	2021-08-08
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: mrkrap
--

COPY public.users (id, name, birthday_at, created_at, updated_at) FROM stdin;
1	Геннадий	1990-10-05	2021-08-08	2021-08-08
2	Наталья	1984-11-12	2021-08-08	2021-08-08
3	Александр	1985-05-20	2021-08-08	2021-08-08
4	Сергей	1988-02-14	2021-08-08	2021-08-08
5	Иван	1998-01-12	2021-08-08	2021-08-08
6	Мария	1992-08-29	2021-08-08	2021-08-08
\.


--
-- Name: catalogs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mrkrap
--

SELECT pg_catalog.setval('public.catalogs_id_seq', 5, true);


--
-- Name: discounts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mrkrap
--

SELECT pg_catalog.setval('public.discounts_id_seq', 1, false);


--
-- Name: orders_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mrkrap
--

SELECT pg_catalog.setval('public.orders_id_seq', 1, false);


--
-- Name: orders_products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mrkrap
--

SELECT pg_catalog.setval('public.orders_products_id_seq', 1, false);


--
-- Name: products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mrkrap
--

SELECT pg_catalog.setval('public.products_id_seq', 7, true);


--
-- Name: storehouses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mrkrap
--

SELECT pg_catalog.setval('public.storehouses_id_seq', 1, false);


--
-- Name: storehouses_products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mrkrap
--

SELECT pg_catalog.setval('public.storehouses_products_id_seq', 6, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mrkrap
--

SELECT pg_catalog.setval('public.users_id_seq', 6, true);


--
-- Name: catalogs catalogs_pkey; Type: CONSTRAINT; Schema: public; Owner: mrkrap
--

ALTER TABLE ONLY public.catalogs
    ADD CONSTRAINT catalogs_pkey PRIMARY KEY (id);


--
-- Name: discounts discounts_pkey; Type: CONSTRAINT; Schema: public; Owner: mrkrap
--

ALTER TABLE ONLY public.discounts
    ADD CONSTRAINT discounts_pkey PRIMARY KEY (id);


--
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: public; Owner: mrkrap
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (id);


--
-- Name: orders_products orders_products_pkey; Type: CONSTRAINT; Schema: public; Owner: mrkrap
--

ALTER TABLE ONLY public.orders_products
    ADD CONSTRAINT orders_products_pkey PRIMARY KEY (id);


--
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: mrkrap
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id);


--
-- Name: storehouses storehouses_pkey; Type: CONSTRAINT; Schema: public; Owner: mrkrap
--

ALTER TABLE ONLY public.storehouses
    ADD CONSTRAINT storehouses_pkey PRIMARY KEY (id);


--
-- Name: storehouses_products storehouses_products_pkey; Type: CONSTRAINT; Schema: public; Owner: mrkrap
--

ALTER TABLE ONLY public.storehouses_products
    ADD CONSTRAINT storehouses_products_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: mrkrap
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

