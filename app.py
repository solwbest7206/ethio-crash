from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)
# Database salphaa balance user-aaf
user_wallets = {"user1": 0} 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play_win', methods=['POST'])
def play_win():
    data = request.json
    amount = int(data.get('amount')) # 5 ykn 25
    user_numbers = data.get('numbers')
    
    # Logic: Lakkofsa 1-15 keessaa 4 filachuun
    winning_numbers = random.sample(range(1, 16), 4)
    matches = len(set(user_numbers) & set(winning_numbers))
    
    # Haala kaffaltii (Payout)
    payout = 0
    if matches == 4:
        payout = 250 if amount == 25 else amount * 10
    
    return jsonify({"payout": payout, "winning": winning_numbers})

if __name__ == '__main__':
    app.run()
