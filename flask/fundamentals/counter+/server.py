from flask import Flask #render_template #session,request,redirect,


app= Flask(__name__)
# app.secret_key='this is counter file'

@app.route('/')
def hello():
    return 'hello'


# @app.route('/destroy_session')
# def session.clear()		# clears all keys
#     session.pop('key_name')


if __name__=="___main__":
    app.run(debug=True)