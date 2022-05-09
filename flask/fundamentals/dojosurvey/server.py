from flask import Flask, render_template,request,redirect,session

app = Flask(__name__)
app.secret_key="DojoSurvey"


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/handle_results', methods= ['POST'])
def handle_results():
    
    session['your_name'] = request.form['your_name']
    session['Location'] = request.form['Location']
    session['Language'] = request.form['Language']
    session['Comments'] = request.form['comments']
    return redirect('/show_results')


@app.route('/show_results')
def results():
    return render_template('results.html')

if __name__=="__main__":
    app.run(debug=True)