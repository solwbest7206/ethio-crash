@app.route('/play_win', methods=['POST'])
def play_win():
    data = request.json
    amount = data.get('amount') # 5 ykn 25
    user_numbers = data.get('numbers')
    
    winning_numbers = random.sample(range(1, 16), 4)
    matches = len(set(user_numbers) & set(winning_numbers))
    
    # Logic-ii kaffaltii
    if matches == 4:
        if amount == 25:
            payout = 250 # 25 Birr yoo ta'e 250 ta'a
        elif amount == 5:
            payout = amount * 10 # Dhibbeentaa/Multiplier (fkn: 10x)
        else:
            payout = amount * 5
    else:
        payout = 0
        
    return jsonify({"payout": payout, "winning_numbers": winning_numbers})
