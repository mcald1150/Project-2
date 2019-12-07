# import necessary libraries
from sqlalchemy import func
import pandas as pd
import json

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/db.sqlite"

db = SQLAlchemy(app)


class Shooting(db.Model):
    __tablename__ = 'Shootings'

    INCIDENT_KEY = db.Column(db.Integer, primary_key=True)
    OCCUR_DATE = db.Column(db.String)
    OCCUR_TIME = db.Column(db.String)
    BORO = db.Column(db.String)
    PERP_SEX = db.Column(db.String)
    PERP_RACE = db.Column(db.String)
    VIC_SEX = db.Column(db.String)
    VIC_RACE = db.Column(db.String)
    Latitude = db.Column(db.Float)
    Longitude = db.Column(db.Float)
    DATE = db.Column(db.String) 



    def __repr__(self):
        return '<Shooting %r>' % (self.name)


@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()


# create route that renders index.html template
@app.route("/")

def index():

    return render_template("index.html", data=data)

# def home():
    
#     return render_template("index.html")

@app.route("/data")
def data():
    sel = [func.strftime("%Y", Shooting.DATE), func.count(Shooting.DATE)]
    print(sel)
    results = db.session.query(*sel).\
        group_by(func.strftime("%Y", Shooting.DATE)).all()
    print(results)
    df = pd.DataFrame(results, columns=['year', 'sightings'])
    return jsonify(df.to_dict(orient="records"))

@app.route("/shootingsdata")
def shootingsdata():
    # df = pd.read_csv('shoot_df_small.csv')
    df = pd.read_csv('shoot_dft2.csv')
    chart_data = df.to_dict(orient='records')
    # chart_data = json.dumps(chart_data, indent=2)
    # data = {'chart_data': chart_data}
    return jsonify(chart_data)

@app.route("/weatherdata")
def weatherdata():
    df = pd.read_csv('weathershootings.csv')
    weather_data = df.to_dict(orient='records')
    return jsonify(weather_data)

@app.route("/holidaydata")
def holidaydata():
    df = pd.read_csv('Holiday.csv')
    chart_data = df.to_dict(orient='records')
    # chart_data = json.dumps(chart_data, indent=2)
    # data = {'chart_data': chart_data}
    return jsonify(chart_data)

if __name__ == "__main__":
    app.run(debug=True)
