from flask import Flask

app = Flask(__name__)

@app.route("/")
def say_hello():
  return "hello world!"

app.run(debug=True)
