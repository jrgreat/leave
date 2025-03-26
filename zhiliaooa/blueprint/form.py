import wtforms
from db.mysql import get_db_instance, execute_sql, execut_select_sql
from wtforms.validators import Email,Length, EqualTo, InputRequired

class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="format of email is not correct")])
    captcha = wtforms.StringField(validators=[Length(min=4,max=4, message="format of verification code is not correct")])
    username = wtforms.StringField(validators=[Length(min=3,max=20, message="format of user is not correct")])
    password = wtforms.StringField(validators=[Length(min=6,max=20, message="format of password is not correct")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])

    #to avoid duplicate username, need access db.
    def check_duplicate_username(self, field):
        db = get_db_instance()
        sql = 'select DISTINCT count(1) as number from TABLE_NAME where email="EMAIL"'
        sql = sql.replace("TABLE_NAME", "users")
        sql = sql.replace("EMAIL", field.data)
        result = execut_select_sql(db, sql)
        if result[0]['number'] != 0:
            raise Exception("the mailbox had been created already!")
        
    def check_duplicate_captcha(self, field):
        email = self.email.data
        captcha = field.data
        db = get_db_instance()
        sql = 'select DISTINCT count(1) as number from TABLE_NAME where email="EMAIL" and captcha="CAPTCHA"'
        sql = sql.replace("TABLE_NAME", "email_captcha")
        sql = sql.replace("EMAIL", email)
        sql = sql.replace("CAPTCHA", captcha)
        result = execut_select_sql(db, sql)
        if result[0]['number'] == 0:
            raise Exception("the captcha and mailbox had been created already!")    
        
    def validate(self, extra_validators = None):
        return super().validate(extra_validators)

class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="format of email is not correct")])
    password = wtforms.StringField(validators=[Length(min=6,max=20, message="format of password is not correct")])

    def check_email_exist(self, field):
        db = get_db_instance()
        sql = 'select DISTINCT count(1) as number from TABLE_NAME where email="EMAIL"'
        sql = sql.replace("TABLE_NAME", "users")
        sql = sql.replace("EMAIL", field.data)
        result = execut_select_sql(db, sql)
        if result[0]['number'] == 0:
            raise Exception("email doesn't exist!")
        
    def verify_passwd(self, field1, field2):
        db = get_db_instance()
        sql = 'select id, password from users where email="EMAIL"'
        sql = sql.replace("EMAIL", field1.data)
        result = execut_select_sql(db, sql)
        if result[0]['password'] != field2.data:
            raise Exception("password of user {} is not correct!".format(field1.data))   
        else:
            return result[0]['id']   
        
    def validate(self, extra_validators = None):
        return super().validate(extra_validators)

class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[Length(min=1,max=200, message="format of title is not correct")])
    content = wtforms.StringField(validators=[Length(min=3, message="format of content is not correct")])

class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[Length(min=3, message="format of content is not correct")])  
    question_id = wtforms.IntegerField(validators=[InputRequired(message="must input question id")]) 
        


