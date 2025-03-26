from flask import Blueprint, redirect,request,session,render_template,g, url_for
from db.mysql import get_db_instance,execute_sql, execut_select_sql
from .form import QuestionForm, AnswerForm
from decorator import login_required
import datetime
qa = Blueprint("qa", __name__, url_prefix="/")


def get_user_id():
    if g.user:
        user_email = g.user['username']
        db = get_db_instance()
        sql = 'select id from users where email="'+user_email+'"'
        id_row = execut_select_sql(db, sql)
        user_id = id_row[0]['id']
        return user_id 
    else:
        return -1   


@qa.route("/")
def index():
    sql = 'select * from question'
    db = get_db_instance()
    result = execut_select_sql(db, sql)

    return render_template("index.html", questions = result)

@qa.route("/qa/public_question", methods=["GET", "POST"])
@login_required
def public_question():
    if not g.user:
        return redirect(url_for("auth.login"))
    if request.method == "GET":
        return render_template("public_question.html")
    else:
        r_form = QuestionForm(request.form)
        if r_form.validate():
            user_id = get_user_id()
            sql = "insert into question (title, content, create_time, author_id) VALUES ('TITLE','CONTENT', 'CREATE_TIME', 'AUTHOR_ID' )"
            sql = sql.replace("TITLE", r_form.title.data)
            sql = sql.replace("CONTENT", r_form.content.data)
            now = datetime.datetime.now()
            now = now.strftime("%Y-%m-%d %H:%M:%S")
            sql = sql.replace("CREATE_TIME", now)   
            sql = sql.replace("AUTHOR_ID", str(user_id))
            db = get_db_instance()
            execute_sql(db, sql)
            return redirect("/")
        else:
            print(r_form.errors)
            return redirect(url_for("qa.public_question"))


@qa.route("/search")
@login_required
def search():
    # /search?q=flask
    # /search/<q>
    # post request.form
    #search for title
    q = request.args.get('q')
    sql = "select * from question where title like '%" + q + "%'"
    result = execut_select_sql(get_db_instance(), sql)
    return render_template("index.html", questions = result)

@qa.route("/qa/detail/<qa_id>")
def qa_detail(qa_id):
    sql = 'select * from question q left join users u on q.author_id = u.id left join answer a on q.id = a.question_id  where q.id="'+qa_id+'" order by a.id desc'
    db = get_db_instance()
    result = execut_select_sql(db, sql)
    if len(result) == 0:
        raise Exception("something wrong with database, the {} question doesn't exist!".format(qa_id))
    question = result[0]
    question['author'] = {'username':question['name']}
    answers = list()
    for item in result:
        answer = dict()
        answer['create_time'] = item['create_time']
        answer['content'] = item['a.content']
        answer['author'] ={'username':item['name']}
        answers.append(answer)
    question['answers'] = answers
    return render_template("detail.html", question = question)

#@qa.route("/answer/public", methods=['POST'])
@qa.post("/answer/public")
@login_required
def public_answer():
    r_form = AnswerForm(request.form)
    if r_form.validate():
        content = r_form.content.data
        question_id = r_form.question_id.data
        author_id = get_user_id()
        sql = "insert into answer (content, question_id, author_id) VALUES ('CONTENT', 'QUESTION_ID','AUTHOR_ID' )"
        sql = sql.replace("CONTENT", content)
        sql = sql.replace("QUESTION_ID", str(question_id))
        sql = sql.replace("AUTHOR_ID", str(author_id))
        execute_sql(get_db_instance(), sql)
        return redirect(url_for("qa.qa_detail", qa_id = question_id)) 
    else:
        print(r_form.errors)
        return redirect(url_for("qa.qa_detail", qa_id = request.form.get("question_id")))    
    