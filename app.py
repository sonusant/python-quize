from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db=SQLAlchemy(app)

class Quiz(db.Model):
    test_id = db.Column(db.Integer , primary_key=True)
    uniq_name = db.Column(db.String(50), nullable=False )
    q_1 = db.Column(db.Integer)
    q_2 = db.Column(db.Integer)
    q_3 = db.Column(db.Integer )
    q_4 = db.Column(db.Integer )
    q_5 = db.Column(db.Integer )
    q_6 = db.Column(db.Integer )
    q_7 = db.Column(db.Integer )
    q_8 = db.Column(db.Integer )
    q_9 = db.Column(db.Integer )
    q_10 = db.Column(db.Integer )
    result = db.Column(db.String(50) )




@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        name = request.form['name']

        print('name send in quiz')
        quiz= Quiz()
        quiz.uniq_name=name
        
        print('name receive in quiz')
        db.session.add(quiz)
        db.session.commit()
        # quiz = Quiz.query.filter_by(uniq_name=name).first()
        return redirect(f'/test/{name}')

    # quiz = Quiz.query.filter_by(uniq_name=name).first()
    return render_template ('index.html' )
# uniq_name=name, q_1=None, q_2=None, q_3=None, q_4=None, q_5=None, q_6=None, q_7=None, q_8=None, q_9=None, q_10=None, result=None

@app.route('/test/<string:name>' , methods=['GET', 'POST'])
def res(name):
    if request.method=='POST':
        name = request.form['name']
        quiz = Quiz.query.filter_by(uniq_name=name).first()
        return redirect(f'/q1/{name}')
        
    quiz = Quiz.query.filter_by(uniq_name=name).first()
    return render_template ('test.html', quiz=quiz)



@app.route('/q1/<string:name>', methods=['GET', 'POST'])
def q1(name):

    if request.method=='POST':
        ans = request.form['ans']
        if int(ans) == 2:
            quiz = Quiz.query.filter_by(uniq_name=name).first()
            quiz.q_1 = 1
            db.session.add(quiz)
            db.session.commit()
            return redirect(f'/q2/{name}')

        else:
            quiz = Quiz.query.filter_by(uniq_name=name).first()
            quiz.q_1 = 0
            db.session.add(quiz)
            db.session.commit()
            return redirect(f'/q2/{name}')

    quiz = Quiz.query.filter_by(uniq_name=name).first()
    return render_template ('q1.html', quiz=quiz )

@app.route('/q2/<string:name>', methods=['GET', 'POST'])
def q2(name):

    if request.method=='POST':
        ans = request.form['ans']
        quiz = Quiz.query.filter_by(uniq_name=name).first()
        if int(ans) == 1:
            quiz = Quiz.query.filter_by(uniq_name=name).first()
            quiz.q_2 = int(1)
            db.session.add(quiz)
            db.session.commit()
            return redirect(f'/q3/{name}')
        else:
            quiz = Quiz.query.filter_by(uniq_name=name).first()
            quiz.q_2 = int(0)
            db.session.add(quiz)
            db.session.commit()
            return redirect(f'/q3/{name}')

    quiz = Quiz.query.filter_by(uniq_name=name).first()
    return render_template ('q2.html', quiz=quiz )

@app.route('/q3/<string:name>', methods=['GET', 'POST'])
def q3(name):

    if request.method=='POST':
        ans = request.form['ans']
        quiz = Quiz.query.filter_by(uniq_name=name).first()
        if int(ans) == 4:
            quiz = Quiz.query.filter_by(uniq_name=name).first()
            quiz.q_3 = int(1)
            db.session.add(quiz)
            db.session.commit()
            return redirect(f'/q4/{name}')
        else:
            quiz = Quiz.query.filter_by(uniq_name=name).first()
            quiz.q_3 = int(0)
            db.session.add(quiz)
            db.session.commit()
            return redirect(f'/q4/{name}')

    quiz = Quiz.query.filter_by(uniq_name=name).first()

    return render_template ('q3.html' , quiz=quiz )


@app.route('/q4/<string:name>', methods=['GET', 'POST'])
def q4(name):
    if request.method=='POST':
        ans = request.form['ans']
        quiz = Quiz.query.filter_by(uniq_name=name).first()
        if int(ans) == 3:
            quiz = Quiz.query.filter_by(uniq_name=name).first()
            quiz.q_4 = int(1)
            db.session.add(quiz)
            db.session.commit()
            return redirect(f'/q5/{name}')
        else:
            quiz = Quiz.query.filter_by(uniq_name=name).first()
            quiz.q_4 = int(0)
            db.session.add(quiz)
            db.session.commit()
            return redirect(f'/q5/{name}')


    quiz = Quiz.query.filter_by(uniq_name=name).first()
    return render_template ('q4.html', quiz=quiz )

@app.route('/q5/<string:name>', methods=['GET', 'POST'])
def q5(name):
    if request.method=='POST':
        ans = request.form['ans']
        quiz = Quiz.query.filter_by(uniq_name=name).first()
        if int(ans) == 1:
            quiz = Quiz.query.filter_by(uniq_name=name).first()
            quiz.q_5 = int(1)
            db.session.add(quiz)
            db.session.commit()
            return redirect(f'/q6/{name}')
        else:
            quiz = Quiz.query.filter_by(uniq_name=name).first()
            quiz.q_5 = int(0)
            db.session.add(quiz)
            db.session.commit()
            return redirect(f'/q6/{name}')


    quiz = Quiz.query.filter_by(uniq_name=name).first()
    return render_template ('q5.html',quiz=quiz )

@app.route('/q6/<string:name>', methods=['GET', 'POST'])
def q6(name):
    if request.method=='POST':
        ans = request.form['ans']
        quiz = Quiz.query.filter_by(uniq_name=name).first()
        if int(ans) == 4:
            quiz = Quiz.query.filter_by(uniq_name=name).first()
            quiz.q_6 = int(1)
            db.session.add(quiz)
            db.session.commit()
            return redirect(f'/q7/{name}')
        else:
            quiz = Quiz.query.filter_by(uniq_name=name).first()
            quiz.q_6 = int(0)
            db.session.add(quiz)
            db.session.commit()
            return redirect(f'/q7/{name}')

    quiz = Quiz.query.filter_by(uniq_name=name).first()
    return render_template ('q6.html',quiz=quiz )

@app.route('/q7/<string:name>', methods=['GET', 'POST'])
def q7(name):
    if request.method=='POST':
        ans = request.form['ans']
        quiz = Quiz.query.filter_by(uniq_name=name).first()
        if int(ans) == 2:
            quiz = Quiz.query.filter_by(uniq_name=name).first()
            quiz.q_7 = int(1)
            db.session.add(quiz)
            db.session.commit()
            return redirect(f'/q8/{name}')
        else:
            quiz = Quiz.query.filter_by(uniq_name=name).first()
            quiz.q_7 = int(0)
            db.session.add(quiz)
            db.session.commit()
            return redirect(f'/q8/{name}')

    quiz = Quiz.query.filter_by(uniq_name=name).first()
    return render_template ('q7.html',quiz=quiz )

@app.route('/q8/<string:name>', methods=['GET', 'POST'])
def q8(name):
    if request.method=='POST':
        ans = request.form['ans']
        quiz = Quiz.query.filter_by(uniq_name=name).first()
        if int(ans) == 2:
            quiz = Quiz.query.filter_by(uniq_name=name).first()
            quiz.q_8 = int(1)
            db.session.add(quiz)
            db.session.commit()
            return redirect(f'/q9/{name}')
        else:
            quiz = Quiz.query.filter_by(uniq_name=name).first()
            quiz.q_8 = int(0)
            db.session.add(quiz)
            db.session.commit()
            return redirect(f'/q9/{name}')

    quiz = Quiz.query.filter_by(uniq_name=name).first()
    return render_template ('q8.html',quiz=quiz )

@app.route('/q9/<string:name>', methods=['GET', 'POST'])
def q9(name):
    if request.method=='POST':
        ans = request.form['ans']
        quiz = Quiz.query.filter_by(uniq_name=name).first()
        if int(ans) == 4:
            quiz = Quiz.query.filter_by(uniq_name=name).first()
            quiz.q_9 = int(1)
            db.session.add(quiz)
            db.session.commit()
            return redirect(f'/q10/{name}')
        else:
            quiz = Quiz.query.filter_by(uniq_name=name).first()
            quiz.q_9 = int(0)
            db.session.add(quiz)
            db.session.commit()
            return redirect(f'/q10/{name}')

    quiz = Quiz.query.filter_by(uniq_name=name).first()
    return render_template ('q9.html', quiz=quiz )

@app.route('/q10/<string:name>', methods=['GET', 'POST'])
def q10(name):
    if request.method=='POST':
        ans = request.form['ans']
        quiz = Quiz.query.filter_by(uniq_name=name).first()
        if int(ans) == 3:
            quiz = Quiz.query.filter_by(uniq_name=name).first()
            quiz.q_10 = int(1)
            db.session.add(quiz)
            db.session.commit()
            return redirect(f'/ans/{name}')
        else:
            quiz = Quiz.query.filter_by(uniq_name=name).first()
            quiz.q_10 = int(0)
            db.session.add(quiz)
            db.session.commit()
            return redirect(f'/ans/{name}')

    quiz = Quiz.query.filter_by(uniq_name=name).first()
    return render_template ('q10.html',quiz=quiz )

@app.route('/ans/<string:name>', methods=['GET', 'POST'])
def ans(name):
    quiz = Quiz.query.filter_by(uniq_name=name).first()
    result=(quiz.q_1)+(quiz.q_2)+(quiz.q_3)+(quiz.q_4)+(quiz.q_5)+(quiz.q_6)+(quiz.q_7)+(quiz.q_8)+(quiz.q_9)+(quiz.q_10)
    print(result)
    quiz.result=result
    db.session.add(quiz)
    db.session.commit()
    return render_template ('ans.html', quiz=quiz, result=result )

if __name__ == '__main__':
    app.run(debug=True)