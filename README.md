**The documentation, and the corresponding user guide (including installation procedures) will be updated respectively after the functionality is fully implemented**

Prereqs you need to succesfully deploy this system:

1. Docker intalled on your system (version does not matter)
2. The MySQL image on your Docker. Check out the docker-compose.yml file. (INSERT THE COMMAND ONE NEED TO RUN TO START THIS)
3. Create a .env file in the cloned repo (in the main folder), and manually set the following params:
   MYSQL_ROOT_PASSWORD= <your_password>
   MYSQL_DATABASE=<the_name_of_your_database> --> in the case of my repo it's reservation_system
4. I am using DataGrip for the database management environment, so I recommend you use this way of accessing your data, but feel free to choose the preffered way of doing this
5. Once 1-4 is satisfied, please start the Docker image of the MySQL, create the database, and manually run the create_tables.sql file first, and inserting_data.sql after. This way you will have some mock data to play around with
6. After you are done with 1-5, go to the flask_app.py, and manually run the file. After that the system could be accessed here: http://127.0.0.1:5000 (if you have any errors popping up, that might be because your port 5000 might not be available)

System requirements:

1. Docker image of MySQL server
2. Python3 and Flask python library, and other relevant packages installed on your system
3. Bootstrap library installed on your local machine (https://getbootstrap.com/)

**To use the docker use the following command after the docker is setted up**
docker compose up

Contributions:

If you have any suggestions / ideas on how to improve the project, please contact me, or submit an issue describing in detail what your suggestion / concert is.
