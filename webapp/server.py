from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Setup the connection to the database
db = SQLAlchemy()
db_uri = 'mysql://root:movie123@database:3306/movies'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


def get_movies():
    """
    Retrieves all movies from the database.
    """
    movies = []

    for row in db.engine.execute("SELECT * FROM movies"):
        movies.append({"name": row[0], "rating": row[1]})

    return movies


def render_movie_li(movies):
    """
    Creates a HTML list (<li>) of all movies.
    """
    html = ""

    for movie in movies:
        html = html + """
            <li class="list-group-item">
                <span class="badge">%s
                    <span class="glyphicon glyphicon-star"></span>
                </span>
                %s
            </li>
        """ % (movie['rating'], movie['name'])

    return html


@app.route('/')
def index():
    """
    This method is called upon opening the webapp.
    """
    movies = get_movies()
    movies_li = render_movie_li(movies)

    # Read the index.html and add the movies_li to it.
    return open('index.html').read() % (movies_li)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
