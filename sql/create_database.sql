CREATE DATABASE datasource;

CREATE user postgres with password 'postgres';

grant all privileges on database datasource to postgres;

