External Authentication Login System - Flask Project

Description:
This project demonstrates how to separate the login system from the main app using two different Flask applications. It simulates a simplified version of OAuth or Nafath where the login happens on a different domain/server.

How it works:
- User opens the main site (client)
- Clicks the login button
- Gets redirected to the auth server
- Logs in
- Gets redirected back to the main client app with their session or data

Project Folder Structure:
authentication-project/
  client/
    app.py
    templates/
      login.html
      welcome.html
  auth_server/
    auth.py
    templates/
      auth_login.html
  .gitignore
  README.md

Requirements:
- Python 3.x
- Flask

Install dependencies:
pip install flask

Run the project:
Open two terminal windows.

In the first terminal, run the auth server:
cd auth_server
python3 auth.py

In the second terminal, run the client app:
cd client
python3 app.py

Default Ports:
Auth Server → http://localhost:5001
Client App  → http://localhost:5000

Example Flow:
1. Open http://localhost:5000
2. Click Login
3. Redirected to http://localhost:5001/login
4. Enter username and password (hardcoded in auth.py)
5. If valid, redirect back to http://localhost:5000/welcome

Security Notes:
- The secret_key is hardcoded and for demo only.
- In production, you must use a secure secret key loaded from environment variables.
- User credentials are stored in a dictionary — replace with database and hashed passwords.

Future Improvements:
- Use JWT tokens instead of session
- Add database storage (e.g. SQLite or PostgreSQL)
- Use bcrypt to hash passwords
- Build a proper frontend with React/Vue for SSO simulation

Author:
Zaid Al‑Mutairi
Eastern Province - Saudi Arabia
IT Engineer / SDR Analyst
