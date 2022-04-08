from app import app

@app.route('/')
@app.route('/index')
def index():
    print(app.instance_path)
    return app.instance_path