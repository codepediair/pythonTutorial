from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')#www.python.com
@app.route('/index')
def index():
    user = {'username': 'codepedia'}
    return render_template('index.html', user=user)

if __name__ == "__main__":
    app.run(debug=True) 