from flask import Flask, render_template
from app.webhook.routes import webhook
from app.extensions import mongo


# Creating our flask app
def create_app():

    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/venkytask"
    mongo.init_app(app)
    # registering all the blueprints
    app.register_blueprint(webhook)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
