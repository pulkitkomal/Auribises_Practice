from flask import Flask, request

app = Flask(__name__)

@app.route("/post_field", methods=["GET", "POST"])
def need_input():
    for key, value in request.form.items():
        print("key: {0}, value: {1}".format(key, value))

@app.route("/form", methods=["GET"])
def get_form():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)