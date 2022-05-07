from flask import Flask, render_template

app=Flask(__name__)

@app.route('/hello')
def hello():
    return "hello"

@app.route('/')
def checkerboard1():
    return render_template("index.html", x=8,y=8,color1="black",color2="red")

@app.route('/4')
def checkerboard2():
    return render_template("index.html",x=4,y=8,color1="black",color2="red")


@app.route('/<int:x>/<int:y>')
def checkerboard3(x,y):
    return render_template("index.html",x = x,y = y,color1 = "black",color2 = "red")




# @app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
# def checkerboard4(x,y,color1,color2):
#     return render_template("index.html,",x=x,y=y, color1=color1,color2=color2)

    
    


if __name__ == "__main__":
    app.run(debug=True)