## Overview

This repository contains a reservation system that is currently in development. Once the functionality is fully implemented, the documentation and corresponding user guide (including installation procedures) will be updated

## Prerequisites

Before deploying the system, ensure that the following prerequisites are met:

- Docker is installed on your system (version does not matter)
- The MySQL image is available on your Docker. Refer to the docker-compose.yml file for details.
- A .env file is created in the cloned repository (in the main folder), and the following parameters are set manually:
  - MYSQL_ROOT_PASSWORD=<your_password>
  - MYSQL_DATABASE=<the_name_of_your_database> (in the case of this repository, it's "reservation_system")
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
