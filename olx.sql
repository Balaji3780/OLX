create database olx;
use olx;

create table login(
username varchar(50),
password varchar(50));

create table dataupload(
type varchar(50),
make varchar(50),
model varchar(50),
year year,
price varchar(50),
description varchar(200),
image longblob);

drop table dataupload;

select * from login;
select * from dataupload;