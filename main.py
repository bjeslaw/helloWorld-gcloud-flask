from flask import Flask, request

app = Flask(__name__)
app.secret_key = "secret_key_1755"

@app.route("/")
def hello():
    name = request.args.get('name','World')
    return f'Hello {name}!'