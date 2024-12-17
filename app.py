from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = "secret_key"  # Tambahkan secret key untuk menggunakan session

@app.route("/")
def index():
    if not session.get("logged_in"):
        return redirect(url_for("login"))  # Jika belum login, redirect ke halaman login
    return render_template("index.html", content_template="data_diri.html")

@app.route("/daftar_nilai")
def daftar_nilai():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("index.html", content_template="daftar_nilai.html")

@app.route("/krs")
def krs():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("index.html", content_template="krs.html")

@app.route("/logout")
def logout():
    session.pop("logged_in", None)  # Hapus sesi login
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if email == "salshabilla@gmail.com" and password == "1482300084":
            session["logged_in"] = True
            return redirect(url_for("index"))
        else:
            error = "Email atau Password salah!"  # Pesan error jika login gagal
            return render_template("login.html", error=error)
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
