create database if not exists mydb;
use mydb;

create table if not exists sensordata (
    tag int not null,
    value int, 
    sourcetime datetime default getdate()
);