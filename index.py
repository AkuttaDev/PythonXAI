from flask import Flask, jsonify,request

app =Flask(__name__)

@app.route("/")
def home():
  return jsonify({"message":"My First API is live and cool!!",
                  "status":200,
                  "data":[],
                  "errors":[]
                  })
  
# @app.route("/greet/<name>")
# def greet(name):
#   return jsonify({"msg": f"Hello, {name}",})

# @app.route("/add/<int:num1>/<int:num2>")
# def add(num1, num2):
#   return jsonify({f"result of {num1} + {num2}": num1 + num2})

@app.route("/add", methods=["POST"])
def add():
  data = request.get_json()
  num1 = data["num1"]
  num2 = data["num2"]
  num3 = data["num3"]
  return jsonify({f"Sum of {num1}, {num2} and {num3}": num1 + num2 + num3})

@app.route("/multiply", methods=["POST"])
def multiply():
  data = request.get_json()
  a = data["First number"]
  b = data["Second number"]
  c = data["Third number"]
  d = data["Fourth number"]
  return jsonify({f"Multiplication of {a}, {b}, {c} and {d}": a * b * c * d})

@app.route("/oddoreven", methods=["POST"])
def oddoreven():
  data = request.get_json()
  num = data["Ran_number"]
  if num%2 == 0:
    return jsonify({f"{num} is": "even"})
  else:
    return jsonify({f"{num} is": "odd"})
  
@app.route("/length", methods=["POST"])
def length():
  req = request.get_json()
  word = req["Word"]
  return jsonify({f"Length of the word \'{word}\' is": f"{len(word)}"})

app.run()