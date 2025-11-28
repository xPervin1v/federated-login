from flask import Flask, request, redirect, session
import requests
import jwt

app = Flask(__name__)
app.secret_key = "client_secret_123"

AUTH_SERVER = "http://127.0.0.1:5000"
CLIENT_ID = "myclient"
REDIRECT_URI = "http://127.0.0.1:8000/callback"

@app.get("/")
def home():
    if "user" not in session:
        return '<a href="/login">Login with Federated Login</a>'
    return f"Welcome {session['user']}"

@app.get("/login")
def login():
    return redirect(f"{AUTH_SERVER}/login?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}")

@app.get("/callback")
def callback():
    code = request.args.get("code")
    resp = requests.post(f"{AUTH_SERVER}/token", data={"code": code})
    token = resp.json()["access_token"]

    # تحقق من التوقيع
    pub = requests.get(f"{AUTH_SERVER}/public").json()["public_key"]
    decoded = jwt.decode(token, pub, algorithms=["HS256"])

    session["user"] = decoded["sub"]
    return redirect("/")

app.run(host="0.0.0.0", port=8000)
