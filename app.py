from flask import Flask, render_template
app = Flask(__name__) #creates an app instance

@app.route("/") #uses home url
def hello():
    return render_template("index.html")

@app.route("/<name>")
def hello_name(name):
    return "Hello " + name

if __name__ == "__main__":
    app.run(debug = True) #runs in debug mode so we can make changes without restarting server
    