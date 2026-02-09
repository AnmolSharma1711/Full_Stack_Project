from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# Use PostgreSQL on Vercel, SQLite locally
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///employee.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'supersecretkey')

db = SQLAlchemy(app)

# Create tables (for Vercel deployment)
with app.app_context():
    db.create_all()

class Employees(db.Model):
    __tablename__ = "employees"   # ✅ explicit table name

    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(500), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()

        if not name or not email:
            flash("Name and Email are required!", "error")
            return redirect("/")

        employee = Employees(name=name, email=email)
        db.session.add(employee)
        db.session.commit()

        return redirect("/")  # ✅ prevents duplicate insert on refresh

    allemployees = Employees.query.all()
    return render_template('index.html', allemployees=allemployees)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/delete/<int:sno>")
def delete(sno):
    employee = Employees.query.get(sno)
    if employee:
        db.session.delete(employee)
        db.session.commit()
    return redirect("/")


@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update(sno):
    employee = Employees.query.get(sno)

    if request.method == 'POST':
        employee.name = request.form['name']
        employee.email = request.form['email']
        db.session.commit()
        return redirect("/")

    return render_template("update.html", employee=employee)


if __name__ == '__main__': # ✅ creates table if not exists
    app.run(debug=True)
