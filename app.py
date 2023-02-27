from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Create a dictionary to store game data
game_data = {}

# Define a function to generate a random ID
def generate_id():
    return str(random.randint(10000, 99999))

# Define a route for the home page
@app.route("/")
def home():
    return render_template("index.html")

# Define a route to create a new game
@app.route("/create", methods=["POST"])
def create():
    # Get the name from the form
    name = request.form["name"]

    # Generate a new game ID
    game_id = generate_id()

    # Create a new game dictionary and add it to the game data
    game = {"id": game_id, "players": [name], "current_player": name}
    game_data[game_id] = game

    # Redirect the user to the game page
    return redirect(url_for("game", game_id=game_id))

# Define a route for the game page
@app.route("/game/<game_id>")
def game(game_id):
    # Get the game from the game data
    game = game_data[game_id]

    # Get the current player and prompt from the game
    current_player = game["current_player"]
    prompt = game.get("prompt")
    image = game.get("image")
    winner = game.get("winner")
    error = request.args.get("error")

    # Render the game template with the game data
    return render_template("game.html", game_id=game_id, players=game["players"], current_player=current_player, prompt=prompt, image=image, winner=winner, error=error)

# Define a route to submit a prompt
@app.route("/submit", methods=["POST"])
def submit_prompt():
    # Get the prompt from the form
    prompt = request.form["prompt"]

    # Get the game ID from the form
    game_id = request.form["game_id"]

    # Get the game from the game data
    game = game_data[game_id]

    # Get the current player from the game
    player = game["current_player"]

    # Set the prompt for the game
    game["prompt"] = prompt

    # Redirect the user to the game page
    return redirect(url_for("game", game_id=game_id))


# Define a route to generate an image
@app.route("/generate", methods=["POST"])
def generate():
    # Get the game ID from the form
    game_id = request.form["game_id"]

    # Get the game from the game data
    game = game_data[game_id]

    # Get the current player from the game
    player = game["current_player"]

    # Check if the player is the current player
    if player != game["players"][0]:
        # If not, return an error message
        return redirect(url_for("game", game_id=game_id, error="You can't generate an image yet!"))

    # Generate an image URL
    image_url = "https://picsum.photos/500"

    # Set the image for the game
    game["image"] = image_url

    # Redirect the user to the game page
    return redirect(url_for("game", game_id=game_id))

# Define a route to submit a guess
@app.route("/guess", methods=["POST"])
def guess():
    # Get the guess from the form
    guess = request.form["guess"]

    # Get the game
@app.route('/submit', methods=['POST'])
def submit():
    player = session['player']
    prompt = request.form['prompt']
    game_id = session['game_id']
    
    # Update the game data
    game_data = games[game_id]
    game_data['prompts'][player] = prompt
    game_data['submitted'].add(player)
    
    # Check if all players have submitted their prompts
    if len(game_data['submitted']) == len(game_data['players']):
        # Generate the chain of messages/images
        chain = generate_chain(game_data['prompts'], game_data['players'], game_data['seed'])
        game_data['chain'] = chain
        
        # Reset the submitted set for the next round
        game_data['submitted'] = set()
        
        # Increment the round number
        game_data['round'] += 1
        
    return redirect(url_for('game'))

if __name__ == '__main__':
    app.run(debug=True)

# Define a route to submit a guess
@app.route("/guess", methods=["POST"])
def guess():
    # Get the guess from the form
    guess = request.form["guess"]

    # Get the game ID from the form
    game_id = request.form["game_id"]

    # Get the game from the game data
    game = game_data[game_id]

    # Get the current player from the game
    player = game["current_player"]

    # Get the previous player from the game
    prev_player_index = game["players"].index(player) - 1
    if prev_player_index < 0:
        prev_player_index = len(game["players"]) - 1
    prev_player = game["players"][prev_player_index]

    # Check if the guess is correct
    if guess.lower() == game["prompt"].lower():
        # If the guess is correct, set the winner and redirect to the game over page
        game["winner"] = player
        return redirect(url_for("game_over", game_id=game_id))

    else:
        # If the guess is incorrect, set the current player to the previous player
        game["current_player"] = prev_player

        # Redirect the user to the game page with an error message
        return redirect(url_for("game", game_id=game_id, error="Incorrect guess!"))
