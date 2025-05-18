# Importerer nødvendige Flask-moduler og utvidelser
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv

# Laster inn miljøvariabler fra .env-fil
load_dotenv()

# Initialiserer Flask-applikasjonen
app = Flask(__name__)

# Konfigurerer applikasjonen med hemmelig nøkkel og database-tilkobling
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'din-hemmelige-nøkkel-her')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mysql://bruker:passord@localhost/innlogging_db')

# Initialiserer SQLAlchemy og LoginManager
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Angir hvilken side brukeren skal omdirigeres til ved innlogging

# Definerer brukermodellen med SQLAlchemy
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        """Hasher og lagrer passordet"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifiserer passordet mot den lagrede hashen"""
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    """Laster inn bruker basert på bruker-ID"""
    return User.query.get(int(user_id))

@app.route('/')
def home():
    """Hjemmeside - viser velkomstmelding og innloggingsstatus"""
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Håndterer innlogging av brukere"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        # Verifiserer brukernavn og passord
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('home'))
        flash('Ugyldig brukernavn eller passord')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Håndterer registrering av nye brukere"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Sjekker om brukernavnet allerede er i bruk
        if User.query.filter_by(username=username).first():
            flash('Brukernavnet er allerede i bruk')
            return redirect(url_for('register'))
        
        # Oppretter ny bruker
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registrering vellykket! Du kan nå logge inn.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    """Logger ut brukeren"""
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Oppretter databasetabeller hvis de ikke eksisterer
    with app.app_context():
        db.create_all()
    app.run(debug=True) 