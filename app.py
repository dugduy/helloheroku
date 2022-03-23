from flask import Flask
app=Flask('app')
@app.route('/')
def home():
    return 'Hello World!'
app.run('0.0.0.0',80)
