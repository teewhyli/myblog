from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'TY Li',
        'title': 'Blog Post 1',
        'content': 'Hello World!',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Jenny Hsiao',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2020'
    }
]

@app.route("/")
@app.route("/home")
def homepage():
    return render_template('home.html', posts=posts, title='Hey!')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)