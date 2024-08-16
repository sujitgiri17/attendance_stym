from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/login')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Check if username and password are correct (for demonstration purposes)
    if username == 'Umesh123' and password == 'Sujit@123':
        # Redirect to a page for the owner
        return redirect(url_for('show_attendance'))
    else:
        # Redirect back to the login page with an error message
        return redirect(url_for('index'))

@app.route("/attendance")
def show_attendance():
    return render_template("attendance.html")

if __name__ == '__main__':
    app.run(debug=True)



