DROP DATABASE IF EXISTS reservation_system;


CREATE DATABASE reservation_system;


USE reservation_system;


CREATE TABLE airport (
    name varchar(255) PRIMARY KEY NOT NULL,
    city varchar(255) NOT NULL
);


CREATE TABLE airline (name varchar(255) PRIMARY KEY NOT NULL);


CREATE TABLE airplane (
    id int PRIMARY KEY NOT NULL,
    seats int NOT NULL,
    airline_name varchar(255) NOT NULL,
    FOREIGN KEY (airline_name) REFERENCES airline (name)
);


-- note that we have a composite primary key for this table as well some FK references
CREATE TABLE flight (
    flight_num varchar(6) NOT NULL,
    departure_time datetime NOT NULL,
    arrival_time datetime NOT NULL,
    price decimal(10, 2) NOT NULL,
    airplane_id int NOT NULL,
    airline_name varchar(255) NOT NULL,
    departure_airport_name varchar(255),
    arrival_airport_name varchar(255),
    dep_status varchar(20) NOT NULL,
    PRIMARY KEY (flight_num, airline_name),
    FOREIGN KEY (airline_name) REFERENCES airline (name),
    FOREIGN KEY (airplane_id) REFERENCES airplane (id),
    FOREIGN KEY (departure_airport_name) REFERENCES airport (name),
    FOREIGN KEY (arrival_airport_name) REFERENCES airport (name)
);


CREATE TABLE customer (
    email varchar(255) PRIMARY KEY NOT NULL,
    name varchar(255) NOT NULL,
    PASSWORD varchar(255) NOT NULL,
    building_number varchar(20) NOT NULL,
    street varchar(255) NOT NULL,
    city varchar(255) NOT NULL,
    state varchar(255) NOT NULL,
    phone_number varchar(20) NOT NULL,
    passport_number varchar(20) NOT NULL,
    passport_expiration date NOT NULL,
    passport_country varchar(255) NOT NULL,
    date_of_birth date NOT NULL
);


CREATE TABLE booking_agent (
    email varchar(255) PRIMARY KEY NOT NULL,
    PASSWORD varchar(255) NOT NULL,
    booking_agent_id int DEFAULT NULL
);


CREATE TABLE ticket (
    id int PRIMARY KEY AUTO_INCREMENT NOT NULL,
    customer_email varchar(255) NOT NULL,
    airline_name varchar(255) NOT NULL,
    flight_id varchar(6) NOT NULL,
    FOREIGN KEY (airline_name) REFERENCES airline (name),
    FOREIGN KEY (flight_id) REFERENCES flight (flight_num),
    FOREIGN KEY (customer_email) REFERENCES customer (email)
);


CREATE TABLE tickets_by_booking_agent (
    booking_agent_email varchar(255) NOT NULL,
    ticket_id int NOT NULL,
    FOREIGN KEY (booking_agent_email) REFERENCES booking_agent (email),
    FOREIGN KEY (ticket_id) REFERENCES ticket (id),
    PRIMARY KEY (booking_agent_email, ticket_id)
);


CREATE TABLE permission (
    TYPE varchar(255) NOT NULL PRIMARY KEY NOT NULL,
    description varchar(255) NOT NULL
);


CREATE TABLE airline_staff (
    username varchar(255) PRIMARY KEY NOT NULL,
    PASSWORD varchar(255) NOT NULL,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    date_of_birth date NOT NULL,
    airline_name varchar(255) NOT NULL,
    permission varchar(255) NOT NULL,
    FOREIGN KEY (airline_name) REFERENCES airline (name),
    FOREIGN KEY (permission) REFERENCES permission (TYPE)
);


CREATE TABLE purchases (
    ticket_id int NOT NULL,
    customer_email varchar(255) NOT NULL,
    booking_agent_id varchar(255) DEFAULT NULL,
    purchase_date date NOT NULL,
    PRIMARY KEY (ticket_id, customer_email),
    FOREIGN KEY (ticket_id) REFERENCES ticket (id),
    FOREIGN KEY (customer_email) REFERENCES customer (email)
);


CREATE TABLE booking_agent_work_for (
    email varchar(255) NOT NULL,
    airline_name varchar(255) NOT NULL,
    PRIMARY KEY (email, airline_name),
    FOREIGN KEY (email) REFERENCES booking_agent (email),
    FOREIGN KEY (airline_name) REFERENCES airline (name)
);


CREATE TABLE permission_by_user (
    username varchar(50) NOT NULL,
    permission_type varchar(50) NOT NULL,
    PRIMARY KEY (username, permission_type),
    FOREIGN KEY (username) REFERENCES airline_staff (username),
    FOREIGN KEY (permission_type) REFERENCES permission (TYPE)
);


CREATE TABLE commission_per_agent (
    booking_agent_email varchar(255) NOT NULL,
    ticket_id int NOT NULL,
    commission decimal(10, 2) DEFAULT 0,
    PRIMARY KEY (booking_agent_email, ticket_id),
    FOREIGN KEY (booking_agent_email) REFERENCES booking_agent (email),
    FOREIGN KEY (ticket_id) REFERENCES ticket (id)
);