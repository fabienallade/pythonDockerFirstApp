import os
from flask_migrate import Migrate
from application import init,models
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from redis import Redis

app = init.create_app()
db = SQLAlchemy(app)

migrate = Migrate(app, db)
# db.init_app(app)
migrate.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)