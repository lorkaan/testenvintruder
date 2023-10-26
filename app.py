from flask import Flask, request

app = Flask(__name__)

allowed_params = ['valid', "apple"]

@app.route('/gtest', methods=["GET"])
def give_output():
    args = request.args
    pos_value = args.get("name")
    if pos_value in allowed_params:
        return "Success: {0}".format(pos_value)
    else:
        return ""

@app.route('/batteringram', methods=["GET"])
def battering_ram():
    args = request.args
    pos_value1 = args.get("name")
    pos_value2 = args.get("head")
    if pos_value1 == pos_value2 and pos_value1 in allowed_params:
        return "Success: {0}".format(pos_value1)
    else:
        return ""

@app.route("/pitchfork", methods=["GET"])
def pitchfork():
    args = request.args
    username = args.get("user")
    password = args.get("pw")
    if username == allowed_params[0] and password == allowed_params[1]:
        return "Success: User is {0} and Password is {1}".format(username, password)
    else:
        return ""

@app.route("/clusterbomb", methods=["POST"])
def clusterbomb():
    args = request.form
    username = args.get("user")
    password = args.get("pw")
    if username == allowed_params[0] and password == allowed_params[1]:
        return "Success: User is {0} and Password is {1}".format(username, password)
    else:
        return ""


if __name__ == '__main__':
    app.run()