-- in case of failure run the query to drop the DB and run the queries again
-- drop database reservation_system;
create database reservation_system;

use reservation_system;

create table
    airport (
        name varchar(255) primary key not null,
        city varchar(255) not null
    );

create table
    airline (name varchar(255) primary key not null);

create table
    airplane (
        id int primary key not null,
        seats int not null,
        airline_name varchar(255) not null,
        foreign key (airline_name) references airline (name)
    );

-- note that we have a composite primary key for this table as well some FK references
create table
    flight (
        flight_num varchar(6) not null,
        departure_time datetime not null,
        arrival_time datetime not null,
        price decimal(10, 2) not null,
        airplane_id int not null,
        airline_name varchar(255) not null,
        departure_airport_name varchar(255),
        arrival_airport_name varchar(255),
        dep_status varchar(20) not null,
        primary key (flight_num, airline_name),
        foreign key (airline_name) references airline (name),
        foreign key (airplane_id) references airplane (id),
        foreign key (departure_airport_name) references airport (name),
        foreign key (arrival_airport_name) references airport (name)
    );

create table
    customer (
        email varchar(255) primary key not null,
        name varchar(255) not null,
        password varchar(255) not null,
        building_number varchar(20) not null,
        street varchar(255) not null,
        city varchar(255) not null,
        state varchar(255) not null,
        phone_number varchar(20) not null,
        passport_number varchar(20) not null,
        passport_expiration date not null,
        passport_country varchar(255) not null,
        date_of_birth date not null
    );

create table
    booking_agent (
        email varchar(255) primary key not null,
        password varchar(255) not null,
        booking_agent_id int DEFAULT null
    );

create table
    ticket (
        id int primary key auto_increment not null,
        customer_email varchar(255) not null,
        airline_name varchar(255) not null,
        flight_id varchar(6) not null,
        foreign key (airline_name) references airline (name),
        foreign key (flight_id) references flight (flight_num),
        foreign key (customer_email) references customer (email)
    );

create table
    tickets_by_booking_agent (
        booking_agent_email varchar(255) not null,
        ticket_id int not null,
        foreign key (booking_agent_email) references booking_agent (email),
        foreign key (ticket_id) references ticket (id),
        primary key (booking_agent_email, ticket_id)
    );

create table
    permission (
        type varchar(255) not null primary key not null,
        description varchar(255) not null
    );

create table
    airline_staff (
        username varchar(255) primary key not null,
        password varchar(255) not null,
        first_name varchar(255) not null,
        last_name varchar(255) not null,
        date_of_birth date not null,
        airline_name varchar(255) not null,
        permission varchar(255) not null,
        foreign key (airline_name) references airline (name),
        foreign key (permission) references permission (type)
    );

CREATE TABLE
    purchases (
        ticket_id int NOT NULL,
        customer_email varchar(255) NOT NULL,
        booking_agent_id varchar(255) DEFAULT NULL,
        purchase_date date NOT NULL,
        PRIMARY KEY (ticket_id, customer_email),
        FOREIGN KEY (ticket_id) REFERENCES ticket (id),
        FOREIGN KEY (customer_email) REFERENCES customer (email)
    );

CREATE TABLE
    booking_agent_work_for (
        email varchar(255) NOT NULL,
        airline_name varchar(255) NOT NULL,
        PRIMARY KEY (email, airline_name),
        FOREIGN KEY (email) REFERENCES booking_agent (email),
        FOREIGN KEY (airline_name) REFERENCES airline (name)
    );

CREATE TABLE
    permission_by_user (
        username varchar(50) NOT NULL,
        permission_type varchar(50) NOT NULL,
        PRIMARY KEY (username, permission_type),
        FOREIGN KEY (username) REFERENCES airline_staff (username),
        FOREIGN KEY (permission_type) REFERENCES permission (type)
    );

CREATE TABLE
    commission_per_agent (
        booking_agent_email varchar(255) NOT NULL,
        ticket_id int NOT NULL,
        commission decimal(10, 2) DEFAULT 0,
        PRIMARY KEY (booking_agent_email, ticket_id),
        FOREIGN KEY (booking_agent_email) REFERENCES booking_agent (email),
        FOREIGN KEY (ticket_id) REFERENCES ticket (id)
    );