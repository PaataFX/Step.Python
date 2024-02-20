from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/starting")
def starting():
    return render_template("starting.html")



@app.route("/a1")
def a1():
    return render_template("a1.html")

@app.route("/a2")
def a2():
    return render_template("a2.html")

@app.route("/a3")
def a3():
    return render_template("a3.html")



@app.route("/a1_1")
def a1_1():
    return render_template("a1_1.html")

@app.route("/a1_2")
def a1_2():
    return render_template("a1_2.html")

@app.route("/a1_3")
def a1_3():
    return render_template("a1_3.html")



@app.route("/a1_1_1")
def a1_1_1():
    return render_template("a1_1_1.html")

@app.route("/a1_1_2")
def a1_1_2():
    return render_template("a1_1_2.html")

@app.route("/a1_1_3")
def a1_1_3():
    return render_template("a1_1_3.html")



@app.route("/a1_1_1_1")
def a1_1_1_1():
    return render_template("a1_1_1_1.html")

@app.route("/a1_1_1_2")
def a1_1_1_2():
    return render_template("a1_1_1_2.html")

@app.route("/a1_1_1_3")
def a1_1_1_3():
    return render_template("a1_1_1_3.html")



@app.route("/a1_1_1_1_1")
def a1_1_1_1_1():
    return render_template("a1_1_1_1_1.html")

@app.route("/a1_1_1_1_2")
def a1_1_1_1_2():
    return render_template("a1_1_1_1_2.html")

@app.route("/a1_1_1_1_3")
def a1_1_1_1_3():
    return render_template("a1_1_1_1_3.html")



@app.route("/a1_1_1_1_1_1")
def a1_1_1_1_1_1():
    return render_template("a1_1_1_1_1_1.html")

@app.route("/a1_1_1_1_1_2")
def a1_1_1_1_1_2():
    return render_template("a1_1_1_1_1_2.html")

@app.route("/a1_1_1_1_1_3")
def a1_1_1_1_1_3():
    return render_template("a1_1_1_1_1_3.html")

@app.route("/character")
def character():
    # Assuming ability_scores is defined somewhere in your application
    ability_scores = [10, 12, 14, 8, 13, 15]  # Example values

    # Pass ability_scores to the template
    return render_template("character.html", ability_scores=ability_scores)

@app.route("/generate", methods=["POST"])
def generate():
    # Get form data
    race = request.form.get("race")
    char_class = request.form.get("class")
    ability_scores = {
        "strength": int(request.form.get("strength", 10)),  # Default to 10 if value is not provided
        "dexterity": int(request.form.get("dexterity", 10)),
        "constitution": int(request.form.get("constitution", 10)),
        "intelligence": int(request.form.get("intelligence", 10)),
        "wisdom": int(request.form.get("wisdom", 10)),
        "charisma": int(request.form.get("charisma", 10))
    }

    # Pass form data to the new HTML page
    return render_template("character_page.html", race=race, char_class=char_class, ability_scores=ability_scores)

@app.route("/character_page")
def character_page():
    # Receive form data passed from the /generate route
    race = request.args.get("race")
    char_class = request.args.get("class")
    ability_scores = {
        "strength": int(request.args.get("strength", 10)),  # Default to 10 if value is not provided
        "dexterity": int(request.args.get("dexterity", 10)),
        "constitution": int(request.args.get("constitution", 10)),
        "intelligence": int(request.args.get("intelligence", 10)),
        "wisdom": int(request.args.get("wisdom", 10)),
        "charisma": int(request.args.get("charisma", 10))
    }

    # Pass form data to the character_page.html template
    return render_template("character_page.html", race=race, char_class=char_class, ability_scores=ability_scores)



if __name__ == "__main__":
    app.run(debug=True)