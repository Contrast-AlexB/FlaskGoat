from flask import Flask

from blueprints import routes

#Setup App
app = Flask(__name__, instance_relative_config=True)

#Setup Routes
app.register_blueprint(routes.router)


if __name__ == "__main__":
    app.run()

