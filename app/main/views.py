from . import main

@main.route('/')
@main.route('/index')
def index():
    return 'Hello World!'
