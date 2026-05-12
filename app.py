from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f"Welcome {username}"
    return render_template('login.html')

@app.route('/reports', methods=['GET', 'POST'])
def reports():
    return render_template('reports.html')

@app.route('/recycling')
def recycling():
    return render_template('recycling.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
    