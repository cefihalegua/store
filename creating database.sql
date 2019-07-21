DROP database IF exists store;
create database store;
use store;

create table categories(
id int not null auto_increment,
name varchar(50) not null,
primary key(id)
);

Drop Table If Exists products;
create table products(
id int not null auto_increment,
title varchar(50),
description varchar(50),
price varchar(50),
img_url varchar(128),
category int not null,
favorite boolean,
primary key(id)
);