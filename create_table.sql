create table ved (
id integer primary key autoincrement,
family text not null,
job varchar(20),
id_deb integer,
salary float
);

create table deps (
id_deb integer primary key,
id_city integer,
title text
);

create table city (
id integer primary key autoincrement,
name text
)


