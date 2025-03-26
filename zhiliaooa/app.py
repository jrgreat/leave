from flask import Flask,request, render_template, jsonify, session, g, url_for
from db.mysql import get_db_instance, execut_select_sql, execute_sql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from blueprint.qa import qa as qa_bp
from blueprint.auth import auth as auth_bp
from flask_mail import Mail
import config


app = Flask(__name__)
app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)
app.config['MAIL_SERVER'] = "smtp.qq.com"
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "214365024@qq.com"
app.config['MAIL_PASSWORD'] = "ftmnofudvxddbgfg"
app.config['MAIL_DEFAULT_SENDER'] = "214365024@qq.com"
app.secret_key = config.SECRET_KEY
mail = Mail(app)

@app.before_request
def my_before_request():
    user_id = session.get("user_id")
    if user_id:
        sql = "select * from users where id=USER_ID"
        sql = sql.replace("USER_ID", str(user_id))
        db = get_db_instance()
        result = execut_select_sql(db, sql)
        if len(result) > 0:
            setattr(g, 'user', {"username":result[0]['name']})
        else:
            setattr(g, 'user', None)
    else:
        setattr(g, 'user', None)
    

@app.context_processor
def my_context_processor():
    my_dict = {"user": g.user}
    return my_dict




if __name__=="__main__":
    app.run(debug=True)