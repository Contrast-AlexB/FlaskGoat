from flask import Flask

from blueprints.routes import navRoutes, viewRoutes
from views import cmdi


#Setup App
app = Flask(__name__, instance_relative_config=True)

#Setup Routes
app.register_blueprint(navRoutes.router)
app.register_blueprint(viewRoutes.router)


if __name__ == "__main__":
    app.run(debug=True)

