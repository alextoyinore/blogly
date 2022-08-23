from crypt import methods
from distutils.log import debug
from flask import Flask, render_template, url_for, redirect, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('dashboard_auth'))


@app.route('/admin')
def dashboard():
    return render_template('/admin/index.html')


@app.route('/admin/login')
def login(error=None):
    return render_template('/admin/login.html', error=error)


@app.route('/admin/create-account', methods=['POST', 'GET'])
def create_account(error=None):
    if request.method == 'POST':
        if valid_create(request.form['username'], request.form['email'], request.form['password']):
            return log_in_to_admin(request.form['username'], request.form['password'])
        else:
            error = 'invalid username/password'
    return render_template('/admin/create-account.html', error=error)


def valid_create(username, email, password):
    if len(username) > 0 and len(email) > 0 and len(password) > 0:
        return True


def valid_login(username, password, email=''):
    if (len(username) > 0 and len(password) > 0) or (len(email) > 0 and len(password) > 0):
        return True


def log_in_to_admin(username, password):
    if valid_login(username, password):
        return redirect(url_for('dashboard'))


@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy-policy.html')


if __name__ == '__main__':
    debug = True
