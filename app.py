from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from os import listdir
from uuid import uuid4
from json import dump, load

app = Flask(__name__)
Bootstrap(app)
data = dict(enumerate(listdir('./static')))

def save_data(data, file):
    with open(file, 'r', encoding='utf-8') as f:
        db = load(f)
    with open(file, 'w', encoding='utf-8') as w:
        db.append(data)
        dump(db, w)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/experiment', methods=['GET', 'POST'])
def experiment():
    if not request.form:
        return render_template('survey.html')
    else:
        if 'survey' in list(request.form.keys()):
            code = 0
            user = str(uuid4())
            form_data = {
                'id': user,
                'born': request.form['born'],
                'origin': request.form['origin'],
                'studies': request.form['studies']
            }
            save_data(form_data, 'users.json')
        else:
            form_data = {
                'user': request.form['user'],
                'audio': data[int(request.form['code'])],
                'judgement': request.form['judgement']
            }
            save_data(form_data, 'judgements.json')
            if int(request.form['code']) == max(data.keys()):
                return render_template('end.html')
            else:
                code = int(request.form['code']) + 1
                user = request.form['user']
        return render_template('experiment.html', user=user, code=code, audio=data[code])

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404