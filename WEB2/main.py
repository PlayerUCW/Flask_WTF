import flask
from scripts.forms import *
import json
import random


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'MARSISADUMP1337'


@app.route('/')
@app.route('/<title>')
@app.route('/index/<title>')
def tp(title='notitle'):
    return flask.render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return flask.render_template('training.html',
                                 title='Тренировки', p=prof.lower())


@app.route('/list_prof/<type>')
@app.route('/list_prof')
def plist(type='ul'):
    l = ['инженер-исследователь', 'пилот', 'строитель',
         'экзобиолог', 'врач', 'инженер по терраформированию',
         'климатолог', 'специалист по радиационной защите',
         'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения',
         'метеоролог', 'оператор марсохода', 'киберинженер',
         'штурман', 'пилот дронов']
    return flask.render_template('plist.html',
                                 title='Список профессий', t=type, l=l)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    form = {'title': 'Анкета',
            'surname': 'Пупкин',
            'name': 'Вася',
            'education': 'выше начального',
            'profession': 'оператор марсохода',
            'sex': 'паркетный',
            'motivation': 'Всегда мечтал засорить Марс!',
            'ready': True}
    return flask.render_template('auto_answer.html', **form)


@app.route('/login')
def emergency():
    form = EmAcForm()
    return flask.render_template('emergency.html',
                                 title='Аварийный доступ', form=form)


@app.route('/distribution')
def rooms():
    crew = ['Алексей Вопилин', 'Вася Пупкин', 'Пётр Сковородко', 'Сара Кацман',
            'Гарик Гончаров', 'Иван Череззаборногузадерищенко']
    return flask.render_template('rooms.html', crew=crew)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    color = ['ff', '66', ('66' if age < 21 else '00')]
    if sex == 'male':
        color = color[::-1]
    img = 'mini' if age < 21 else 'crewmate'
    return flask.render_template('table.html', title='Предпросмотр каюты', color='#' + ''.join(color), img=img)


@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    form = FileForm()
    if form.validate_on_submit():
        f = form.file.data
        f.save(f'static/{f.filename}')
        with open('static/gallery_items.list', 'a') as li:
            li.write(f.filename + '\n')
    with open('static/gallery_items.list', 'r') as li:
        pics = li.read().strip().split('\n')
    return flask.render_template('gallery.html', form=form, title='Красная планета', pics=pics)


@app.route('/member')
def member():
    with open('templates/crew.json', 'r', encoding='utf-8') as f:
        crew = json.load(f)
    return flask.render_template('member.html', title='Случайный астронавт', m=random.choice(crew))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')