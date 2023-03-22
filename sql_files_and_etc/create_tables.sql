-- this is the document with the queries to create the tables based on the SCHEMA.PDF file

-- first of all create a DB
create database reservation_system;
-- in case of failure run the query to drop the DB and run the queries again
-- drop database reservation_system;

create table airport(
    name varchar(255) primary key not null,
    city varchar(255) not null
);

create table airline(
    name varchar(255) primary key not null
);


create table airplane(
    id int primary key not null,
    seats int not null,
    airline_name varchar(255) not null, 
    foreign key(airline_name) references airline(name)
);

-- note that we have a composite primary key for this table as well some FK references
create table flight(
    flight_num varchar(6) not null, 
    departure_time datetime not null,
    arrival_time datetime not null, 
    price decimal(10,2) not null, 
    airplane_id int not null, 
    airline_name varchar(255) not null, 
    departure_airport_name varchar(255), 
    arrival_airport_name varchar(255),
    dep_status varchar(20) not null,
    primary key (flight_num, airline_name),
    foreign key(airline_name) references airline(name),
    foreign key(airplane_id) references airplane(id),
    foreign key(departure_airport_name) references airport(name),
    foreign key(arrival_airport_name) references airport(name)
);

create table customer(
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

create table booking_agent(
    email varchar(255) primary key not null,
    password varchar(255) not null,
    booking_agent_id int not null
);


create table ticket(
    id int primary key auto_increment not null, 
    customer_email varchar(255) not null, 
    airline_name varchar(255) not null, 
    flight_id varchar(6) not null, 
    foreign key(airline_name) references airline(name),
    foreign key(flight_id) references flight(flight_num)
);


create table tickets_by_booking_agent(
    booking_agent_email varchar(255) not null,
    ticket_id int not null,
    foreign key(booking_agent_email) references booking_agent(email),
    foreign key(ticket_id) references ticket(id),
    primary key (booking_agent_email, ticket_id)
);

create table airline_staff(
    username varchar(255) primary key not null, 
    password varchar(255) not null,
    first_name varchar(255) not null,
    last_name varchar(255) not null,
    date_of_birth date not null,
    airline_name varchar(255) not null,
    foreign key(airline_name) references airline(name)
); 

create table permission(
    type varchar(255) not null,
    description varchar(255)
);
