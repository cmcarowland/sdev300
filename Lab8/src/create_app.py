"""
Create and configure a Flask application instance.

This function initializes a new Flask application using the current module's 
name and returns the application instance. It can be used to set up routes, 
error handlers, and other configurations needed for the application.

Returns:
    Flask: A Flask application instance.

Example:
    app = create_app()
"""

import random
from datetime import datetime, timezone
from flask import Flask, render_template, request, redirect, make_response
import backend
from logger import LogItem, Log, LogTypes

app = Flask(__name__)
users = backend.Users()
log = Log()

def cookie() -> str:
    s = ""
    for _ in range(10):
        s = s + chr(random.randint(0x41, 0x67))

    return s

def is_authed(req) -> bool:
    if 'auth' in req.cookies:
        if req.cookies['auth'] in users.authenticated:
            return True

    return False

def get_auth_user_name(req) -> str:
    if 'auth' in req.cookies:
        if req.cookies['auth'] in users.authenticated:
            return users.authenticated[req.cookies['auth']].split(":")[0]

    return ""

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if is_authed(request):
            log.add_log(LogItem(LogTypes.WARN,\
                'Already Auth', datetime.now(timezone.utc), request.remote_addr))
            return redirect('/loggedin')
        if users.user_exist(request.form['uname']):
            if users.login(request.form['uname'], request.form['pword']):
                c = cookie()
                resp = make_response(redirect('/loggedin'))
                resp.set_cookie('auth', c)
                users.authenticated[c] = request.form['uname'] + ":" \
                    + str(datetime.now(timezone.utc))
                log.add_log(LogItem(LogTypes.INFO, 'Success', \
                                    datetime.now(timezone.utc), request.remote_addr))
                return resp

            log.add_log(LogItem(LogTypes.MED, 'Invalid Password', \
                datetime.now(timezone.utc), request.remote_addr))
        else:
            log.add_log(LogItem(LogTypes.MED, 'Invalid Username', \
                                datetime.now(timezone.utc), request.remote_addr))

        return render_template('login.html')

    if is_authed(request):
        return redirect('/loggedin')

    return render_template('login.html', invalid="hidden=true")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        if is_authed(request):
            return redirect('/loggedin')

        if users.user_exist(request.form['uname']):
            return render_template('signup.html', user="", \
                            pw="hidden=true", common="hidden=true")

        p = backend.Password(request.form['pword'])
        if p.is_common_password():
            return render_template('signup.html', user="hidden=true",\
                                pw="hidden=true", common="")

        if p.valid_password():
            users.add_user(request.form['uname'], request.form['pword'])
            return redirect('/login')

        return render_template('signup.html', user="hidden=true", \
                                pw="", common="hidden=true")

    return render_template('signup.html', user="hidden=true", \
            pw="hidden=true", common="hidden=true")

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        if not is_authed(request):
            return redirect('/login')
        
        uname = get_auth_user_name(request)

        if request.form['pword'] != request.form['pword2']:
            log.add_log(LogItem(LogTypes.HIGH, f'User {uname} tried to update their password, new PW did not match', \
                            datetime.now(timezone.utc), request.remote_addr))
            return render_template('update_password.html', old_pw="hidden=true", pw_match="", \
            pw="hidden=true", common="hidden=true", signup="", signup_success="hidden=true")

        update_status = users.update_password(uname, request.form['old_pw'], \
                                            request.form['pword'])
        rt = render_template('update_password.html', old_pw="hidden=true",\
                            pw_match="hidden=true", \
            pw="hidden=true", common="hidden=true", \
            signup="hidden=true", signup_success="")

        if  update_status == 2:
            log.add_log(LogItem(LogTypes.HIGH, f'User {uname} tried to update their password, gave incorrect Old PW', \
                            datetime.now(timezone.utc), request.remote_addr))
            rt = render_template('update_password.html', old_pw="", pw_match="hidden=true", \
            pw="hidden=true", common="hidden=true", signup="", signup_success="hidden=true")

        if update_status == 3:
            log.add_log(LogItem(LogTypes.WARN, f'User {uname} tried to update their password, PW is in common PW list', \
                            datetime.now(timezone.utc), request.remote_addr))
            rt = render_template('update_password.html',\
                                old_pw="hidden=true",pw_match="hidden=true", \
            pw="hidden=true", common="", signup="", signup_success="hidden=true")

        if update_status == 4:
            log.add_log(LogItem(LogTypes.LOW, f'User {uname} tried to update their password, gave incorrect new PW', \
                            datetime.now(timezone.utc), request.remote_addr))
            rt = render_template('update_password.html', old_pw="hidden=true",\
                                pw_match="hidden=true", pw="", common="hidden=true", \
                                signup="", signup_success="hidden=true")

        log.add_log(LogItem(LogTypes.INFO, f'User {uname} updated their password', \
                            datetime.now(timezone.utc), request.remote_addr))
        return rt

    if not is_authed(request):
        return redirect('/login')

    return render_template('update_password.html', old_pw="hidden=true", \
                        pw_match="hidden=true", pw="hidden=true", common="hidden=true", \
                        signup="", signup_success="hidden=true")

@app.route('/loggedin')
def loggedin():
    if not is_authed(request):
        log.add_log(LogItem(LogTypes.HIGH, 'Unauthorized Access Request', \
                            datetime.now(timezone.utc), request.remote_addr))
        return redirect('/login')

    dt = datetime.now()
    date_time = dt.strftime("%d/%m/%Y, %H:%M:%S")

    return render_template("loggedin.html", date_time=date_time)

@app.route('/sim_racing')
def sim():
    if not is_authed(request):
        log.add_log(LogItem(LogTypes.HIGH, 'Unauthorized Access Request', \
                            datetime.now(timezone.utc), request.remote_addr))
        return redirect('/login')

    return render_template("sim_racing.html")

@app.route('/games')
def games():
    if not is_authed(request):
        log.add_log(LogItem(LogTypes.HIGH, 'Unauthorized Access Request', \
                            datetime.now(timezone.utc), request.remote_addr))
        return redirect('/login')

    return render_template("games.html")

@app.errorhandler(404)
def error(e):
    log.add_log(LogItem(LogTypes.HIGH, '404 error', \
                            datetime.now(timezone.utc), request.remote_addr))

    return render_template("404.html", error=e), 404

@app.route('/logout')
def logout():
    if is_authed(request):
        del users.authenticated[request.cookies['auth']]

    return render_template('logout.html')
