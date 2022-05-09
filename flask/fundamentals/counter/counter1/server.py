from flask import Flask,render_template, session#,request,redirect,session


app= Flask(__name__)
app.secret_key='this is counter file'

@app.route('/')
def counter():
    print("counter")
    return render_template("index.html")


# @app.route('/destroy_session')
# def session.clear()		# clears all keys
#     session.pop('key_name')


if __name__=="main":
    app.run(debug=True)