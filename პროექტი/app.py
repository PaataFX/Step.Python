from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

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

@app.route("/character", methods=['GET', 'POST'])
def character():
    if request.method == 'POST':
        # Fetching data from form
        race = request.form['race']
        player_class = request.form['class']
        strength = int(request.form['strength'])
        dexterity = int(request.form['dexterity'])
        constitution = int(request.form['constitution'])
        intelligence = int(request.form['intelligence'])
        wisdom = int(request.form['wisdom'])
        charisma = int(request.form['charisma'])
        time = request.form['time']
        username = request.form['username']
        password = request.form['password']

        # Save character data to a JSON file
        character_data = {
            'race': race,
            'class': player_class,
            'strength': strength,
            'dexterity': dexterity,
            'constitution': constitution,
            'intelligence': intelligence,
            'wisdom': wisdom,
            'charisma': charisma,
            'time': time,
            'username': username,
            'password': password
        }
        try:
            with open('characters.json', 'a') as file:
                json.dump(character_data, file)
                file.write('\n')
        except Exception as e:
            print(f"Error writing to file: {e}")

        return redirect(url_for('character_page', race=race, player_class=player_class,
                                strength=strength, dexterity=dexterity, constitution=constitution,
                                intelligence=intelligence, wisdom=wisdom, charisma=charisma, time=time,
                                username=username, password=password))
    return render_template('character.html')


@app.route('/character_page')
def character_page():
    # Fetch URL parameters
    name = request.args.get('name', 'Unknown')
    race = request.args.get('race')
    player_class = request.args.get('class')
    strength = request.args.get('strength')
    dexterity = request.args.get('dexterity')
    constitution = request.args.get('constitution')
    intelligence = request.args.get('intelligence')
    wisdom = request.args.get('wisdom')
    charisma = request.args.get('charisma')
    time = request.args.get('time')

    return render_template('character_page.html', name=name, race=race, player_class=player_class,
                            strength=strength, dexterity=dexterity, constitution=constitution,
                            intelligence=intelligence, wisdom=wisdom, charisma=charisma, time=time)


if __name__ == "__main__":
    app.run(debug=True)
