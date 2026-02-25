from flask import Flask
from extension import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret1234'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost:3306/db_tareas"
# initialize the app with the extension
db.init_app(app)
from models import Tarea
with app.app_context():
    db.create_all()
from routes import *

if __name__ == '__main__':
    app.run(debug=True)
    
