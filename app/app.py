from flask import Flask, render_template

app = Flask(__name__)

 
@app.route('/')
def index():
    index={
        'titulo':'Kodland',
    }
    return render_template('index.html', index=index)

@app.route('/valores')
def darvalores():
    index={
        'titulo':'Kodland',
    }
    return render_template('valores.html', index=index)

@app.route('/plan')
def darplan():
    index={
        'titulo':'Kodland',
    }
    return render_template('plan.html', index=index)

if __name__ == '__main__':
    app.run(debug=True, port=5000)