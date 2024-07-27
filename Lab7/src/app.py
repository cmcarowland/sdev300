"""
Flask Web Application

This module sets up a simple Flask web application with routes for different pages. 

Routes:
- '/': Displays the index page with the current date and time.
- '/index': Alias for the index page.
- '/sim_racing': Displays the simulation racing page.
- '/games': Displays the games page.
- '/404': Handles 404 errors by displaying a custom '404.html' page.

Error Handling:
- 404 errors: Redirects to a custom '404.html' page when a requested URL is not found.

Dependencies:
- Flask: A web framework used to build the application.
- datetime: Used to fetch and format the current date and time.

The application uses the Flask framework to handle routing and rendering of HTML templates. 
Ensure that the HTML templates ('index.html', 'sim_racing.html', 'games.html', and '404.html') 
are present in the templates directory for proper functionality.
"""

import random
from datetime import datetime
from flask import Flask, render_template, request, redirect, make_response
import backend


def create_app() -> Flask:
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

    a = Flask(__name__)

    @a.route('/')
    def index():
        return redirect('/login')

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

    @a.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            if is_authed(request):
                return render_template('loggedin.html')

            if users.user_exist(request.form['uname']):
                if users.login(request.form['uname'], request.form['pword']):
                    c = cookie()
                    resp = make_response(render_template('loggedin.html'))
                    resp.set_cookie('auth', c)
                    users.authenticated[c] = datetime.now()
                    return resp

            return render_template('login.html')

        if is_authed(request):
            return redirect('/loggedin')

        return render_template('login.html', invalid="hidden=true")

    @a.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            if is_authed(request):
                return render_template('loggedin.html')

            if users.user_exist(request.form['uname']):
                return render_template('signup.html', user="", pw="hidden=true")

            p = backend.Password(request.form['pword'])
            if p.valid_password():
                users.add_user(request.form['uname'], request.form['pword'])
                return redirect('/login')

            return render_template('signup.html', user="hidden=true", pw="")

        if is_authed(request):
            return redirect('/loggedin')

        return render_template('signup.html', user="hidden=true", pw="hidden=true")

    @a.route('/loggedin')
    def loggedin():
        """
        Handle requests to the root URL ('/') and '/index'.
        
        Renders the 'index.html' template with the current date and time.
        
        Returns:
            str: Rendered HTML of 'index.html' with the current date and time.
        """
        if not is_authed(request):
            return redirect('/login')

        dt = datetime.now()
        date_time = dt.strftime("%d/%m/%Y, %H:%M:%S")

        return render_template("loggedin.html", date_time=date_time)

    @a.route('/sim_racing')
    def sim():
        """
        Handle requests to the '/sim_racing' URL.
        
        Renders the 'sim_racing.html' template.
        
        Returns:
            str: Rendered HTML of 'sim_racing.html'.
        """
        if not is_authed(request):
            return redirect('/login')

        return render_template("sim_racing.html")

    @a.route('/games')
    def games():
        """
        Handle requests to the '/games' URL.
        
        Renders the 'games.html' template.
        
        Returns:
            str: Rendered HTML of 'games.html'.
        """
        if not is_authed(request):
            return redirect('/login')

        return render_template("games.html")

    @a.errorhandler(404)
    def error(e):
        """
        Handle 404 errors (page not found).
        
        Renders the '404.html' template when a requested page is not found.
        
        Args:
            e (Exception): The exception raised for the 404 error.
        
        Returns:
            str: Rendered HTML of '404.html'.
        """

        return render_template("404.html", error=e), 404

    @a.route('/logout')
    def logout():
        if is_authed(request):
            del users.authenticated[request.cookies['auth']]

        return render_template('logout.html')

    return a

users = backend.Users()
app = create_app()
