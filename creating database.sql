DROP database IF exists store;
create database store;
use store;
create table categories(
id int not null auto_increment,
name varchar(50) not null,
primary key(id)
);