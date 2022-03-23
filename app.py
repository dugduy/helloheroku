from flask import Flask
app=Flask('app')
@app.route('/')
def home():
    return 'Hello World!'
app.run(debug=True, use_reloader=True)
