# Lockr
#### Video Demo:  <[URL HERE](https://www.youtube.com/watch?v=1wFkQxpwX3k)>
#### Description:
Lockr is a basic password manager where you can store all of your password anytime. It provides all the necessary functions that a passwords manager needs such as editing the passwords, searching for a password, deleting a password etc.

File Structure and Descriptions
1) app.py
This is the core of the Flask application. It defines all the routes and handles the main business logic of the app.
It manages:
User registration and login
Session tracking using Flask's session object
CRUD operations on password entries
Routing logic for pages like /, /error, /edit, and /delete

Design decision: I kept all routes in a single file for simplicity. If the application were to grow further, I would separate concerns using Flask Blueprints.

2) helpers.py
This file contains reusable helper functions to support the application, such as:
Encrypting and decrypting passwords before database storage
Login required before accessing any other pages

Design decision: This modular approach keeps app.py clean and allows easy updates or improvements to utility functions without touching core logic.

2) lockr.db
This is a local SQLite database used for storing user and password data. It contains tables like:
users: with id, username, hash
passwords: with id, user_id, service_name, service_username, and service_password

Design decision: SQLite is lightweight and requires no setup, making it ideal for a self-contained project like this. It can be swapped with PostgreSQL or MySQL for production.

2) templates/ (Jinja HTML Templates)
a) layout.html
This is the base template extended by all other pages. It contains the navigation bar, links to stylesheets and scripts, and a {% block main %} section for injecting page-specific content.

Design decision: This follows DRY principles—Don’t Repeat Yourself—by avoiding repeated code across HTML files.

b) index.html
The landing page after a successful login. It serves as the main page which renders all the existing entries stored, an form through which we can add more and more entries, a search feature which can search usernames and websites and filter out the data accordingly, an edit button which lets users edit their entries, delete entries with a trash icon etc.

Design decision: Keeping everything visible and accessible in one table improves usability. JavaScript enhances interactivity without extra page reloads.

c) login.html
A login form for existing users. It posts credentials to /login and provides feedback on authentication status.

d) register.html
Contains the registration form to create a new user account. Submits data to /register and handles basic input validation.

f) edit.html
Allows editing an existing password entry. It loads the selected row’s data into a form and submits updates back to the database.

Design decision: Having a separate edit page simplifies logic and ensures the form is clean and focused.

g) error.html
Displays user-friendly error messages, such as incorrect logins or duplicate usernames. Improves user experience by providing feedback instead of silent failure.

3) static/ (CSS, JavaScript, Images)
a) styles.css
Contains custom CSS that gives the app a sleek dark theme. It adjusts the background, form colors, and text contrast. Overrides Bootstrap defaults for consistent dark UI.

Design decision: I customized the look manually to give a unique, minimal, and hacker-style visual theme.

b) script.js
Holds client-side JavaScript for:
Toggling password visibility
Real-time filtering of entries based on input
Any future interactivity like animations or form validation

Design decision: Separating JS keeps the HTML cleaner and supports better debugging and maintenance.

c) icon.png
A small image/logo used in the navigation bar or as a favicon to brand the app as "Lockr".
