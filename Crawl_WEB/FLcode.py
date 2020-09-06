# API: get, post, put, delete

from flask import Flask, redirect, render_template, request
import psycopg2

app = Flask(__name__)
@app.route('/')

def index():
    return 'hello'

def test():
    return 'nam'

@app.route('/say-hi/<string:name>')
def say_hi_everyone(name):
    return 'xin chào {}'.format(name)

@app.route('/add/<int:x>/<int:y>')
def sum_total(x, y):
    print(x+y)
    total = x + y
    return str(total)

@app.route('/redirect')
def test_redirect():
    return redirect('https://www.facebook.com/mixi04/')

@app.route('/web', methods = {'GET','POST'})
def homepage():
    if request.method == 'GET':
        return render_template('D:\Xactor_FACE_Recognition\Crawl_WEB\consula\index.html')
    elif request.method == "POST":
        form  = request.form
        answer1 = form["question1"]
        answer2 = form["question2"]
        print(answer1, answer2)


        user_agent = request.user_agent
        print(user_agent.platform)
        print(user_agent.version)
        print(user_agent.browser)
        print(user_agent.language)
        print(request.remote_addr)
        
        src_string = 'postgresql://{}:{}@localhost:5432/{}'.format('postgres','123','postgres')
        conn = psycopg2.connect(src_string)

        sql = '''
            insert into answers (answer1, answer2, platform, browser) values ('{}', '{}', '{}', '{}');
            '''.format(answer1, answer2, user_agent.platform, user_agent.browser)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        conn.close()

    return render_template('D:\Xactor_FACE_Recognition\Crawl_WEB\consula\index.html')

if __name__ == '__main__':
    app.run()

