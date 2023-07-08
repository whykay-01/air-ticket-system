SELECT *
FROM booking_agent
WHERE email = '{}';


-- 
INSERT INTO booking_agent (email, PASSWORD)
VALUES ('{}', MD5 ('{}'));


SELECT *
FROM customer
WHERE email = '{}'
    AND PASSWORD = MD5 ('{}');


-- 
SELECT *
FROM airline_staff
WHERE username = '{}'
    AND PASSWORD = MD5 ('{}');


-- 
SELECT *
FROM booking_agent
WHERE email = '{}'
    AND PASSWORD = MD5 ('{}');


-- 
INSERT INTO customer
VALUES (
        '{}',
        '{}',
        MD5 ('{}'),
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}'
    );


-- 
SELECT *
FROM airline_staff
WHERE username = '{}';


-- 
INSERT INTO airline_staff (
        username,
        PASSWORD,
        first_name,
        last_name,
        date_of_birth,
        airline_name,
        permission
    )
VALUES ('{}', MD5 ('{}'), '{}', '{}', '{}', '{}', 'N/A');


-- 
SELECT F.flight_num,
    F.airline_name,
    F.departure_airport_name,
    F.departure_time,
    F.arrival_airport_name,
    F.arrival_time,
    F.dep_status
FROM ticket AS T
    JOIN flight AS F ON T.flight_id = F.flight_num
WHERE customer_email = '{}'
    AND dep_status = 'Upcoming';


-- 
SELECT first_name,
    last_name,
    airline_name,
    permission
FROM airline_staff
WHERE username = '{}';


-- 
SELECT airline_name,
    flight_num,
    departure_airport_name,
    departure_time,
    arrival_airport_name,
    arrival_time,
    dep_status
FROM flight
WHERE airline_name = '{}'
    AND departure_time BETWEEN NOW ()
    AND DATE_ADD (NOW (), INTERVAL 30 DAY);


-- 
SELECT airline_name
FROM booking_agent_work_for
WHERE email = '{}';


-- 
SELECT F.airline_name,
    F.flight_num,
    F.departure_airport_name,
    F.departure_time,
    F.arrival_airport_name,
    F.arrival_time,
    F.dep_status,
    T.customer_email
FROM purchases AS P
    JOIN ticket AS T ON P.ticket_id = T.id
    JOIN flight F ON (
        T.flight_id = F.flight_num
        AND T.airline_name = F.airline_name
    )
WHERE F.airline_name = '{}'
    AND P.booking_agent_id = '{}'
    AND F.dep_status = 'Upcoming';


-- 
SELECT DISTINCT F.departure_airport_name
FROM purchases AS P
    JOIN ticket AS T ON P.ticket_id = T.id
    JOIN flight F ON (
        T.flight_id = F.flight_num
        AND T.airline_name = F.airline_name
    )
WHERE F.airline_name = '{}'
    AND P.booking_agent_id = '{}';


-- 
SELECT DISTINCT F.departure_airport_name
FROM purchases AS P
    JOIN ticket AS T ON P.ticket_id = T.id
    JOIN flight F ON (
        T.flight_id = F.flight_num
        AND T.airline_name = F.airline_name
    )
WHERE F.airline_name = '{}'
    AND P.booking_agent_id = '{}';


-- 
SELECT first_name,
    last_name,
    airline_name,
    permission
FROM airline_staff
WHERE username = '{}';


-- 
SELECT airline_name,
    flight_num,
    departure_airport_name,
    departure_time,
    arrival_airport_name,
    arrival_time,
    dep_status
FROM flight
WHERE airline_name = '{}'
    AND departure_time BETWEEN NOW ()
    AND DATE_ADD (NOW (), INTERVAL 30 DAY);


-- 
SELECT permission,
    airline_name
FROM airline_staff
WHERE username = '{}';


-- 
SELECT id,
    seats
FROM airplane
WHERE airline_name = '{}'
ORDER BY id;


-- 
SELECT *
FROM airplane
WHERE id = '{}';


-- 
SELECT permission
FROM airline_staff
WHERE username = '{}';


-- 
SELECT airline_name
FROM airline_staff
WHERE username = '{}';


-- 
INSERT INTO airplane (id, seats, airline_name)
VALUES ('{}', '{}', '{}');


-- 
SELECT permission
FROM airline_staff
WHERE username = '{}';


-- 
SELECT name,
    city
FROM airport
ORDER BY city;


-- 
SELECT *
FROM airport
WHERE name = '{}';


-- 
SELECT permission
FROM airline_staff
WHERE username = '{}';


-- 
INSERT INTO airport (name, city)
VALUES ('{}', '{}');


-- 
SELECT permission
FROM airline_staff
WHERE username = '{}';


-- 
SELECT airline_name
FROM airline_staff
WHERE username = '{}';


-- 
SELECT id
FROM airplane
WHERE airline_name = '{}';


-- 
SELECT name
FROM airport;


-- 
SELECT airline_name
FROM airline_staff
WHERE username = '{}';


-- 
SELECT *
FROM flight
WHERE flight_num = '{}'
    AND airline_name = '{}';


-- 
INSERT INTO flight (
        flight_num,
        departure_time,
        arrival_time,
        price,
        airplane_id,
        airline_name,
        departure_airport_name,
        arrival_airport_name,
        dep_status
    )
VALUES (
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}'
    );


-- 
SELECT permission,
    airline_name
FROM airline_staff
WHERE username = '{}';


-- 
SELECT flight_num
FROM flight
WHERE airline_name = '{}';


-- 
SELECT airline_name
FROM airline_staff
WHERE username = '{}';


-- 
UPDATE flight
SET dep_status = '{}'
WHERE flight_num = '{}'
    AND airline_name = '{}';


-- 
SELECT permission,
    airline_name
FROM airline_staff
WHERE username = '{}';


-- 
SELECT username,
    first_name,
    last_name,
    date_of_birth,
    permission
FROM airline_staff
WHERE username <> '{}'
    AND airline_name = '{}'
ORDER BY username;


-- 
SELECT airline_name
FROM airline_staff
WHERE username = '{}';


-- 
SELECT permission
FROM airline_staff
WHERE username = '{}'
    AND airline_name = '{}';


-- 
SELECT username
FROM airline_staff
WHERE username = '{}'
    AND airline_name = '{}';


-- 
UPDATE airline_staff
SET permission = '{}'
WHERE username = '{}';


-- 
SELECT permission,
    airline_name
FROM airline_staff
WHERE username = '{}';


-- 
SELECT b.email,
    b.booking_agent_id
FROM booking_agent b
    JOIN booking_agent_work_for bawf ON bawf.email = b.email
WHERE bawf.airline_name = '{}';


-- 
SELECT permission,
    airline_name
FROM airline_staff
WHERE username = '{}';


-- 
SELECT email
FROM booking_agent
WHERE email = '{}';


-- 
SELECT email
FROM booking_agent_work_for
WHERE email = '{}'
    AND airline_name = '{}';


-- 
SELECT *
FROM booking_agent AS b
    JOIN booking_agent_work_for AS bawf ON b.email = bawf.email
WHERE bawf.airline_name = '{}'
    AND b.booking_agent_id = '{}';


-- 
INSERT INTO booking_agent_work_for
VALUES ('{}', '{}');


-- 
UPDATE booking_agent
SET booking_agent_id = '{}'
WHERE email = '{}';


-- 
SELECT permission,
    airline_name
FROM airline_staff
WHERE username = '{}';


-- 
SELECT b.email,
    b.booking_agent_id
FROM booking_agent b
    JOIN booking_agent_work_for bawf ON bawf.email = b.email
WHERE bawf.airline_name = '{}';


-- 
SELECT b.email,
    COUNT(p.ticket_id) AS num_tickets
FROM booking_agent b
    JOIN purchases p ON b.email = p.booking_agent_id
    JOIN booking_agent_work_for bawf ON b.email = bawf.email
WHERE p.purchase_date >= DATE_SUB (CURDATE (), INTERVAL 1 MONTH)
    AND bawf.airline_name = '{}'
GROUP BY b.email
ORDER BY num_tickets DESC
LIMIT 5;


-- 
SELECT b.email,
    COUNT(p.ticket_id) AS num_tickets
FROM booking_agent b
    JOIN purchases p ON b.email = p.booking_agent_id
    JOIN booking_agent_work_for bawf ON b.email = bawf.email
WHERE p.purchase_date >= DATE_SUB (CURDATE (), INTERVAL 1 YEAR)
    AND bawf.airline_name = '{}'
GROUP BY b.email
ORDER BY num_tickets DESC
LIMIT 5;


-- 
SELECT cpa.booking_agent_email,
    SUM(cpa.commission) AS total_commission
FROM commission_per_agent cpa
    JOIN booking_agent_work_for bawf ON cpa.booking_agent_email = bawf.email
    JOIN purchases p ON cpa.ticket_id = p.ticket_id
WHERE p.purchase_date >= DATE_SUB (CURDATE (), INTERVAL 1 YEAR)
    AND bawf.airline_name = '{}'
GROUP BY cpa.booking_agent_email
ORDER BY total_commission DESC
LIMIT 5;


-- 
SELECT cpa.booking_agent_email,
    SUM(cpa.commission) AS total_commission
FROM commission_per_agent cpa
    JOIN booking_agent_work_for bawf ON cpa.booking_agent_email = bawf.email
    JOIN purchases p ON cpa.ticket_id = p.ticket_id
WHERE p.purchase_date >= DATE_SUB (CURDATE (), INTERVAL 1 MONTH)
    AND bawf.airline_name = '{}'
GROUP BY cpa.booking_agent_email
ORDER BY total_commission DESC
LIMIT 5;


-- 
SELECT airline_name
FROM airline_staff
WHERE username = '{}' -- 
SELECT f.arrival_airport_name,
    a.city,
    COUNT(p.ticket_id) AS times
FROM purchases p
    JOIN ticket t ON p.ticket_id = t.id
    JOIN flight f ON (
        t.flight_id = f.flight_num
        AND t.airline_name = f.airline_name
    )
    JOIN airport a ON f.arrival_airport_name = a.name
WHERE p.purchase_date >= DATE_SUB (CURDATE (), INTERVAL 3 MONTH)
    AND f.airline_name = '{}'
GROUP BY (a.name)
ORDER BY times DESC
LIMIT 3;


-- 
SELECT f.arrival_airport_name,
    a.city,
    COUNT(p.ticket_id) AS times
FROM purchases p
    JOIN ticket t ON p.ticket_id = t.id
    JOIN flight f ON (
        t.flight_id = f.flight_num
        AND t.airline_name = f.airline_name
    )
    JOIN airport a ON f.arrival_airport_name = a.name
WHERE p.purchase_date >= DATE_SUB (CURDATE (), INTERVAL 1 YEAR)
    AND f.airline_name = '{}'
GROUP BY (a.name)
ORDER BY times DESC
LIMIT 3;


-- 
SELECT c.name,
    COUNT(p.ticket_id) AS trips,
    SUM(f.price),
    c.email
FROM purchases p
    JOIN customer c ON p.customer_email = c.email
    JOIN ticket t ON t.id = p.ticket_id
    JOIN flight f ON (
        f.flight_num = t.flight_id
        AND f.airline_name = t.airline_name
    )
WHERE p.purchase_date >= DATE_SUB (CURDATE (), INTERVAL 1 YEAR)
GROUP BY (c.email)
ORDER BY trips DESC
LIMIT 1;


-- 
SELECT airline_name
FROM airline_staff
WHERE username = '{}';


-- 
SELECT *
FROM customer
WHERE email = '{}';


-- 
SELECT f.flight_num,
    f.airline_name,
    f.departure_airport_name,
    f.arrival_airport_name,
    f.departure_time,
    f.arrival_time,
    f.dep_status,
    p.customer_email
FROM purchases p
    JOIN ticket t ON t.id = p.ticket_id
    JOIN flight f ON (
        t.flight_id = f.flight_num
        AND t.airline_name = f.airline_name
    )
WHERE p.customer_email = '{}'
    AND f.airline_name = '{}';


-- 
SELECT name
FROM customer
WHERE email = '{}';


-- 
SELECT c.name,
    COUNT(p.ticket_id) AS trips,
    SUM(f.price),
    c.email
FROM purchases p
    JOIN customer c ON p.customer_email = c.email
    JOIN ticket t ON t.id = p.ticket_id
    JOIN flight f ON (
        f.flight_num = t.flight_id
        AND f.airline_name = t.airline_name
    )
WHERE p.purchase_date >= DATE_SUB (CURDATE (), INTERVAL 1 YEAR)
GROUP BY (c.email)
ORDER BY trips DESC
LIMIT 1;


-- 
SELECT airline_name
FROM airline_staff
WHERE username = '{}';


--
SELECT
SUM(f.price)
FROM purchases p
    JOIN ticket t ON t.id = p.ticket_id
    JOIN flight f ON (
        t.flight_id = f.flight_num
        AND t.airline_name = f.airline_name
    )
WHERE p.purchase_date >= DATE_SUB (CURDATE (), INTERVAL 1 MONTH)
    AND f.airline_name = '{}'
    AND p.booking_agent_id IS NULL;


-- 
SELECT SUM(f.price)
FROM purchases p
    JOIN ticket t ON t.id = p.ticket_id
    JOIN flight f ON (
        t.flight_id = f.flight_num
        AND t.airline_name = f.airline_name
    )
WHERE p.purchase_date >= DATE_SUB (CURDATE (), INTERVAL 1 YEAR)
    AND f.airline_name = '{}'
    AND p.booking_agent_id IS NULL;


-- 
SELECT SUM(f.price)
FROM purchases p
    JOIN ticket t ON t.id = p.ticket_id
    JOIN flight f ON (
        t.flight_id = f.flight_num
        AND t.airline_name = f.airline_name
    )
WHERE p.purchase_date >= DATE_SUB (CURDATE (), INTERVAL 1 MONTH)
    AND f.airline_name = '{}'
    AND p.booking_agent_id IS NOT NULL;


-- 
SELECT SUM(f.price)
FROM purchases p
    JOIN ticket t ON t.id = p.ticket_id
    JOIN flight f ON (
        t.flight_id = f.flight_num
        AND t.airline_name = f.airline_name
    )
WHERE p.purchase_date >= DATE_SUB (CURDATE (), INTERVAL 1 YEAR)
    AND f.airline_name = '{}'
    AND p.booking_agent_id IS NOT NULL;


-- 
SELECT airline_name
FROM airline_staff
WHERE username = '{}';


-- 
SELECT COUNT(*) AS tickets_sold,
    YEAR (P.purchase_date) AS year,
    MONTH (P.purchase_date) AS MONTH
FROM purchases AS P
    JOIN ticket AS T ON P.ticket_id = T.id
WHERE P.purchase_date >= '{}'
    AND P.purchase_date <= '{}'
    AND T.airline_name = '{}'
GROUP BY YEAR (P.purchase_date),
    MONTH (P.purchase_date)
ORDER BY YEAR (P.purchase_date),
    MONTH (P.purchase_date);


-- 
SELECT COUNT(*) AS tickets_sold,
    YEAR (P.purchase_date) AS year,
    MONTH (P.purchase_date) AS MONTH
FROM purchases AS P
    JOIN ticket AS T ON P.ticket_id = T.id
WHERE P.purchase_date >= DATE_SUB (CURDATE (), INTERVAL 1 YEAR)
    AND T.airline_name = '{}'
GROUP BY YEAR (P.purchase_date),
    MONTH (P.purchase_date)
ORDER BY YEAR (P.purchase_date),
    MONTH (P.purchase_date);


-- 
SELECT COUNT(*) AS tickets_sold,
    YEAR (P.purchase_date) AS year,
    MONTH (P.purchase_date) AS MONTH,
    DAY (P.purchase_date) AS DAY
FROM purchases AS P
    JOIN ticket AS T ON P.ticket_id = T.id
WHERE P.purchase_date >= DATE_SUB (CURDATE (), INTERVAL 1 MONTH)
    AND T.airline_name = '{}'
GROUP BY YEAR (P.purchase_date),
    MONTH (P.purchase_date),
    DAY (P.purchase_date)
ORDER BY YEAR (P.purchase_date),
    MONTH (P.purchase_date),
    DAY (P.purchase_date);


-- 
SELECT airline_name
FROM airline_staff
WHERE username = '{}';


-- 
SELECT flight_num
FROM flight
WHERE airline_name = '{}';


-- 
SELECT airline_name
FROM airline_staff
WHERE username = '{}';


-- 
SELECT DISTINCT c.email,
    c.name,
    c.date_of_birth,
    c.passport_country,
    c.passport_number
FROM purchases AS P
    JOIN ticket AS T ON P.ticket_id = T.id
    JOIN customer c ON c.email = P.customer_email
WHERE T.airline_name = '{}'
    AND T.flight_id = '{}'
ORDER BY c.name;


-- 
SELECT airline_name
FROM airline_staff
WHERE username = '{}';


-- 
SELECT flight_num
FROM flight
WHERE airline_name = '{}';


-- 
SELECT flight_num,
    airline_name,
    departure_airport_name,
    arrival_airport_name,
    departure_time,
    arrival_time,
    dep_status
FROM flight
WHERE departure_airport_name = '{}';


-- 
SELECT flight_num,
    airline_name,
    departure_airport_name,
    arrival_airport_name,
    departure_time,
    arrival_time,
    dep_status
FROM flight
WHERE arrival_airport_name = '{}';


-- 
SELECT flight_num,
    airline_name,
    departure_airport_name,
    arrival_airport_name,
    departure_time,
    arrival_time,
    dep_status
FROM flight
WHERE DATE (departure_time) = '{}';


-- 
SELECT flight_num,
    airline_name,
    departure_airport_name,
    arrival_airport_name,
    departure_time,
    arrival_time,
    dep_status
FROM flight
WHERE flight_num = '{}';


-- 
SELECT flight_num,
    airline_name,
    departure_airport_name,
    arrival_airport_name,
    departure_time,
    arrival_time,
    dep_status
FROM flight
WHERE DATE (departure_time) = '{}';


-- 
SELECT DISTINCT arrival_airport_name
FROM flight;


-- 
SELECT DISTINCT departure_airport_name
FROM flight;


-- 
SELECT DISTINCT flight_num
FROM flight;


-- 
SELECT DISTINCT arrival_airport_name
FROM flight;


-- 
SELECT DISTINCT departure_airport_name
FROM flight;


-- 
SELECT DISTINCT flight_num
FROM flight;


-- 
SELECT airplane_id
FROM flight
WHERE airline_name = '{}'
    AND flight_num = '{}';


-- 
SELECT seats
FROM airplane
WHERE airline_name = '{}'
    AND id = '{}';


-- 
SELECT COUNT(*)
FROM ticket
WHERE airline_name = '{}'
    AND flight_id = '{}';


-- 
SELECT DISTINCT arrival_airport_name
FROM flight;


-- 
SELECT DISTINCT departure_airport_name
FROM flight;


-- 
SELECT DISTINCT flight_num
FROM flight;


-- 
SELECT airline_name
FROM booking_agent_work_for
WHERE email = '{}';


-- 
SELECT DISTINCT arrival_airport_name
FROM flight
WHERE airline_name = '{}';


-- 
SELECT DISTINCT departure_airport_name
FROM flight
WHERE airline_name = '{}';


-- 
SELECT DISTINCT flight_num
FROM flight
WHERE airline_name = '{}';


-- 
SELECT airplane_id
FROM flight
WHERE airline_name = '{}'
    AND flight_num = '{}';


-- 
SELECT seats
FROM airplane
WHERE airline_name = '{}'
    AND id = '{}';


-- 
SELECT COUNT(*)
FROM ticket
WHERE airline_name = '{}'
    AND flight_id = '{}';


-- 
SELECT price
FROM flight
WHERE flight_num = '{}'
    AND airline_name = '{}'
    AND departure_time = '{}';


-- 
SELECT COUNT(*)
FROM customer
WHERE email = '{}';


-- 
SELECT COUNT(*)
FROM ticket
WHERE customer_email = '{}'
    AND flight_id = '{}'
    AND airline_name = '{}';


-- 
INSERT INTO ticket (customer_email, airline_name, flight_id)
VALUES ('{}', '{}', '{}');


-- 
SELECT id
FROM ticket
WHERE customer_email = '{}'
    AND airline_name = '{}'
    AND flight_id = '{}';


-- 
INSERT INTO purchases (
        ticket_id,
        customer_email,
        booking_agent_id,
        purchase_date
    )
VALUES ('{}', '{}', '{}', CURDATE ());


-- 
INSERT INTO commission_per_agent (booking_agent_email, ticket_id, commission)
VALUES ('{}', '{}', '{}');


-- 
INSERT INTO tickets_by_booking_agent (booking_agent_email, ticket_id)
VALUES ('{}', '{}');


-- 
SELECT airline_name
FROM booking_agent_work_for
WHERE email = '{}';


-- 
SELECT DISTINCT F.departure_airport_name
FROM purchases AS P
    JOIN ticket AS T ON P.ticket_id = T.id
    JOIN flight F ON (
        T.flight_id = F.flight_num
        AND T.airline_name = F.airline_name
    )
WHERE F.airline_name = '{}'
    AND P.booking_agent_id = '{}' -- 
SELECT DISTINCT F.departure_airport_name
FROM purchases AS P
    JOIN ticket AS T ON P.ticket_id = T.id
    JOIN flight F ON (
        T.flight_id = F.flight_num
        AND T.airline_name = F.airline_name
    )
WHERE F.airline_name = '{}'
    AND P.booking_agent_id = '{}' -- 
SELECT F.airline_name,
    F.flight_num,
    F.departure_airport_name,
    F.departure_time,
    F.arrival_airport_name,
    F.arrival_time,
    F.dep_status,
    T.customer_email
FROM purchases AS P
    JOIN ticket AS T ON P.ticket_id = T.id
    JOIN flight F ON (
        T.flight_id = F.flight_num
        AND T.airline_name = F.airline_name
    )
WHERE
    AND F.dep_status = 'Upcoming';


-- 
SELECT SUM(cpa.commission) / COUNT(DISTINCT p.ticket_id) AS avg_commission_per_ticket
FROM purchases p
    JOIN ticket t ON t.id = p.ticket_id
    JOIN commission_per_agent cpa ON (
        t.id = cpa.ticket_id
        AND cpa.booking_agent_email = p.booking_agent_id
    )
WHERE cpa.booking_agent_email = '{}'
    AND p.purchase_date >= DATE_SUB (CURDATE (), INTERVAL 1 MONTH);


-- 
SELECT COUNT(DISTINCT p.ticket_id)
FROM purchases p
    JOIN ticket t ON t.id = p.ticket_id
    JOIN commission_per_agent cpa ON (
        t.id = cpa.ticket_id
        AND cpa.booking_agent_email = p.booking_agent_id
    )
WHERE cpa.booking_agent_email = '{}'
    AND p.purchase_date >= DATE_SUB (CURDATE (), INTERVAL 1 MONTH);


-- 
SELECT SUM(cpa.commission) / COUNT(DISTINCT p.ticket_id) AS avg_commission_per_ticket
FROM purchases p
    JOIN ticket t ON t.id = p.ticket_id
    JOIN commission_per_agent cpa ON (
        t.id = cpa.ticket_id
        AND cpa.booking_agent_email = p.booking_agent_id
    )
WHERE cpa.booking_agent_email = '{}'
    AND p.purchase_date >= '{}'
    AND p.purchase_date <= '{}';


-- 
SELECT COUNT(DISTINCT p.ticket_id)
FROM purchases p
    JOIN ticket t ON t.id = p.ticket_id
    JOIN commission_per_agent cpa ON (
        t.id = cpa.ticket_id
        AND cpa.booking_agent_email = p.booking_agent_id
    )
WHERE cpa.booking_agent_email = '{}'
    AND p.purchase_date >= '{}'
    AND p.purchase_date <= '{}';


-- 
SELECT SUM(cpa.commission)
FROM purchases p
    JOIN ticket t ON t.id = p.ticket_id
    JOIN commission_per_agent cpa ON (
        t.id = cpa.ticket_id
        AND cpa.booking_agent_email = p.booking_agent_id
    )
WHERE cpa.booking_agent_email = '{}'
    AND p.purchase_date >= DATE_SUB (CURDATE (), INTERVAL 1 MONTH);


-- 
SELECT SUM(cpa.commission) / COUNT(DISTINCT p.ticket_id) AS avg_commission_per_ticket
FROM purchases p
    JOIN ticket t ON t.id = p.ticket_id
    JOIN commission_per_agent cpa ON (
        t.id = cpa.ticket_id
        AND cpa.booking_agent_email = p.booking_agent_id
    )
WHERE cpa.booking_agent_email = '{}'
    AND p.purchase_date >= DATE_SUB (CURDATE (), INTERVAL 1 MONTH);


-- 
SELECT COUNT(DISTINCT p.ticket_id)
FROM purchases p
    JOIN ticket t ON t.id = p.ticket_id
    JOIN commission_per_agent cpa ON (
        t.id = cpa.ticket_id
        AND cpa.booking_agent_email = p.booking_agent_id
    )
WHERE cpa.booking_agent_email = '{}'
    AND p.purchase_date >= DATE_SUB (CURDATE (), INTERVAL 1 MONTH);


--
SELECT
airline_name
FROM booking_agent_work_for
WHERE email = '{}' --  
SELECT t.customer_email,
    SUM(cpa.commission) AS total_commission_per_customer
FROM commission_per_agent cpa
    JOIN ticket t ON t.id = cpa.ticket_id
    JOIN purchases p ON t.id = p.ticket_id
WHERE cpa.booking_agent_email = '{}'
    AND p.purchase_date >= DATE_SUB (NOW (), INTERVAL 6 MONTH)
GROUP BY t.customer_email
ORDER BY SUM(cpa.commission) DESC
LIMIT 5;


-- 
SELECT t.customer_email,
    COUNT(t.id) AS total_tickets_per_customer
FROM ticket t
    JOIN purchases p ON t.id = p.ticket_id
WHERE p.booking_agent_id = '{}'
    AND p.purchase_date >= DATE_SUB (NOW (), INTERVAL 6 MONTH)
GROUP BY t.customer_email
ORDER BY COUNT(t.id) DESC
LIMIT 5;


-- 
SELECT COUNT(*)
FROM ticket
WHERE customer_email = '{}'
    AND flight_id = '{}'
    AND airline_name = '{}';


-- 
INSERT INTO ticket (customer_email, airline_name, flight_id)
VALUES ('{}', '{}', '{}');


-- 
SELECT id
FROM ticket
WHERE customer_email = '{}'
    AND airline_name = '{}'
    AND flight_id = '{}';


-- 
INSERT INTO purchases (ticket_id, customer_email, purchase_date)
VALUES ('{}', '{}', CURDATE ());


-- 
SELECT SUM(F.price) AS money_spent_per_month,
    YEAR (P.purchase_date) AS year,
    MONTH (P.purchase_date) AS MONTH
FROM purchases AS P
    JOIN ticket AS T ON P.ticket_id = T.id
    JOIN flight AS F ON F.flight_num = T.flight_id
WHERE P.customer_email = '{}'
    AND P.purchase_date BETWEEN '{}' AND '{}'
GROUP BY YEAR (P.purchase_date),
    MONTH (P.purchase_date)
ORDER BY YEAR (P.purchase_date),
    MONTH (P.purchase_date);


-- 
SELECT SUM(F.price) AS money_spent_per_month,
    YEAR (P.purchase_date) AS year,
    MONTH (P.purchase_date) AS MONTH
FROM purchases AS P
    JOIN ticket AS T ON P.ticket_id = T.id
    JOIN flight AS F ON F.flight_num = T.flight_id
WHERE P.customer_email = '{}'
    AND P.purchase_date >= DATE_SUB (NOW (), INTERVAL 6 MONTH)
GROUP BY YEAR (P.purchase_date),
    MONTH (P.purchase_date)
ORDER BY YEAR (P.purchase_date),
    MONTH (P.purchase_date);


- -