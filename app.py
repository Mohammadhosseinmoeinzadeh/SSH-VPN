from flask import Flask, render_template, request, redirect, url_for, session
import subprocess
import crypt
import pexpect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'   

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)


with app.app_context():
    db.create_all()


users = []

@app.route('/')
def home():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('panel'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin': # user password
            session['logged_in'] = True  
            return redirect(url_for('panel'))
        else:
            return render_template('login.html', message='Invalid username or password.')
    return render_template('login.html')

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('logged_in', None) 
    return redirect(url_for('login'))

@app.route('/panel')
def panel():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    
    users = User.query.all()

    return render_template('panel.html', users=users)

@app.route('/create_user', methods=['POST'])
def create_user():
    username = request.form['username']
    password = request.form['password']
    expiration_date_str = request.form['expiration_date']
    expiration_date = datetime.strptime(expiration_date_str, '%Y-%m-%d')
    # رمزنگاری رمز عبور
    encrypted_password = crypt.crypt(password)
    subprocess.run(['useradd', '-p', encrypted_password, username])
    subprocess.run(['chage', '-E', expiration_date_str, username])
    new_user = User(username=username, password=encrypted_password,expiration_date=expiration_date)
    db.session.add(new_user)
    db.session.commit()



    return redirect(url_for('panel'))

@app.route('/delete_user', methods=['POST'])
def delete_user():
    username = request.form['username']

  
    pkill_cmd = f"sudo pkill -u {username}"
    pkill_process = pexpect.spawn(pkill_cmd)
    pkill_process.expect(pexpect.EOF)

   
    userdel_cmd = f"sudo userdel -r {username}"
    userdel_process = pexpect.spawn(userdel_cmd)
    userdel_process.expect(pexpect.EOF)

  
    user_to_delete = User.query.filter_by(username=username).first()
    if user_to_delete:
        db.session.delete(user_to_delete)
        db.session.commit()

    return redirect(url_for('panel'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
