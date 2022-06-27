--
-- PostgreSQL database dump
--

-- Dumped from database version 13.6 (Debian 13.6-1.pgdg110+1)
-- Dumped by pg_dump version 13.6 (Debian 13.6-1.pgdg110+1)

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

--
-- Name: geostore; Type: SCHEMA; Schema: -; Owner: geostore
--

CREATE USER geostore with password 'geostore';

CREATE SCHEMA geostore;


ALTER SCHEMA geostore OWNER TO geostore;

--
-- Name: geostore_test; Type: SCHEMA; Schema: -; Owner: geostore
--

CREATE SCHEMA geostore_test;


ALTER SCHEMA geostore_test OWNER TO geostore;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: gs_attribute; Type: TABLE; Schema: geostore; Owner: geostore
--

CREATE TABLE geostore.gs_attribute (
    id bigint NOT NULL,
    attribute_date timestamp without time zone,
    name character varying(255) NOT NULL,
    attribute_number double precision,
    attribute_text character varying(255),
    attribute_type character varying(255) NOT NULL,
    resource_id bigint NOT NULL
);


ALTER TABLE geostore.gs_attribute OWNER TO geostore;

--
-- Name: gs_category; Type: TABLE; Schema: geostore; Owner: geostore
--

CREATE TABLE geostore.gs_category (
    id bigint NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE geostore.gs_category OWNER TO geostore;

--
-- Name: gs_resource; Type: TABLE; Schema: geostore; Owner: geostore
--

CREATE TABLE geostore.gs_resource (
    id bigint NOT NULL,
    creation timestamp without time zone NOT NULL,
    description character varying(10000),
    lastupdate timestamp without time zone,
    metadata character varying(30000),
    name character varying(255) NOT NULL,
    category_id bigint NOT NULL
);


ALTER TABLE geostore.gs_resource OWNER TO geostore;

--
-- Name: gs_security; Type: TABLE; Schema: geostore; Owner: geostore
--

CREATE TABLE geostore.gs_security (
    id bigint NOT NULL,
    canread boolean NOT NULL,
    canwrite boolean NOT NULL,
    group_id bigint,
    resource_id bigint,
    user_id bigint,
    username character varying(255),
    groupname character varying(255)
);


ALTER TABLE geostore.gs_security OWNER TO geostore;

--
-- Name: gs_stored_data; Type: TABLE; Schema: geostore; Owner: geostore
--

CREATE TABLE geostore.gs_stored_data (
    id bigint NOT NULL,
    stored_data character varying(10000000) NOT NULL,
    resource_id bigint NOT NULL
);


ALTER TABLE geostore.gs_stored_data OWNER TO geostore;

--
-- Name: gs_user; Type: TABLE; Schema: geostore; Owner: geostore
--

CREATE TABLE geostore.gs_user (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    user_password character varying(255),
    user_role character varying(255) NOT NULL,
    group_id bigint,
    enabled character(1) DEFAULT 'Y'::bpchar NOT NULL
);


ALTER TABLE geostore.gs_user OWNER TO geostore;

--
-- Name: gs_user_attribute; Type: TABLE; Schema: geostore; Owner: geostore
--

CREATE TABLE geostore.gs_user_attribute (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    string character varying(255),
    user_id bigint NOT NULL
);


ALTER TABLE geostore.gs_user_attribute OWNER TO geostore;

--
-- Name: gs_usergroup; Type: TABLE; Schema: geostore; Owner: geostore
--

CREATE TABLE geostore.gs_usergroup (
    id bigint NOT NULL,
    groupname character varying(255) NOT NULL,
    description character varying(255),
    enabled character(1) DEFAULT 'Y'::bpchar NOT NULL
);


ALTER TABLE geostore.gs_usergroup OWNER TO geostore;

--
-- Name: gs_usergroup_members; Type: TABLE; Schema: geostore; Owner: geostore
--

CREATE TABLE geostore.gs_usergroup_members (
    user_id bigint NOT NULL,
    group_id bigint NOT NULL
);


ALTER TABLE geostore.gs_usergroup_members OWNER TO geostore;

--
-- Name: hibernate_sequence; Type: SEQUENCE; Schema: geostore; Owner: geostore
--

CREATE SEQUENCE geostore.hibernate_sequence
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE geostore.hibernate_sequence OWNER TO geostore;

--
-- Name: gs_attribute; Type: TABLE; Schema: geostore_test; Owner: geostore
--

CREATE TABLE geostore_test.gs_attribute (
    id bigint NOT NULL,
    attribute_date timestamp without time zone,
    name character varying(255) NOT NULL,
    attribute_number double precision,
    attribute_text character varying(255),
    attribute_type character varying(255) NOT NULL,
    resource_id bigint NOT NULL
);


ALTER TABLE geostore_test.gs_attribute OWNER TO geostore;

--
-- Name: gs_category; Type: TABLE; Schema: geostore_test; Owner: geostore
--

CREATE TABLE geostore_test.gs_category (
    id bigint NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE geostore_test.gs_category OWNER TO geostore;

--
-- Name: gs_resource; Type: TABLE; Schema: geostore_test; Owner: geostore
--

CREATE TABLE geostore_test.gs_resource (
    id bigint NOT NULL,
    creation timestamp without time zone NOT NULL,
    description character varying(10000),
    lastupdate timestamp without time zone,
    metadata character varying(30000),
    name character varying(255) NOT NULL,
    category_id bigint NOT NULL
);


ALTER TABLE geostore_test.gs_resource OWNER TO geostore;

--
-- Name: gs_security; Type: TABLE; Schema: geostore_test; Owner: geostore
--

CREATE TABLE geostore_test.gs_security (
    id bigint NOT NULL,
    canread boolean NOT NULL,
    canwrite boolean NOT NULL,
    group_id bigint,
    resource_id bigint,
    user_id bigint,
    username character varying(255),
    groupname character varying(255)
);


ALTER TABLE geostore_test.gs_security OWNER TO geostore;

--
-- Name: gs_stored_data; Type: TABLE; Schema: geostore_test; Owner: geostore
--

CREATE TABLE geostore_test.gs_stored_data (
    id bigint NOT NULL,
    stored_data character varying(10000000) NOT NULL,
    resource_id bigint NOT NULL
);


ALTER TABLE geostore_test.gs_stored_data OWNER TO geostore;

--
-- Name: gs_user; Type: TABLE; Schema: geostore_test; Owner: geostore
--

CREATE TABLE geostore_test.gs_user (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    user_password character varying(255),
    user_role character varying(255) NOT NULL,
    group_id bigint,
    enabled character(1) DEFAULT 'Y'::bpchar NOT NULL
);


ALTER TABLE geostore_test.gs_user OWNER TO geostore;

--
-- Name: gs_user_attribute; Type: TABLE; Schema: geostore_test; Owner: geostore
--

CREATE TABLE geostore_test.gs_user_attribute (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    string character varying(255),
    user_id bigint NOT NULL
);


ALTER TABLE geostore_test.gs_user_attribute OWNER TO geostore;

--
-- Name: gs_usergroup; Type: TABLE; Schema: geostore_test; Owner: geostore
--

CREATE TABLE geostore_test.gs_usergroup (
    id bigint NOT NULL,
    groupname character varying(255) NOT NULL,
    description character varying(255),
    enabled character(1) DEFAULT 'Y'::bpchar NOT NULL
);


ALTER TABLE geostore_test.gs_usergroup OWNER TO geostore;

--
-- Name: gs_usergroup_members; Type: TABLE; Schema: geostore_test; Owner: geostore
--

CREATE TABLE geostore_test.gs_usergroup_members (
    user_id bigint NOT NULL,
    group_id bigint NOT NULL
);


ALTER TABLE geostore_test.gs_usergroup_members OWNER TO geostore;

--
-- Name: hibernate_sequence; Type: SEQUENCE; Schema: geostore_test; Owner: geostore
--

CREATE SEQUENCE geostore_test.hibernate_sequence
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE geostore_test.hibernate_sequence OWNER TO geostore;


--
-- Data for Name: gs_attribute; Type: TABLE DATA; Schema: geostore; Owner: geostore
--

INSERT INTO geostore.gs_attribute VALUES (15, NULL, 'attributes', NULL, 'null', 'STRING', 14);
INSERT INTO geostore.gs_attribute VALUES (19, NULL, 'detailsSettings', NULL, '{}', 'STRING', 14);
INSERT INTO geostore.gs_attribute VALUES (32, NULL, 'thumbnail', NULL, 'rest/geostore/data/51/raw?decode=datauri&v=0822fda0-2b24-11eb-aefb-452dad1e3676', 'STRING', 14);
INSERT INTO geostore.gs_attribute VALUES (122, NULL, 'attributes', NULL, 'null', 'STRING', 121);
INSERT INTO geostore.gs_attribute VALUES (126, NULL, 'detailsSettings', NULL, '{}', 'STRING', 121);
INSERT INTO geostore.gs_attribute VALUES (246, NULL, 'attributes', NULL, 'null', 'STRING', 245);
INSERT INTO geostore.gs_attribute VALUES (249, NULL, 'detailsSettings', NULL, '{}', 'STRING', 245);


--
-- Data for Name: gs_category; Type: TABLE DATA; Schema: geostore; Owner: geostore
--

INSERT INTO geostore.gs_category VALUES (1, 'MAP');
INSERT INTO geostore.gs_category VALUES (2, 'THUMBNAIL');
INSERT INTO geostore.gs_category VALUES (3, 'DETAILS');
INSERT INTO geostore.gs_category VALUES (4, 'DASHBOARD');
INSERT INTO geostore.gs_category VALUES (5, 'GEOSTORY');
INSERT INTO geostore.gs_category VALUES (6, 'CONTEXT');
INSERT INTO geostore.gs_category VALUES (7, 'TEMPLATE');
INSERT INTO geostore.gs_category VALUES (8, 'USERSESSION');


--
-- Data for Name: gs_resource; Type: TABLE DATA; Schema: geostore; Owner: geostore
--

INSERT INTO geostore.gs_resource VALUES (51, '2020-11-20 11:32:15.023', '', NULL, '', '14-thumbnail-09774300-2b24-11eb-aefb-452dad1e3676', 2);
INSERT INTO geostore.gs_resource VALUES (26, '2020-11-14 15:22:18.147', '', '2020-11-20 11:32:15.022', '', '14-thumbnail-2e4b8ec0-268d-11eb-97f9-87bf3899a797', 2);
INSERT INTO geostore.gs_resource VALUES (121, '2021-01-31 17:53:51.673', 'Amministrazione Infrastruttura Cartografica City Capitale', '2021-10-15 14:08:20.635', '', 'GeoCity Admin', 1);
INSERT INTO geostore.gs_resource VALUES (245, '2021-04-29 06:24:06.886', '', '2021-10-15 14:09:09.827', '', 'CTC1000', 1);
INSERT INTO geostore.gs_resource VALUES (14, '2020-11-14 07:54:14.936', 'Infrastruttura Cartografica di City Capitale', '2022-03-05 21:37:04.927', '', 'GeoCity', 1);


--
-- Data for Name: gs_security; Type: TABLE DATA; Schema: geostore; Owner: geostore
--

INSERT INTO geostore.gs_security VALUES (45, true, true, NULL, 26, 12, NULL, NULL);
INSERT INTO geostore.gs_security VALUES (46, true, false, 9, 26, NULL, NULL, NULL);
INSERT INTO geostore.gs_security VALUES (385, true, true, NULL, 121, 12, NULL, NULL);
INSERT INTO geostore.gs_security VALUES (391, true, true, NULL, 245, 12, NULL, NULL);
INSERT INTO geostore.gs_security VALUES (1877, true, true, NULL, 51, 12, NULL, NULL);
INSERT INTO geostore.gs_security VALUES (1879, true, false, 9, 51, NULL, NULL, NULL);
INSERT INTO geostore.gs_security VALUES (1880, true, true, NULL, 14, 12, NULL, NULL);
INSERT INTO geostore.gs_security VALUES (1881, true, false, 9, 14, NULL, NULL, NULL);


--
-- Data for Name: gs_stored_data; Type: TABLE DATA; Schema: geostore; Owner: geostore
--


--
-- Data for Name: gs_user; Type: TABLE DATA; Schema: geostore; Owner: geostore
--

INSERT INTO geostore.gs_user VALUES (11, 'guest', NULL, 'GUEST', NULL, 'Y');
INSERT INTO geostore.gs_user VALUES (13, 'user', NULL, 'USER', NULL, 'Y');
INSERT INTO geostore.gs_user VALUES (293, 'STF.MRR', NULL, 'ADMIN', NULL, 'Y');
INSERT INTO geostore.gs_user VALUES (304, 'BRT.FNC', NULL, 'USER', NULL, 'Y');
INSERT INTO geostore.gs_user VALUES (12, 'admin', NULL, 'ADMIN', NULL, 'Y');
INSERT INTO geostore.gs_user VALUES (636, 'wso2.test', NULL, 'USER', NULL, 'Y');
INSERT INTO geostore.gs_user VALUES (763, 'ndr.qtrn', NULL, 'USER', NULL, 'Y');
INSERT INTO geostore.gs_user VALUES (773, 'QTR.NDR', NULL, 'USER', NULL, 'Y');
INSERT INTO geostore.gs_user VALUES (835, 'MTT.SRA', NULL, 'USER', NULL, 'Y');
INSERT INTO geostore.gs_user VALUES (935, 'CCC.RRT', NULL, 'USER', NULL, 'Y');
INSERT INTO geostore.gs_user VALUES (1440, 'RDL.RRT', NULL, 'USER', NULL, 'Y');
INSERT INTO geostore.gs_user VALUES (1645, 'mss.llll', NULL, 'USER', NULL, 'Y');
INSERT INTO geostore.gs_user VALUES (1815, 'PRD.LRT', NULL, 'USER', NULL, 'Y');
INSERT INTO geostore.gs_user VALUES (1944, 'FRN.SVT', NULL, 'USER', NULL, 'Y');


--
-- Data for Name: gs_user_attribute; Type: TABLE DATA; Schema: geostore; Owner: geostore
--

INSERT INTO geostore.gs_user_attribute VALUES (2151, 'sub', 'MTT.SRA', 835);
INSERT INTO geostore.gs_user_attribute VALUES (1586, 'sub', '6YWNLDGCLM263ABH4VEGM2OFWR6W', 763);
INSERT INTO geostore.gs_user_attribute VALUES (1648, 'sub', 'mss.llll', 1645);
INSERT INTO geostore.gs_user_attribute VALUES (1827, 'sub', 'PRD.LRT', 1815);
INSERT INTO geostore.gs_user_attribute VALUES (1598, 'sub', '00000000', 935);
INSERT INTO geostore.gs_user_attribute VALUES (1606, 'sub', 'MFELI7XAFIDRFSYY1E2X1QYOXKEE', 773);
INSERT INTO geostore.gs_user_attribute VALUES (2018, 'sub', 'FRN.SVT', 1944);
INSERT INTO geostore.gs_user_attribute VALUES (2132, 'sub', 'BRT.FNC', 304);
INSERT INTO geostore.gs_user_attribute VALUES (1921, 'sub', 'RDL.RRT', 1440);
INSERT INTO geostore.gs_user_attribute VALUES (637, 'UUID', 'e6bc5c00-5e63-11ec-8c3d-1395b3b23f58', 636);
INSERT INTO geostore.gs_user_attribute VALUES (2147, 'sub', '525252', 293);


--
-- Data for Name: gs_usergroup; Type: TABLE DATA; Schema: geostore; Owner: geostore
--

INSERT INTO geostore.gs_usergroup VALUES (9, 'everyone', NULL, 'Y');
INSERT INTO geostore.gs_usergroup VALUES (455, 'GEOCITY_ADMINS', 'GEOCITY Admins', 'Y');
INSERT INTO geostore.gs_usergroup VALUES (473, 'ambiente-AsparmRaccoltaFarmaci-EDIT', 'ambiente-AsparmRaccoltaFarmaci-EDIT', 'Y');
INSERT INTO geostore.gs_usergroup VALUES (476, 'ROLE_SYS_GWCS', NULL, 'Y');
INSERT INTO geostore.gs_usergroup VALUES (479, 'ctr-AltimetriaLineeCTRN-VIEW', NULL, 'Y');
INSERT INTO geostore.gs_usergroup VALUES (482, 'ctr-AltimetriaLineeCTRN-EDIT', NULL, 'Y');
INSERT INTO geostore.gs_usergroup VALUES (737, 'TestGeocity', 'test', 'Y');
INSERT INTO geostore.gs_usergroup VALUES (1003, 'EDITOR_COMPLETO', 'Utente con permessi di EDIT su tutto.', 'Y');
INSERT INTO geostore.gs_usergroup VALUES (1014, 'EDITOR_DPAU', NULL, 'Y');
INSERT INTO geostore.gs_usergroup VALUES (1017, 'EDITOR_CPQ', NULL, 'Y');
INSERT INTO geostore.gs_usergroup VALUES (1020, 'EDITOR_DBGT', NULL, 'Y');
INSERT INTO geostore.gs_usergroup VALUES (1023, 'EDITOR_SIZA', NULL, 'Y');
INSERT INTO geostore.gs_usergroup VALUES (1026, 'EDITOR_ATAC', NULL, 'Y');
INSERT INTO geostore.gs_usergroup VALUES (1029, 'EDITOR_NIC', NULL, 'Y');
INSERT INTO geostore.gs_usergroup VALUES (1032, 'EDITOR_AMBIENTE', NULL, 'Y');
INSERT INTO geostore.gs_usergroup VALUES (1035, 'EDITOR_SITPAU', NULL, 'Y');
INSERT INTO geostore.gs_usergroup VALUES (1038, 'EDITOR_VINCOLI', NULL, 'Y');
INSERT INTO geostore.gs_usergroup VALUES (1041, 'EDITOR_URBANISTICA', NULL, 'Y');
INSERT INTO geostore.gs_usergroup VALUES (1044, 'EDITOR_CITTA_PUBBLICA', NULL, 'Y');
INSERT INTO geostore.gs_usergroup VALUES (1581, 'VIEWER', NULL, 'Y');


--
-- Data for Name: gs_usergroup_members; Type: TABLE DATA; Schema: geostore; Owner: geostore
--

INSERT INTO geostore.gs_usergroup_members VALUES (1645, 9);
INSERT INTO geostore.gs_usergroup_members VALUES (1815, 9);
INSERT INTO geostore.gs_usergroup_members VALUES (1944, 9);
INSERT INTO geostore.gs_usergroup_members VALUES (11, 9);
INSERT INTO geostore.gs_usergroup_members VALUES (12, 9);
INSERT INTO geostore.gs_usergroup_members VALUES (13, 9);
INSERT INTO geostore.gs_usergroup_members VALUES (293, 9);
INSERT INTO geostore.gs_usergroup_members VALUES (304, 9);
INSERT INTO geostore.gs_usergroup_members VALUES (293, 455);
INSERT INTO geostore.gs_usergroup_members VALUES (636, 9);
INSERT INTO geostore.gs_usergroup_members VALUES (763, 9);
INSERT INTO geostore.gs_usergroup_members VALUES (773, 9);
INSERT INTO geostore.gs_usergroup_members VALUES (835, 9);
INSERT INTO geostore.gs_usergroup_members VALUES (935, 9);
INSERT INTO geostore.gs_usergroup_members VALUES (763, 1026);
INSERT INTO geostore.gs_usergroup_members VALUES (1440, 9);
INSERT INTO geostore.gs_usergroup_members VALUES (763, 1581);
INSERT INTO geostore.gs_usergroup_members VALUES (304, 1581);
INSERT INTO geostore.gs_usergroup_members VALUES (935, 1581);
INSERT INTO geostore.gs_usergroup_members VALUES (835, 1581);
INSERT INTO geostore.gs_usergroup_members VALUES (773, 1581);
INSERT INTO geostore.gs_usergroup_members VALUES (1440, 1581);


--
-- Data for Name: gs_attribute; Type: TABLE DATA; Schema: geostore_test; Owner: geostore
--



--
-- Data for Name: gs_category; Type: TABLE DATA; Schema: geostore_test; Owner: geostore
--



--
-- Data for Name: gs_resource; Type: TABLE DATA; Schema: geostore_test; Owner: geostore
--



--
-- Data for Name: gs_security; Type: TABLE DATA; Schema: geostore_test; Owner: geostore
--



--
-- Data for Name: gs_stored_data; Type: TABLE DATA; Schema: geostore_test; Owner: geostore
--



--
-- Data for Name: gs_user; Type: TABLE DATA; Schema: geostore_test; Owner: geostore
--



--
-- Data for Name: gs_user_attribute; Type: TABLE DATA; Schema: geostore_test; Owner: geostore
--



--
-- Data for Name: gs_usergroup; Type: TABLE DATA; Schema: geostore_test; Owner: geostore
--



--
-- Data for Name: gs_usergroup_members; Type: TABLE DATA; Schema: geostore_test; Owner: geostore
--



--
-- Name: hibernate_sequence; Type: SEQUENCE SET; Schema: geostore; Owner: geostore
--

SELECT pg_catalog.setval('geostore.hibernate_sequence', 2151, true);


--
-- Name: hibernate_sequence; Type: SEQUENCE SET; Schema: geostore_test; Owner: geostore
--

SELECT pg_catalog.setval('geostore_test.hibernate_sequence', 1, false);


--
-- Name: gs_attribute gs_attribute_name_resource_id_key; Type: CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_attribute
    ADD CONSTRAINT gs_attribute_name_resource_id_key UNIQUE (name, resource_id);


--
-- Name: gs_attribute gs_attribute_pkey; Type: CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_attribute
    ADD CONSTRAINT gs_attribute_pkey PRIMARY KEY (id);


--
-- Name: gs_category gs_category_name_key; Type: CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_category
    ADD CONSTRAINT gs_category_name_key UNIQUE (name);


--
-- Name: gs_category gs_category_pkey; Type: CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_category
    ADD CONSTRAINT gs_category_pkey PRIMARY KEY (id);


--
-- Name: gs_resource gs_resource_name_key; Type: CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_resource
    ADD CONSTRAINT gs_resource_name_key UNIQUE (name);


--
-- Name: gs_resource gs_resource_pkey; Type: CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_resource
    ADD CONSTRAINT gs_resource_pkey PRIMARY KEY (id);


--
-- Name: gs_security gs_security_pkey; Type: CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_security
    ADD CONSTRAINT gs_security_pkey PRIMARY KEY (id);


--
-- Name: gs_security gs_security_resource_id_group_id_key; Type: CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_security
    ADD CONSTRAINT gs_security_resource_id_group_id_key UNIQUE (resource_id, group_id);


--
-- Name: gs_security gs_security_user_id_resource_id_key; Type: CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_security
    ADD CONSTRAINT gs_security_user_id_resource_id_key UNIQUE (user_id, resource_id);


--
-- Name: gs_stored_data gs_stored_data_pkey; Type: CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_stored_data
    ADD CONSTRAINT gs_stored_data_pkey PRIMARY KEY (id);


--
-- Name: gs_stored_data gs_stored_data_resource_id_key; Type: CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_stored_data
    ADD CONSTRAINT gs_stored_data_resource_id_key UNIQUE (resource_id);


--
-- Name: gs_user_attribute gs_user_attribute_name_user_id_key; Type: CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_user_attribute
    ADD CONSTRAINT gs_user_attribute_name_user_id_key UNIQUE (name, user_id);


--
-- Name: gs_user_attribute gs_user_attribute_pkey; Type: CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_user_attribute
    ADD CONSTRAINT gs_user_attribute_pkey PRIMARY KEY (id);


--
-- Name: gs_user gs_user_name_key; Type: CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_user
    ADD CONSTRAINT gs_user_name_key UNIQUE (name);


--
-- Name: gs_user gs_user_pkey; Type: CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_user
    ADD CONSTRAINT gs_user_pkey PRIMARY KEY (id);


--
-- Name: gs_usergroup gs_usergroup_groupname_key; Type: CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_usergroup
    ADD CONSTRAINT gs_usergroup_groupname_key UNIQUE (groupname);


--
-- Name: gs_usergroup_members gs_usergroup_members_pkey; Type: CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_usergroup_members
    ADD CONSTRAINT gs_usergroup_members_pkey PRIMARY KEY (user_id, group_id);


--
-- Name: gs_usergroup gs_usergroup_pkey; Type: CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_usergroup
    ADD CONSTRAINT gs_usergroup_pkey PRIMARY KEY (id);


--
-- Name: gs_attribute gs_attribute_name_resource_id_key; Type: CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_attribute
    ADD CONSTRAINT gs_attribute_name_resource_id_key UNIQUE (name, resource_id);


--
-- Name: gs_attribute gs_attribute_pkey; Type: CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_attribute
    ADD CONSTRAINT gs_attribute_pkey PRIMARY KEY (id);


--
-- Name: gs_category gs_category_name_key; Type: CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_category
    ADD CONSTRAINT gs_category_name_key UNIQUE (name);


--
-- Name: gs_category gs_category_pkey; Type: CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_category
    ADD CONSTRAINT gs_category_pkey PRIMARY KEY (id);


--
-- Name: gs_resource gs_resource_name_key; Type: CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_resource
    ADD CONSTRAINT gs_resource_name_key UNIQUE (name);


--
-- Name: gs_resource gs_resource_pkey; Type: CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_resource
    ADD CONSTRAINT gs_resource_pkey PRIMARY KEY (id);


--
-- Name: gs_security gs_security_pkey; Type: CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_security
    ADD CONSTRAINT gs_security_pkey PRIMARY KEY (id);


--
-- Name: gs_security gs_security_resource_id_group_id_key; Type: CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_security
    ADD CONSTRAINT gs_security_resource_id_group_id_key UNIQUE (resource_id, group_id);


--
-- Name: gs_security gs_security_user_id_resource_id_key; Type: CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_security
    ADD CONSTRAINT gs_security_user_id_resource_id_key UNIQUE (user_id, resource_id);


--
-- Name: gs_stored_data gs_stored_data_pkey; Type: CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_stored_data
    ADD CONSTRAINT gs_stored_data_pkey PRIMARY KEY (id);


--
-- Name: gs_stored_data gs_stored_data_resource_id_key; Type: CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_stored_data
    ADD CONSTRAINT gs_stored_data_resource_id_key UNIQUE (resource_id);


--
-- Name: gs_user_attribute gs_user_attribute_name_user_id_key; Type: CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_user_attribute
    ADD CONSTRAINT gs_user_attribute_name_user_id_key UNIQUE (name, user_id);


--
-- Name: gs_user_attribute gs_user_attribute_pkey; Type: CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_user_attribute
    ADD CONSTRAINT gs_user_attribute_pkey PRIMARY KEY (id);


--
-- Name: gs_user gs_user_name_key; Type: CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_user
    ADD CONSTRAINT gs_user_name_key UNIQUE (name);


--
-- Name: gs_user gs_user_pkey; Type: CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_user
    ADD CONSTRAINT gs_user_pkey PRIMARY KEY (id);


--
-- Name: gs_usergroup gs_usergroup_groupname_key; Type: CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_usergroup
    ADD CONSTRAINT gs_usergroup_groupname_key UNIQUE (groupname);


--
-- Name: gs_usergroup_members gs_usergroup_members_pkey; Type: CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_usergroup_members
    ADD CONSTRAINT gs_usergroup_members_pkey PRIMARY KEY (user_id, group_id);


--
-- Name: gs_usergroup gs_usergroup_pkey; Type: CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_usergroup
    ADD CONSTRAINT gs_usergroup_pkey PRIMARY KEY (id);


--
-- Name: idx_attribute_date; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_attribute_date ON geostore.gs_attribute USING btree (attribute_date);


--
-- Name: idx_attribute_name; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_attribute_name ON geostore.gs_attribute USING btree (name);


--
-- Name: idx_attribute_number; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_attribute_number ON geostore.gs_attribute USING btree (attribute_number);


--
-- Name: idx_attribute_resource; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_attribute_resource ON geostore.gs_attribute USING btree (resource_id);


--
-- Name: idx_attribute_text; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_attribute_text ON geostore.gs_attribute USING btree (attribute_text);


--
-- Name: idx_attribute_type; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_attribute_type ON geostore.gs_attribute USING btree (attribute_type);


--
-- Name: idx_attribute_user; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_attribute_user ON geostore.gs_user_attribute USING btree (user_id);


--
-- Name: idx_category_type; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_category_type ON geostore.gs_category USING btree (name);


--
-- Name: idx_resource_category; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_resource_category ON geostore.gs_resource USING btree (category_id);


--
-- Name: idx_resource_creation; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_resource_creation ON geostore.gs_resource USING btree (creation);


--
-- Name: idx_resource_description; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_resource_description ON geostore.gs_resource USING btree (description);


--
-- Name: idx_resource_metadata; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_resource_metadata ON geostore.gs_resource USING btree (metadata);


--
-- Name: idx_resource_name; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_resource_name ON geostore.gs_resource USING btree (name);


--
-- Name: idx_resource_update; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_resource_update ON geostore.gs_resource USING btree (lastupdate);


--
-- Name: idx_security_group; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_security_group ON geostore.gs_security USING btree (group_id);


--
-- Name: idx_security_groupname; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_security_groupname ON geostore.gs_security USING btree (groupname);


--
-- Name: idx_security_read; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_security_read ON geostore.gs_security USING btree (canread);


--
-- Name: idx_security_resource; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_security_resource ON geostore.gs_security USING btree (resource_id);


--
-- Name: idx_security_user; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_security_user ON geostore.gs_security USING btree (user_id);


--
-- Name: idx_security_username; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_security_username ON geostore.gs_security USING btree (username);


--
-- Name: idx_security_write; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_security_write ON geostore.gs_security USING btree (canwrite);


--
-- Name: idx_user_attribute_name; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_user_attribute_name ON geostore.gs_user_attribute USING btree (name);


--
-- Name: idx_user_attribute_text; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_user_attribute_text ON geostore.gs_user_attribute USING btree (string);


--
-- Name: idx_user_group; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_user_group ON geostore.gs_user USING btree (group_id);


--
-- Name: idx_user_name; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_user_name ON geostore.gs_user USING btree (name);


--
-- Name: idx_user_password; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_user_password ON geostore.gs_user USING btree (user_password);


--
-- Name: idx_user_role; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_user_role ON geostore.gs_user USING btree (user_role);


--
-- Name: idx_usergroup_name; Type: INDEX; Schema: geostore; Owner: geostore
--

CREATE INDEX idx_usergroup_name ON geostore.gs_usergroup USING btree (groupname);


--
-- Name: idx_attribute_date; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_attribute_date ON geostore_test.gs_attribute USING btree (attribute_date);


--
-- Name: idx_attribute_name; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_attribute_name ON geostore_test.gs_attribute USING btree (name);


--
-- Name: idx_attribute_number; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_attribute_number ON geostore_test.gs_attribute USING btree (attribute_number);


--
-- Name: idx_attribute_resource; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_attribute_resource ON geostore_test.gs_attribute USING btree (resource_id);


--
-- Name: idx_attribute_text; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_attribute_text ON geostore_test.gs_attribute USING btree (attribute_text);


--
-- Name: idx_attribute_type; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_attribute_type ON geostore_test.gs_attribute USING btree (attribute_type);


--
-- Name: idx_attribute_user; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_attribute_user ON geostore_test.gs_user_attribute USING btree (user_id);


--
-- Name: idx_category_type; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_category_type ON geostore_test.gs_category USING btree (name);


--
-- Name: idx_resource_category; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_resource_category ON geostore_test.gs_resource USING btree (category_id);


--
-- Name: idx_resource_creation; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_resource_creation ON geostore_test.gs_resource USING btree (creation);


--
-- Name: idx_resource_description; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_resource_description ON geostore_test.gs_resource USING btree (description);


--
-- Name: idx_resource_metadata; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_resource_metadata ON geostore_test.gs_resource USING btree (metadata);


--
-- Name: idx_resource_name; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_resource_name ON geostore_test.gs_resource USING btree (name);


--
-- Name: idx_resource_update; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_resource_update ON geostore_test.gs_resource USING btree (lastupdate);


--
-- Name: idx_security_group; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_security_group ON geostore_test.gs_security USING btree (group_id);


--
-- Name: idx_security_groupname; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_security_groupname ON geostore_test.gs_security USING btree (groupname);


--
-- Name: idx_security_read; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_security_read ON geostore_test.gs_security USING btree (canread);


--
-- Name: idx_security_resource; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_security_resource ON geostore_test.gs_security USING btree (resource_id);


--
-- Name: idx_security_user; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_security_user ON geostore_test.gs_security USING btree (user_id);


--
-- Name: idx_security_username; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_security_username ON geostore_test.gs_security USING btree (username);


--
-- Name: idx_security_write; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_security_write ON geostore_test.gs_security USING btree (canwrite);


--
-- Name: idx_user_attribute_name; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_user_attribute_name ON geostore_test.gs_user_attribute USING btree (name);


--
-- Name: idx_user_attribute_text; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_user_attribute_text ON geostore_test.gs_user_attribute USING btree (string);


--
-- Name: idx_user_group; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_user_group ON geostore_test.gs_user USING btree (group_id);


--
-- Name: idx_user_name; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_user_name ON geostore_test.gs_user USING btree (name);


--
-- Name: idx_user_password; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_user_password ON geostore_test.gs_user USING btree (user_password);


--
-- Name: idx_user_role; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_user_role ON geostore_test.gs_user USING btree (user_role);


--
-- Name: idx_usergroup_name; Type: INDEX; Schema: geostore_test; Owner: geostore
--

CREATE INDEX idx_usergroup_name ON geostore_test.gs_usergroup USING btree (groupname);


--
-- Name: gs_attribute fk_attribute_resource; Type: FK CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_attribute
    ADD CONSTRAINT fk_attribute_resource FOREIGN KEY (resource_id) REFERENCES geostore.gs_resource(id);


--
-- Name: gs_stored_data fk_data_resource; Type: FK CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_stored_data
    ADD CONSTRAINT fk_data_resource FOREIGN KEY (resource_id) REFERENCES geostore.gs_resource(id);


--
-- Name: gs_resource fk_resource_category; Type: FK CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_resource
    ADD CONSTRAINT fk_resource_category FOREIGN KEY (category_id) REFERENCES geostore.gs_category(id);


--
-- Name: gs_security fk_security_group; Type: FK CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_security
    ADD CONSTRAINT fk_security_group FOREIGN KEY (group_id) REFERENCES geostore.gs_usergroup(id);


--
-- Name: gs_security fk_security_resource; Type: FK CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_security
    ADD CONSTRAINT fk_security_resource FOREIGN KEY (resource_id) REFERENCES geostore.gs_resource(id);


--
-- Name: gs_security fk_security_user; Type: FK CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_security
    ADD CONSTRAINT fk_security_user FOREIGN KEY (user_id) REFERENCES geostore.gs_user(id);


--
-- Name: gs_user_attribute fk_uattrib_user; Type: FK CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_user_attribute
    ADD CONSTRAINT fk_uattrib_user FOREIGN KEY (user_id) REFERENCES geostore.gs_user(id);


--
-- Name: gs_user fk_user_ugroup; Type: FK CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_user
    ADD CONSTRAINT fk_user_ugroup FOREIGN KEY (group_id) REFERENCES geostore.gs_usergroup(id);


--
-- Name: gs_usergroup_members fkfde460db62224f72; Type: FK CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_usergroup_members
    ADD CONSTRAINT fkfde460db62224f72 FOREIGN KEY (user_id) REFERENCES geostore.gs_user(id);


--
-- Name: gs_usergroup_members fkfde460db9ec981b7; Type: FK CONSTRAINT; Schema: geostore; Owner: geostore
--

ALTER TABLE ONLY geostore.gs_usergroup_members
    ADD CONSTRAINT fkfde460db9ec981b7 FOREIGN KEY (group_id) REFERENCES geostore.gs_usergroup(id);


--
-- Name: gs_attribute fk_attribute_resource; Type: FK CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_attribute
    ADD CONSTRAINT fk_attribute_resource FOREIGN KEY (resource_id) REFERENCES geostore.gs_resource(id);


--
-- Name: gs_stored_data fk_data_resource; Type: FK CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_stored_data
    ADD CONSTRAINT fk_data_resource FOREIGN KEY (resource_id) REFERENCES geostore.gs_resource(id);


--
-- Name: gs_resource fk_resource_category; Type: FK CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_resource
    ADD CONSTRAINT fk_resource_category FOREIGN KEY (category_id) REFERENCES geostore.gs_category(id);


--
-- Name: gs_security fk_security_group; Type: FK CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_security
    ADD CONSTRAINT fk_security_group FOREIGN KEY (group_id) REFERENCES geostore.gs_usergroup(id);


--
-- Name: gs_security fk_security_resource; Type: FK CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_security
    ADD CONSTRAINT fk_security_resource FOREIGN KEY (resource_id) REFERENCES geostore.gs_resource(id);


--
-- Name: gs_security fk_security_user; Type: FK CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_security
    ADD CONSTRAINT fk_security_user FOREIGN KEY (user_id) REFERENCES geostore.gs_user(id);


--
-- Name: gs_user_attribute fk_uattrib_user; Type: FK CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_user_attribute
    ADD CONSTRAINT fk_uattrib_user FOREIGN KEY (user_id) REFERENCES geostore.gs_user(id);


--
-- Name: gs_user fk_user_ugroup; Type: FK CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_user
    ADD CONSTRAINT fk_user_ugroup FOREIGN KEY (group_id) REFERENCES geostore.gs_usergroup(id);


--
-- Name: gs_usergroup_members fkfde460db62224f72; Type: FK CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_usergroup_members
    ADD CONSTRAINT fkfde460db62224f72 FOREIGN KEY (user_id) REFERENCES geostore.gs_user(id);


--
-- Name: gs_usergroup_members fkfde460db9ec981b7; Type: FK CONSTRAINT; Schema: geostore_test; Owner: geostore
--

ALTER TABLE ONLY geostore_test.gs_usergroup_members
    ADD CONSTRAINT fkfde460db9ec981b7 FOREIGN KEY (group_id) REFERENCES geostore.gs_usergroup(id);


