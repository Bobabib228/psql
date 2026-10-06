create table customers_data (
customer_id varchar(10) not null primary key,
company_name varchar(50) not null,
contact_name varchar(10) not null
);

create table employees_data(
employee_id int not null primary key,
first_name varchar(50) not null,
last_name varchar(50) not null,
title varchar(50) not null,
birth_date date not null,
notes text not null
);

create table orders_data (
order_id int primary key,
customer_id varchar(10) references customers_data(customer_id) not null,
employee_id int references employees_data(employee_id) not null,
order_date date not null,
ship_city varchar(100) not null
);
