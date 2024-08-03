"""
Flask Web Application

This module sets up a simple Flask web application with routes for different pages. 

Routes:
- '/': Displays the index page with the current date and time.
- '/index': Alias for the index page.
- '/sim_racing': Displays the simulation racing page.
- '/games': Displays the games page.
- '/404': Handles 404 errors by displaying a custom '404.html' page.
- '/update': Allows users to update their password

Error Handling:
- 404 errors: Redirects to a custom '404.html' page when a requested URL is not found.

Dependencies:
- Flask: A web framework used to build the application.
- datetime: Used to fetch and format the current date and time.

The application uses the Flask framework to handle routing and rendering of HTML templates. 
Ensure that the HTML templates ('index.html', 'sim_racing.html', 'games.html', and '404.html') 
are present in the templates directory for proper functionality.
"""

from create_app import app

if __name__ == "__main__":
    app.run()
