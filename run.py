from flask import Flask, render_template, jsonify, request
import requests

from server import ldg

app = Flask(__name__, static_folder="./dist/static", template_folder="./dist")


@app.route("/api/balance")
def get_balance():
    account = request.args.get('account', '')
    s = ldg.ledger_balance(account)
    response = {"message": s}
    return jsonify(response)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    if app.debug:
        # Forward request to NPM development server.
        return requests.get("http://localhost:8080/{}".format(path)).text
    return render_template("index.html")
