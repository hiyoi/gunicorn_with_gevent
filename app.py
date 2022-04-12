import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.pool import NullPool, QueuePool


db = SQLAlchemy(session_options={'autocommit': True, 'autoflush': True},
                engine_options={'poolclass': QueuePool})

SQLALCHEMY_POOL_SIZE = 100
SQLALCHEMY_DATABASE_URI = \
    "postgresql://postgres:postgres@localhost:5432/postgres"
SQLALCHEMY_TRACK_MODIFICATIONS = False


def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)
    db.init_app(app)

    @app.route('/')
    def index():
        time.sleep(1)
        return 'ok'

    @app.route('/db')
    def query():
        db.session.execute('SELECT pg_sleep(1)')
        return 'done'

    return app


app = create_app()


if __name__ == '__main__':
    create_app().run()
