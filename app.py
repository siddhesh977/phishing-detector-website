from flask import Flask, render_template, request
import random
from datetime import datetime

app = Flask(__name__)

def perform_deep_analysis(content):
    # Simulated AI logic
    score = random.randint(10, 98)
    
    if score > 75:
        prediction = "Phishing Detected"
        flags = ["Suspicious URL Pattern", "Urgent Language", "Unknown Sender"]
    elif score > 40:
        prediction = "Suspicious Content"
        flags = ["Non-standard Domain", "Neutral Sentiment"]
    else:
        prediction = "Safe / Legitimate"
        flags = ["Secure Protocol Found", "No Known Threats"]
        
    return prediction, score, flags

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        content = request.form.get('url') or request.form.get('email_text')
        if content:
            prediction, score, flags = perform_deep_analysis(content)
            result = {
                "prediction": prediction,
                "score": score,
                "flags": flags,
                "target": content[:45] + "..." if len(content) > 45 else content,
                "time": datetime.now().strftime("%H:%M:%S")
            }
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)