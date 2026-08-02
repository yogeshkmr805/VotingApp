from flask import Flask
app = Flask(__name__)

votecounts = {}

# Adding a vote for the specified candidate
@app.route('/vote/<candidate>', methods=['POST'])
def vote(candidate):
    if candidate not in votecounts:
        votecounts[candidate] = 0
    votecounts[candidate] += 1
    return f"Vote recorded for {candidate}!"

# Return the current vote counts for all candidates
@app.route('/results', methods=['GET'])
def results():
    return votecounts

# Reset the vote counts for all candidates
@app.route('/reset', methods=['POST'])
def reset():
    votecounts.clear()
    return "Vote counts have been reset!"

if __name__ == '__main__':
    app.run(debug=True)