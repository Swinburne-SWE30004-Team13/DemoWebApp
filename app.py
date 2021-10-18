from flask import Flask
import os
import socket

from flask.templating import render_template

app = Flask(__name__, template_folder="view")

@app.route("/")
def hello():
    html =  "<h3 id='heading'>Team 13</h3>" \
            "<b id='student1'>Student Name:</b> Jack Hyland - 101603196<br/>" \
            "<b id='student2'>Student Name:</b> Chuong Ho - 101921623<br/>" \
            "<p>Tutorial time: 12:30PM - 14:30PM </p>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

@app.route("/calc")
def calc():
    return render_template('calc.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 7998)
