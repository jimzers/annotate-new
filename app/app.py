from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import db_username, db_password, db_host, db_name

app = Flask(__name__)

db_uri = 'mysql+pymysql://' + db_username + ":" + db_password + "@" + db_host + "/" + db_name
#print(db_uri)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
