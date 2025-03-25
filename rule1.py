from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def is_valid_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not (password[0].islower() and password[-1].islower()):
        return False, "Password must start and end with a lowercase letter."
    
    types_matched = 0
    if re.search(r'[a-z]', password): types_matched += 1
    if re.search(r'[A-Z]', password): types_matched += 1
    if re.search(r'\d', password): types_matched += 1
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>/?\\|`~]', password): types_matched += 1

    if types_matched < 3:
        return False, "Password must include at least three of the following: lowercase, uppercase, digit, special character."

    if re.search(r'[<>{}]', password):
        return False, "Password contains invalid characters."

    return True, "Password is valid!"

@app.route("/validate_rule1", methods=["POST"])
def validate_rule1():
    data = request.json
    password = data.get("password", "")
    valid, message = is_valid_password(password)
    return jsonify({"valid": valid, "message": message})

if __name__ == "__main__":
    app.run(debug=True)
