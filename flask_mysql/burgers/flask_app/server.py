from flask_app import app

from burger import Burger
app = Flask(__name__)

from flask_app.controllers import burgers

if __name__=="__main__":
    app.run(debug=True)