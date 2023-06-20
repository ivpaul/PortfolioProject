from flask import Flask
from main import main_bp

app = Flask(__name__)
app.register_blueprint(main_bp, url_prefix="/")



if __name__ == '__main__':
    app.run(debug=True, port=8000)
