from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    done = db.Column(db.Boolean)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create-task', methods=['POST'])
def create():
    Task(content = request.form['content'], done=False) 
    #db.session.add()


if __name__ == '__main__':
    app.run(debug=True)
