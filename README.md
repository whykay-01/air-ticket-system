## Overview

This repository contains codebase fot the airline ticket reservation system. The system is built using Python 3 and Flask framework, and the database is deployed using Docker image of MySQL server. 

The system is designed to be used by three types of users: airline staff, booking agent, and customer. 

The airline staff can add new flights, view the list of flights, and view the list of customers on a specific flight. Apart from that, airline staff who have the admin access can add / delete / modify the booking agents, view the top customers, and view the commission. Also, they could add new airports and view the list of airports. 

The booking agent can book a flight for a customer, view the top customers, and view their own commission for the specified period of time. 

The customer can search flights, book flights, and view their own flight history. 

The system is designed and intended to be user-friendly and easy to deploy. The front-end design is based on Bootstrap library.

I am currently working on reorganizing the structure of the project, so if you want to help me with that -- be my guest and submit a pull request. I would be very glad to review it!

## Prerequisites

Before deploying the system, ensure that the following prerequisites are met:

- Docker is installed on your system (latest version should be fine)
- MySQL image is installed on your Docker. Use the docker-compose.yml file to create an image of the SQL server.
- A .env file is created in the cloned repository (in the main folder), and the following parameters are set manually (refer to `.env.example` file for more information):
  - MYSQL_ROOT_PASSWORD=<your_password>
  - MYSQL_DATABASE=<the_name_of_your_database> (in our case, in the create_tables.sql file, the database name is set as "reservation_system")
- DataGrip is recommended for database management, but you can choose any other GUI to interact with the data.
- [Bootstrap-3.4] (https://getbootstrap.com/docs/3.4/getting-started/) library is installed on your local machine

Note: the database we refer to is stored in other/database_design/create_tables.sql file. The database is created using the SQL script, and the mock data is inserted using the insert_data.sql file in the same folder. 

You could run those files manually to create the database and populate it with mock data.

## Deployment

To deploy the system, follow these steps:

Note: the following commands are for Mac OS. If you are using Windows, please refer to the official documentation of Python 3 and Docker.

Note: Please ensure that you are in the main folder of the cloned repository prior to running any commands.

```bash
cd air-ticket-system
```

Now let's create your own virtual environment:

```bash
python3 -m venv .venv
```

Now make sure that you are in the virtual environment by running the following command:

```bash
source venv/bin/activate
```

Once you are in the virtual environment, install the required packages:

```bash
pip install -r requirements.txt
```

Now, as all the prereqs are met, let's deploy the system itself:

1. Create the Docker Image of the MySQL server using the docker-compose.yml file. The image will be created automatically.

```bash
docker-compose up
```

2. Run the Docker Container of the MySQL server that was earlier created by the Docker Image.

```bash
docker-compose start
```

3. Create the database and run the create_tables.sql file, then insert_data.sql to populate the database with mock data. To do this simply go to your SQL GUI and run the files manually. I was in a rush, so I didn't have time to automate this process. Sorry :) 

3. In the flask_app.py file, run the file manually to start the system. The system can be accessed at http://127.0.0.1:5000. If you encounter any errors, check if your port 5000 is available. Again, I was in a rush, so I didn't have time to automate this process.

## Contributions

If you have any suggestions or ideas on how to improve the project, please contact the project owner or submit an issue describing your suggestion or concern in detail. Contributions are welcome.

## License

This project is licensed under the MIT license. See MIT Licence for more details.

## Things to mention:

1. I have some JS scripts which handle password confirmation
2. In the app, all the commit statements appear only in the end (after all the intermediary queries have been sucessfully executed)
3. Security concerns: no SQL injections would be possible, as all the queries are pre-written, static strings
4. Contributors: there are no contributors, I worked alone for this project.
5. Easy to deploy 
6. New technology of using Docker image for the database deployment
7. Front end is based on Bootstrap library
8. One more "permission" in the airline_staff N/A for security reasons
9. The newly registered booking agent cannot view anything until they are approved by the airline staff
