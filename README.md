# docker-compose-exercise
This is a Docker compose exercise made for the Capgemini Engineering Docker workshop.

## Project structure
### Database
A MySQL database consisting of one table with some movies (see database/database.sql).

### Webapp
The webapp retrieves the movies from the database and shows them in a HTML page. This webapp is build using Flask (a Python Microframework).

## Exercise
## 1. Running the database and webapp
First create a separate network for the database and webapp by running: `docker network create --driver bridge docker-compose-exercise`

Start the containers by running:
* Database: `docker run -d --name database --net=docker-compose-exercise -e MYSQL_ROOT_PASSWORD=movie123 koenkk/docker-compose-exercise-database`
* Webapp: `docker run -d --name webapp --net=docker-compose-exercise -p 8080:80 koenkk/docker-compose-exercise-webapp`

Open your browser and go to http://localhost:8080. You will now see the movies from the database displayed by the webapp.

Note: The images are being pulled from https://hub.docker.com/ (https://hub.docker.com/r/koenkk/docker-compose-exercise-webapp/ and https://hub.docker.com/r/koenkk/docker-compose-exercise-database/)

## 2. Running with Docker Compose
To run the containers you had to execute 3 commands. It would be easier if we only had to execute one command. We can achieve this by using Docker Compose.

### Creating a docker-compose.yml
Create a docker-compose.yml file to run the webapp and the database. Information on how to create such a file can be found here:
* https://docs.docker.com/compose/overview/
* https://docs.docker.com/compose/compose-file/

Once your created the docker-compose.yml file, run:
```
docker-compose up
```
