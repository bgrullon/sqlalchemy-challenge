# Import the dependencies for Flask and SQLAlchemy
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np


#################################################
# Database Setup
#################################################


# reflect an existing database into a new model
Base = automap_base()
engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo=False)

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# our session (link) from Python to the DB
def get_session():
    return Session(bind=engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


@app.route("/")
def homepage():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"<br/>"
        f"precipitation: /api/v1.0/precipitation<br/>"
        f"<br/>"
        f"stations: /api/v1.0/stations<br/>"
        f"<br/>"
        f"tobs: /api/v1.0/tobs<br/>"
        f"<br/>"
        f"start: /api/v1.0/start<br/>"
        f"<br/>"
        f"start/end: /api/v1.0/start/end<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of all precipitation"""
    # Query all precipitation
    session = get_session()
    results = session.query(Measurement.date, Measurement.
                            prcp).order_by(Measurement.date).all()
    
    # a dictionary from the row data and append to a list of precipitation
    precipitation = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        precipitation.append(precipitation_dict)

    return jsonify(precipitation)

# a flask endpoint as /api/v1.0/stations and a function called stations what returns a list of all stations
@app.route("/api/v1.0/stations")
def stations():
    """Return a list of all stations"""
    # Query all stations
    session = get_session()
    results = session.query(Station.station).all()

    # Convert list of tuples into normal list
    stations = list(np.ravel(results))

    return jsonify(stations)

# a flask endpoint as /api/v1.0/tobs and a function called tobs what returns a list of all tobs
@app.route("/api/v1.0/tobs")
def tobs():
    """Return a list of all tobs"""
    # Query all tobs
    session = get_session()
    results = session.query(Measurement.tobs).all()

    # Convert list of tuples into normal list
    tobs = list(np.ravel(results))

    return jsonify(tobs)

# a flask endpoint as /api/v1.0/start and a function called start what returns a list of all start
@app.route("/api/v1.0/start")
def start():
    """Return a list of all start"""
    # Query all start
    session = get_session()
    results = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= "2016-08-23").\
        group_by(Measurement.date).\
        order_by(Measurement.date).all()

    # Convert list of tuples into normal list
    start = list(np.ravel(results))

    return jsonify(start)

# a flask endpoint as /api/v1.0/start/end and a function called start/end what returns a list of all start/end
@app.route("/api/v1.0/start/end")
def start_end():
    """Return a list of all start/end"""
    # Query all start/end
    session = get_session()
    results = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= "2016-08-23").\
        filter(Measurement.date <= "2017-08-23").\
        group_by(Measurement.date).\
        order_by(Measurement.date).all()

    # Convert list of tuples into normal list
    start_end = list(np.ravel(results))

    return jsonify(start_end)


if __name__ == '__main__':
    app.run(debug=True)