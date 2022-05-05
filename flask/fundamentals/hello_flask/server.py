from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/dojo')
def another_route():
    return "Dojo!"

@app.route('/say/<route_data>')
def test_data(route_data):
    return f"Hi! {route_data}"

@app.route('/repeat/<int:num>/<string:words>')
def sayingwords(num,words):
    output= ''

    for i in range(0,num):
        output += f'<p>{words}</p>'
    return output



#@app.route('/userprofile/<int:user_id>')
#@app.route('/userprofile/<string:user_name>')



if __name__ == "__main__":
    app.run(debug=True)
