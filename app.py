from flask import Flask, render_template, redirect, request, session, url_for

app = Flask(__name__)
app.secret_key = "secret_key_123"  # Jangan lupa tambahkan secret key

@app.route("/")
@app.route("/<page>")
def index(page="DataDiri"):
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    if page == "DataDiri":
        content_template = "data_diri.html"
    elif page == "DaftarNilai":
        content_template = "daftar_nilai.html"
    else:
        content_template = "data_diri.html"
    return render_template("index.html", page=page, content_template=content_template)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if email == "salshabilla@gmail.com" and password == "1482300084":
            session["logged_in"] = True
            return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("login"))

@app.route("/daftar_nilai")
def daftar_nilai():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("index.html", page="DaftarNilai", content_template="daftar_nilai.html")

if __name__ == "__main__":
    app.run(debug=True)
