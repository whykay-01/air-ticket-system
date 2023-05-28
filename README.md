## Overview

This repository contains a reservation system that is currently in development. Once the functionality is fully implemented, the documentation and corresponding user guide (including installation procedures) will be updated.

I am currently working on reorganizing the structure of the project, so if you want to help me with that -- be my guest and submit a pull request. I would be very glad to review it!

## Prerequisites

Before deploying the system, ensure that the following prerequisites are met:

- Docker is installed on your system (version does not matter)
- The MySQL image is available on your Docker. Refer to the docker-compose.yml file for details.
- A .env file is created in the cloned repository (in the main folder), and the following parameters are set manually:
  - MYSQL_ROOT_PASSWORD=<your_password>
  - MYSQL_DATABASE=<the_name_of_your_database>
- DataGrip is recommended for database management, but you can choose any preferred method.
- Bootstrap library is installed on your local machine (https://getbootstrap.com/)

## Deployment

To deploy the system, follow these steps:

1. Start the Docker image of the MySQL server.
2. Create the database and run the create_tables.sql file, then insert_data.sql to populate the database with mock data.
3. In the flask_app.py file, run the file manually to start the system. The system can be accessed at http://127.0.0.1:5000. If you encounter any errors, check if your port 5000 is available.

## System Requirements

The reservation system requires the following components:

- Docker image of MySQL server
- Python 3 and Flask Python library, along with other relevant packages, installed on your system
- Bootstrap library installed on your local machine

## Contributions

If you have any suggestions or ideas on how to improve the project, please contact the project owner or submit an issue describing your suggestion or concern in detail. Contributions are welcome.

## License

This project is licensed under the MIT license. See MIT Licence for more details.

## Things to mention:

1. JS script to handle password confirmation
2. Commit statements only in the end (after all the intermediary queries have been sucessfully executed)
3. No SQL injections possible, as all the queries are pre-written, static strings
4. Solo work for the whole project
5. Easy to deploy 
6. New technology of using Docker image for the database deployment
7. Front end design
8. One more "permission" in the airline_staff N/A for security reasons
9. The newly registered booking agent cannot view anything until they are approved by the airline staff

