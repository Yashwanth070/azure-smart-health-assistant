
from flask import Flask, render_template, request
import openai

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    if request.method == 'POST':
        user_input = request.form['query']
        response = get_ai_response(user_input)
    return render_template('index.html', response=response)

def get_ai_response(prompt):
    openai.api_key = "your-openai-api-key"
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
