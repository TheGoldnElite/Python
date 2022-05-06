from flask import Flask, render_template

app=Flask(__name__)



@app.route('<int:x>/<int:y>')

def checkboard(x,y):
    for i in range(0,y):
        for j in range(0,x):











# def checkboard(x,y):
#     result=[]

#     for j in range(0,y):
#         temp=[]
#         for i in range(0,x):
#             temp.append((i+j) % 2)
#     result.append(temp)

#     return render_template("index.html", result=result)
            



if __name__ == "__main__":
    app.run(debug=True)