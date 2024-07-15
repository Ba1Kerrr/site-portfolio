from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')
@app.route('/')
def Home():
    return render_template('index.html')
@app.route('/About/')
def About():
    return render_template('About.html')
@app.route('/Contact/')
def Contact():
    return render_template('Contact.html')

if __name__ == "__main__":
    app.run(debug=True)