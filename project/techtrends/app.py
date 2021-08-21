import sqlite3
import logging

from flask import (
    Flask,
    jsonify,
    json,
    render_template,
    request,
    url_for,
    redirect,
    flash,
)
from werkzeug.exceptions import abort

db_connection_count = 0
post_count = 0

# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row
    global db_connection_count
    db_connection_count += 1
    return connection


# Function to get a post using its ID
def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    connection.close()
    return post


# Define the Flask application
app = Flask(__name__)
app.config["SECRET_KEY"] = "your secret key"

# Logging configuration
FORMAT = "%(levelname)s:%(module)s:%(asctime)s, %(message)s"
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format=FORMAT,
    datefmt=("%m/%d/%Y, %H:%M:%S"),
)

# Define the main route of the web application
@app.route("/")
def index():
    connection = get_db_connection()
    posts = connection.execute("SELECT * FROM posts").fetchall()
    global post_count
    post_count = len(posts)
    connection.close()
    return render_template("index.html", posts=posts)


# Define how each individual article is rendered
# If the post ID is not found a 404 page is shown
@app.route("/<int:post_id>")
def post(post_id):
    post = get_post(post_id)
    if post is None:
        logging.error("Attempted to retrieve non-existing article.")
        return render_template("404.html"), 404
    else:
        logging.info('Article "%s" retrieved!', post["title"])
        return render_template("post.html", post=post)


# Define the About Us page
@app.route("/about")
def about():
    logging.info('"About Us" page retrieved!')
    return render_template("about.html")


# Define the post creation functionality
@app.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if not title:
            flash("Title is required!")
        else:
            connection = get_db_connection()
            connection.execute(
                "INSERT INTO posts (title, content) VALUES (?, ?)", (title, content)
            )
            connection.commit()
            connection.close()
            logging.info('New article "%s" created!', title)
            return redirect(url_for("index"))

    return render_template("create.html")


# Define route for status checking
@app.route("/healthz")
def status():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype="application/json",
    )
    return response


# Define route for posts and connections metrics
@app.route("/metrics")
def metrics():
    response = app.response_class(
        # TODO: Create/Look for function to get these values
        response=json.dumps(
            {
                "db_connection_count": db_connection_count,
                "post_count": post_count,
            }
        ),
        status=200,
        mimetype="application/json",
    )
    return response


# start the application on port 3111
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="3111")
