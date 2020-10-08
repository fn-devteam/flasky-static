from flask import Flask, render_template
app = Flask(__name__)

@app.route('/html')
def static_page():
    return render_template("main_page.html")

@app.route('/sergio')
def sergio():
    return "Hello World!"

if __name__ == '__main__':
    app.run()