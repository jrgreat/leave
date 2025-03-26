from flask import Flask,request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from utilities.utility import *

app = Flask(__name__)


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


@app.route("/blog/<int:blog_id>")
def blog_list(blog_id):
    return render_template("details.html", blog_id=blog_id, user_name="zhangsan")

@app.route("/blog/list")
def page_blog_list():
    page = request.args.get("page", 1, int)

    return "you are accesing blog/page: {}".format(page)
"""
@app.route('/')
def hello_world():
    return 'Hello,World'

"""

def customize_filter(value):
    return "hello,world!, customized filter is working now!"

app.add_template_filter(customize_filter, "j_customize_filter")



@app.route('/')
def show_main_page():
    user = User("知了","xxxx@qq.com")
                
    return render_template("index.html", j_user=user.username, j_email=user.email)

@app.route('/filter')
def filter_demo():
    user = User("知了","xxxx@qq.com")
    return render_template("filter.html", j_user=user)

@app.route('/control/<int:age>')
def control_statement(age):
    #age = 17
    books = [{"name":"三国志", "author":"陈寿"}, 
             {"name":"西游记", "author":"吴承恩"},
             {"name":"水浒","author":"施耐庵"}
             ]
    return render_template("control.html", j_age = age, j_books = books)


@app.route('/child1')
def child1():
    return render_template('child1.html')

@app.route('/child2')
def child2():
    return render_template('child2.html')

@app.route('/static')
def static_demo():
    return render_template("static.html")

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

db=SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

user = User(username="张三", password="111111")



with app.app_context():
    with db.engine.connect() as conn:
        rs = conn.execute(text("select 1"))
        print(rs.fetchone())
        db.create_all()


@app.route("/usr/add")
def add_user():
    user1 = User(username="张三", password="111111")
    user2 = User(username="李四", password="111111")
    for usr in [user1, user2]:
        db.session.add(usr)
        db.session.commit()
    return "user add done!"

@app.route("/usr/query")
def query_user():
    user = User.query.get(1)
    print(user.id, user.username, user.password)
    users = User.query.filter_by(username="张三")
    for usr in users:
        print(usr.id, usr.username, usr.password)
    return render_template("data_show.html", j_users = users)

@app.route("/usr/update")
def update_user():
    user = User.query.filter_by(username="李四").first()
    user.password = "222222"
    db.session.commit()
    return "update user done"

@app.route("/usr/delete")
def delete_user():
    user = User.query.filter_by(username="李四").first()
    db.session.delete(user)
    db.session.commit()
    return "delete user done"

if __name__=="__main__":


    app.run()