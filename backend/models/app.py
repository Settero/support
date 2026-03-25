from flask import Flask
from support.backend.models.config import Config
from support.backend.models.models import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/')
def home():
    return {"message": "API работает"}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)