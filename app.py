from flask import Flask, request, render_template_string
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
db = SQLAlchemy(app)

# @app.route('/')
# def hello():
#     return 'Hello, Flask!'

@app.route('/', methods=['GET', 'POST'])
def hello():
    name = request.form.get('name', 'World')
    html_form = """
        <html>
            <body>
                <form method="post">
                    <label for="name">Enter your name:</label>
                    <input type="text" id="name" name="name">
                    <input type="submit" value="Submit">
                </form>
                <h1>Hello, {}!</h1>
            </body>
        </html>
    """.format(name)
    return render_template_string(html_form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
#http://localhost:5000