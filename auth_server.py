from flask import Flask, request, redirect, jsonify
import jwt
import time
import secrets

app = Flask(__name__)

# \u0645\u0641\u0627\u062a\u064a\u062d \u0627\u0644\u062a\u0648\u0642\u064a\u0639
PRIVATE_KEY = "secret123"
PUBLIC_KEY = "secret123"

# \u0642\u0627\u0639\u062f\u0629 \u0628\u064a\u0627\u0646\u0627\u062a \u0645\u0624\u0642\u062a\u0629 \u0644\u0644\u0643\u0648\u062f\u0627\u062a
AUTH_CODES = {}

# \u0635\u0641\u062d\u0629 \u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644
@app.get("/login")
def login_page():
    client_id = request.args.get("client_id")
    redirect_uri = request.args.get("redirect_uri")
    return f"""
    <form action="/login" method="post">
        <input type="hidden" name="client_id" value="{client_id}">
        <input type="hidden" name="redirect_uri" value="{redirect_uri}">
        <input name="username" placeholder="Username">
        <input name="password" placeholder="Password" type="password">
        <button>Login</button>
    </form>
    """

# \u0645\u0639\u0627\u0644\u062c\u0629 \u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644
@app.post("/login")
def login_handler():
    username = request.form["username"]
    password = request.form["password"]
    client_id = request.form["client_id"]
    redirect_uri = request.form["redirect_uri"]

    if username == "zaid" and password == "1234":
        code = secrets.token_hex(16)
        AUTH_CODES[code] = username
        return redirect(f"{redirect_uri}?code={code}")
    else:
        return "Invalid login"

# endpoint /token
@app.post("/token")
def token_endpoint():
    code = request.form["code"]
    username = AUTH_CODES.get(code)

    if not username:
        return jsonify({"error": "invalid code"}), 400

    # \u0646\u0635\u0646\u0639 JWT
    token = jwt.encode({
        "sub": username,
        "iat": int(time.time()),
        "exp": int(time.time()) + 3600,
        "iss": "auth-server"
    }, PRIVATE_KEY, algorithm="HS256")

    return jsonify({
        "access_token": token,
        "token_type": "bearer"
    })

# public key endpoint
@app.get("/public")
def public_key():
    return jsonify({"public_key": PUBLIC_KEY})

app.run(host="0.0.0.0", port=5000)
