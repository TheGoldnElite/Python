from flask import Flask,render_template,redirect,session,request


app = Flask(__name__)
app.secret_key ="counter assignment"    


@app.route('/')        
def counter():
    if 'num' not in session:
        session['num'] = 0
    else:
        session['num'] += 1
    return render_template("index.html")

@app.route('/handle',method='post')
def handle():
    session['click'] = request.form['click']
    return redirect('/')



@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect ('/')

if __name__=="__main__":  
    app.run(debug=True)