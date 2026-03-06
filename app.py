from flask import Flask, render_template, request, redirect

app = Flask(__name__)

players = [
    {"id":1, "name":"Virat Kohli", "age":35, "innings":237, "runs":7263, "bid":20000000, "company":"None"},
    {"id":2, "name":"Rohit Sharma", "age":36, "innings":243, "runs":6211, "bid":18000000, "company":"None"},
    {"id":3, "name":"MS Dhoni", "age":42, "innings":250, "runs":5082, "bid":15000000, "company":"None"},
    {"id":4, "name":"Jasprit Bumrah", "age":30, "innings":120, "runs":100, "bid":12000000, "company":"None"},
    {"id":5, "name":"KL Rahul", "age":32, "innings":118, "runs":4163, "bid":14000000, "company":"None"},
    {"id":6, "name":"Hardik Pandya", "age":31, "innings":123, "runs":2309, "bid":13000000, "company":"None"},
]

@app.route("/")
def index():
    return render_template("index.html", players=players)


@app.route("/bid/<int:id>", methods=["POST"])
def bid(id):

    company = request.form["company"]
    new_bid = int(request.form["bid"])

    for player in players:
        if player["id"] == id:

            if new_bid >= player["bid"]:   # bid cannot be less
                player["bid"] = new_bid
                player["company"] = company

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)