from flask import Flask, render_template
app = Flask(__name__)

"""
Idea for this logic is taken from https://realpython.com/primer-on-jinja-templating/
"""

@app.route("/")
def template_test():
    return render_template('template.html',  my_list=[0,1,2])


if __name__ == '__main__':
    app.run(debug=True)
