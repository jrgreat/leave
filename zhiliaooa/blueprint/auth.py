from flask import Blueprint, render_template, request, jsonify, url_for, redirect, session
from flask_mail import Message
from db.mysql import get_db_instance,execute_sql, execut_select_sql
from .form import RegisterForm, LoginForm
from exts import mail
import time
import config 
import datetime
import string
import random
auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/cleardb")
def cleardb():
    
    for sql in ["TRUNCATE table email_captcha","TRUNCATE table users"]:
        db = get_db_instance()
        execute_sql(db, sql)
    return "done"


@auth.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        r_form = LoginForm(request.form)
        if r_form.validate():
            r_form.check_email_exist(r_form.email)
            try:
                user_id = r_form.verify_passwd(r_form.email, r_form.password)
            except Exception as e:
                print(e)
                return redirect(url_for("auth.login"))
            session['user_id'] = user_id
            return redirect(url_for("qa.index"))
        else:
            print(r_form.errors)
            return redirect(url_for("auth.login"))



@auth.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        r_form = RegisterForm(request.form)
        if r_form.validate():
            db = get_db_instance()
            r_form.check_duplicate_captcha(r_form.captcha) 
            r_form.check_duplicate_username(r_form.email)
            sql = "insert into TABLE_NAME (name, email, join_time, password) VALUES ('NAME','EMAIL', 'JOIN_TIME', 'PASSWORD' )"
            sql = sql.replace("TABLE_NAME", "users", 1)
            sql = sql.replace("NAME", r_form.username.data)
            sql = sql.replace("EMAIL", r_form.email.data)
            sql = sql.replace("PASSWORD", r_form.password.data)
            now = datetime.datetime.now()
            now = now.strftime("%Y-%m-%d %H:%M:%S")
            sql = sql.replace("JOIN_TIME", now)
            execute_sql(db, sql)
            return redirect(url_for("auth.login"))
        else:
            print(r_form.errors)
            return redirect(url_for("auth.register"))


@auth.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@auth.route("/captcha/email", methods =['GET','POST'])
def get_email_captcha():
    # / captcha/email?email=xxx@qq.com
    email = request.args.get("email")
    source = string.digits * 4
    captcha = random.sample(source, 4)
    captcha = "".join(captcha)
    message = Message("verification code", recipients=[email], body="your verify code is {}".format(captcha))
    mail.send(message)
    sql = "insert into TABLE_NAME (email, captcha) VALUES ('EMAIL', 'CAPTCHA' )"
    sql = sql.replace("TABLE_NAME", config.DB_TABLE_EMAIL_CAPTCHA, 1)
    sql = sql.replace("EMAIL", email, 1)
    sql = sql.replace("CAPTCHA", captcha, 1)
    mysql_db  = get_db_instance()
    execute_sql(mysql_db, sql)
    return jsonify({"code":200, "message":"", "data":None})
    

@auth.route("/mail/test")
def mail_test():
    message = Message("mail test", recipients=["great2000_1@163.com"], body="test_mail")
    mail.send(message)
    return "mail test done!"