# altran-docker-compose
This is a Docker compose exercise made for the Altran Docker workshop.

## Project structure
### Database
A MySQL database consisting of one table with some movies (see database/database.sql).

### Webapp
The webapp retrieves the movies from the database and shows them in a HTML page. This webapp is build using Flask (a Python Microframework).

## Exercise
## 1. Running the database and webapp
First create a separate network for the database and webapp by running: `docker network create --driver bridge altran-docker-compose`.

Build the images by running:
* Database: `docker build -t altran-docker-compose-database database`.
* Webapp: `docker build -t altran-docker-compose-webapp webapp`.

Start the containers by running:
* Database: `docker run -it --name database --rm --net=altran-docker-compose -e MYSQL_ROOT_PASSWORD=movie123 altran-docker-compose-database`.
* Webapp: `docker run -it --name webapp --rm --net=altran-docker-compose -p 8080:80 altran-docker-compose-webapp`.

Open your browser and go to http://localhost:8080. You will now see the movies from the database displayed by the webapp.

## 2. Running with Docker Compose
To run the containers you had to execute 5 commands. It would be easier if we only had to execute one command. We can achieve this by using Docker Compose.

### Creating a docker-compose.yml
Create a docker-compose.yml file to run the webapp and the database. Information on how to create such a file can be found here:
* https://docs.docker.com/compose/overview/
* https://docs.docker.com/compose/compose-file/compose-file-v2/

Once your created the docker-compose.yml file, run:
```
docker-compose build
docker-compose up
```

### Solution
A working docker-compose.yml file is in solution.zip (but of course it's password protected ;))
