from flask import  Flask
from route import  route_dropdown

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(route_dropdown.main,url_prefix='/')
    app.run(debug=True)