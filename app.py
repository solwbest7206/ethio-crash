from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Wallet system-ii gabaabaa (User balance)
user_wallets = {"user1": 1000} 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play_game():
    bet_amount = request.json.get('amount')
    # Multiplier inni itti crash godhu (0.01 - 10.0)
    crash_point = round(random.uniform(1.0, 10.0), 2)
    return jsonify({"crash_point": crash_point})

if __name__ == '__main__':
    app.run()
