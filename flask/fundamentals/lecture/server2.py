from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/another_route')
def another_route():
    return "this is another route!"

@app.route('/test/<route_data')
def test_data(route_data):
    return f"the route data {route_data}"

@app.route('multiply/<int:x/<int:y>')
def multiply_two_numbers(x,y):
    return render_template("mulitply.html",x=x,y=y,result=x*y)
    

if __name__ == "__main__":
    app.run(degug=True)

