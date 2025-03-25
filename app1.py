python3 app1.py



from flask import Flask, request, jsonify
from rule1 import validate_rule1
from rule2 import validate_rule2
from rule3 import validate_rule3

app = Flask(__name__)

@app.route("/validate_rule1", methods=["POST"])
def api_rule1():
    data = request.get_json()
    valid, message = validate_rule1(data.get("password", ""))
    return jsonify({"valid": valid, "message": message})

@app.route("/validate_rule2", methods=["POST"])
def api_rule2():
    data = request.get_json()
    valid, message = validate_rule2(data.get("password", ""))
    return jsonify({"valid": valid, "message": message})

@app.route("/validate_rule3", methods=["POST"])
def api_rule3():
    data = request.get_json()
    valid, message = validate_rule3(data.get("password", ""))
    return jsonify({"valid": valid, "message": message})

if __name__ == "__main__":
    app.run(debug=True)
