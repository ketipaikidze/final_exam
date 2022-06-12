'''
შექმენით ფლასკის აპლიკაცია. აპლიკაცია გაუშვით 0.0.0.0 მისამართზე.
პორტი მიუთითეთ 8090. აპლიკაციას დაამატეთ ORM მოდული. მონაცემთა
ბაზად გამოიყენეთ Sqlite. შექმენით მოდელი Building. განუსაზღვრეთ
ველები: id, მისამართი და სართულების რაოდენობა. აპლიკაციას დაამატეთ
ორი გზა. ერთმა გზამ უნდა შექმნას ახალი ჩანაწერი მონაცემთა ბაზაში.
ხოლო მეორე გზამ უნდა მოგვცეს ბაზაში არსებული ჩანაწერის განახლების
უფლება. HTTP მეთოდები და გზების სახელწოდებები შეარჩიეთ თქვენით.
დაიცავით სტანდარტი შერჩევის დროს.
'''
from urllib import request

from flask import Flask, flash, render_template
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{basedir}/sqlite.db'
db = SQLAlchemy(app)

class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(80), unique=True, nullable=False)
    numbs_of_floor = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f'Building("{self.id}", "{self.address}", "{self.numbs_of_floor}")'


@app.route('/add_building', methods=['GET', 'POST'])
def add_building():
    if request.method == 'POST':
        if not request.form['id'] or not request.form['address'] or not request.form['numbs_of_floor']:
            flash('Please enter all the fields', 'error')
        else:
            building = Building(request.form['id'], request.form['address'],
                                request.form['numbs_of_floor'])

            db.session.add(building)
            db.session.commit()

    return render_template('add_building.html')








if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8090)