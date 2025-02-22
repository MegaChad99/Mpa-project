from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/spy1')
def spy1():
    return render_template('spy1.html')

if __name__ == '__main__':
    app.run(debug=True)
