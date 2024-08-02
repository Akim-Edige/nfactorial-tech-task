from Logger import Logger
log = Logger()


# TEST CASES FOR DIRECT TEST --------->

# print(log.shouldPrintMessage(1, "foo"))
# print(log.shouldPrintMessage(2, "bar"))

# print(log.shouldPrintMessage(3, "foo"))
# print(log.shouldPrintMessage(8, "bar"))

# print(log.shouldPrintMessage(10, "foo"))
# print(log.shouldPrintMessage(11, "foo"))


# print(log.loggerSize())
# print(log.clean(11))
# print(log.clean(12))


# ------------------------------------------
# WEB INTERFACE

from flask import Flask, render_template, request
app = Flask(__name__)


result = ''

@app.route('/')
def home():
    return render_template("index.html", pas='', name='')


@app.route("/main", methods=["POST"])
def receive_data():
    global result
    timestamp = request.form["timestamp"]
    message = request.form["message"]
    result = log.shouldPrintMessage(timestamp, message)
    time = log.currentTime
    size = log.loggerSize()
    return render_template("index.html", res = result, time = time, size = size)

@app.route("/login", methods=["POST"])
def clean_data():
    timestamp = request.form["clean"]
    clean = log.clean(timestamp)

    if(clean):
        clean = "True"
    else:
        clean = f"False there is message - {log.findKeyByValue(timestamp)}"

    time = log.currentTime
    size = log.loggerSize()

    return render_template("index.html", res = result, time = time, size = size, clean=clean)


# START HERE ------>>>
if __name__ == "__main__":
    app.run(debug=True)