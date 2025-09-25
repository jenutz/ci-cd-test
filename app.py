from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        user_id = int(request.args.get('id', 2))
    except ValueError:
        user_id = 1
    return f'<h1>Hello, user #{user_id}!</h1>'

if __name__ == '__main__':
    app.run(debug=True) # Уязвимость! Никогда не используйте debug=True в продакшене.
