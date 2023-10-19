from flask import Flask, render_template, redirect, url_for, flash
import os
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Plant, user_plants
from forms import PlantSearchForm
from fetch_data import fetch_plants_by_query

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plantdaddy.db'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db.init_app(app)

@app.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('profile.html', user=user)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PlantSearchForm()
    plants = []
    if form.validate_on_submit():
        query = form.query.data
        plants = fetch_plants_by_query(query)
        if not plants:
            flash('No plants found for the given query.', 'danger')
    return render_template('index.html', form=form, plants=plants)

@app.route('/save_plant/<int:plant_id>', methods=['POST'])
def save_plant(plant_id):
    # Check if user is authenticated; for now, let's use a placeholder user_id
    user_id = 1  # Placeholder; replace this with the logged-in user's ID later

    # Check if plant is already saved by the user
    saved = db.session.query(user_plants).filter_by(user_id=user_id, plant_id=plant_id).first()
    if saved:
        flash('Plant already saved!', 'info')
        return redirect(url_for('index'))

    # If not, save the plant for the user
    new_saved_plant = user_plants.insert().values(user_id=user_id, plant_id=plant_id)
    db.session.execute(new_saved_plant)
    db.session.commit()

    flash('Plant saved successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
