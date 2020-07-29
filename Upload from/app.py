from flask import Flask,render_template,request
import os

app = Flask(__name__)

wsgi_app  = app.wsgi_app

@app.route('/',methods = ["GET","POST"])
def hello():
    if request.method == "POST":
        file = request.files["file"]
        file.save(os.path.join("uploads",file.filename))
        return render_template("index.html",message="success")
    return render_template("index.html",message="Upload")

if __name__ == "__main__":
    app.run(debug=True)