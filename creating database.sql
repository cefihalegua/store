DROP database IF exists store;
create database store;
use store;
create table categories(
id int not null auto_increment,
name varchar(50) not null,
primary key(id)
);

create table products(
id int not null auto_increment,
title varchar(30),
description varchar(100),
favorite boolean,
price int,
img_url varchar(100),
category_id int
)