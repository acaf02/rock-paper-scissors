from flask import Flask, request, jsonify, render_template
from main import play
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play_route():
    data = request.get_json()
    user_choice = data.get('choice')
    player_wins = data.get('player_wins', 0)
    computer_wins = data.get('computer_wins', 0)
    n = data.get('n', 5)

    result, user, computer = play(user_choice)

    if result == 1:
        player_wins += 1
    elif result == -1:
        computer_wins += 1

    wins_needed = math.ceil(n / 2)
    finished = False
    winner = None
    if player_wins >= wins_needed:
        finished = True
        winner = 'player'
    elif computer_wins >= wins_needed:
        finished = True
        winner = 'computer'

    return jsonify({
        'result': result,
        'user': user,
        'computer': computer,
        'player_wins': player_wins,
        'computer_wins': computer_wins,
        'finished': finished,
        'winner': winner
    })

if __name__ == '__main__':
    app.run(debug=True)
