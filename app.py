from flask import Flask

# blue print imports
from routes.main_bp import main_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
