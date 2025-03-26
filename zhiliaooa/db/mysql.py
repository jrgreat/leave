import pymysql
import datetime


HOSTNAME="192.168.121.131"
PORT="3306"
USERNAME="root"
PASSWORD="123456"
DATABASE="zhiliaooa"

BUILD_USER_TABLE="CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(100), email VARCHAR(200), \
    join_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP); commit;"

BUILD_CAPTCHA_TABLE = "CREATE TABLE email_captcha (id INT PRIMARY KEY, email VARCHAR(200), captcha  VARCHAR(200));commit;"

BUILD_QUESTION_TABLE = "CREATE TABLE question ( id INT PRIMARY KEY, title VARCHAR(200), content  TEXT, create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, author_id INT, FOREIGN KEY (author_id) REFERENCES users(id));commit;"

BUILD_ANSWER_TABLE = "CREATE TABLE answer ( \
    id INT PRIMARY KEY, \
    content  TEXT, \
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
    author_id INT, \
    question_id INT, \
    FOREIGN KEY (author_id) REFERENCES users(id), \
    FOREIGN KEY (question_id) REFERENCES question(id));commit;"

def get_db_instance(hostname=HOSTNAME, port=PORT, user=USERNAME, passwd=PASSWORD, db=DATABASE):
    conn = pymysql.connect(host=hostname, port=int(port), user=user, passwd=passwd, db=db, charset='utf8mb4')
    return conn

def execute_sql(db, sql):
    print("sql is :[{}]".format(sql))
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

def execut_select_sql(db, sql):
    print("sql is :[{}]".format(sql))
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    row = cursor.fetchall()
    cursor.close()
    db.close()    
    return row




if __name__=="__main__":
    user_email = "great2000_1@163.com"
    db = get_db_instance()
    sql = 'select id from users where email="'+user_email+'"'
    result = execut_select_sql(db, sql)
    pass
