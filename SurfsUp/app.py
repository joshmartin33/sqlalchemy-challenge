
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

#### Question 1 / landing page ####

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"<H1>Available Routes:</H1><br/>"
        f"<br/>"
        f"<em>Return the last 12 months precipitation data.</em><br/>"
        f"<strong>/api/v1.0/precipitation</strong><br/>"
        f"<br/>"
        f"<em>Return all stations data</em><br/>"
        f"<strong>/api/v1.0/stations</strong><br/>"
        f"<br/>"
        f"<em>Return last 12 month temperature observations and dates of the most-active station</em><br/>"
        f"<strong>/api/v1.0/tobs</strong><br/>"
        f"<br/>"
        f"<br/>"
        f"<em>Return Max, Min and average temperature from or between ranges</em><br/>"
        f"'start-date' and 'end-date' format to be supplied as <em>yyyy-mm-dd</em>.<br/>"
        f"<br/>"
        f"<strong>/api/v1.0/'start-date'</strong><br/>"
        f"(eg. '/api/v1.0/2016-04-24' will give results from the 24th of April 2016 and greater)<br/>"
        f"<br/>"
        f"<strong>/api/v1.0/'start-date'/'end-date'</strong><br/>"
        f"(eg. '/api/v1.0/2016-04-24/2017-07-23' will give results from the 24th of April 2016 to 23rd of July 2017)<br/>"
       
    )

#### Question 2 /api/v1.0/precipitation ####

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Retrieve only the last 12 months of data"""
    # Query measurement db for last 12 months
    results = session.query(Measurement.date, Measurement.prcp)\
        .filter(Measurement.date > '2016-08-23')\
        .filter(Measurement.date <= '2017-08-23')\
        .order_by(Measurement.date)\
        .all()

    session.close()

    # Create a dictionary from the row data and append to a list of precipitation_12_months
    precipitation_12_months = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict[date] = prcp
        precipitation_12_months.append(precipitation_dict)

    return jsonify(precipitation_12_months)

#### Question 3 /api/v1.0/stations ####

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations from the dataset"""
    # Query all stations
    results = session.query(Station.station, Station.name,\
             Station.latitude, Station.longitude, Station.elevation)\
            .all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_stations
    all_stations = []
    for station, name, latitude, longitude, elevation in results:
        stations_dict = {}
        stations_dict["station"] = station
        stations_dict["name"] = name
        stations_dict["latitude"] = latitude
        stations_dict["longitude"] = longitude
        stations_dict["elevation"] = elevation
        all_stations.append(stations_dict)

    return jsonify(all_stations)

#### Question 4 /api/v1.0/tobs ####

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of temperature observations for the previous year"""
    # Query the dates and temperature observations of the most-active station for the previous year of data.
    results = session.query(Measurement.date, Measurement.tobs)\
                .filter(Measurement.station == "USC00519281")\
                .filter(Measurement.date > '2016-08-18')\
                .filter(Measurement.date <= '2017-08-18')\
                .order_by(Measurement.date)\
                .all()

    session.close()

    # Create a dictionary from the row data and append to a list of tobs_12_months
    tobs_12_months = []
    tobs_USC00519281 = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict[date] = tobs
        tobs_12_months.append(tobs_dict)
    tobs_dict2 = {}
    tobs_dict2["USC00519281"] = tobs_12_months
    tobs_USC00519281.append(tobs_dict2)

    return jsonify(tobs_USC00519281)

#### Question 5 /api/v1.0/<start> ####

@app.route("/api/v1.0/<start>")
def start_date(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Retrieve only the data from specific start date"""
    # Query tobs min, max and avg from start date range
    start_date = start
    results = session.query(func.min(Measurement.tobs)\
                , func.max(Measurement.tobs)\
                , func.round(func.AVG(Measurement.tobs),2))\
                .filter(Measurement.date >= start_date)\
                .all()

    session.close()

    # Create a dictionary from the row data and append to a list of start_months
    start_months = []
    for min, max, avg in results:
        start_dict = {}
        start_dict["min"] = min
        start_dict["max"] = max
        start_dict["avg"] = avg
        start_months.append(start_dict)

    return jsonify(start_months)

#### Question 5 /api/v1.0/<start>/<end> ####

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Retrieve only the data between date ranges"""
    # Query tobs min, max and avg between start and end date ranges
    start_date = start
    end_date = end
    results = session.query(func.min(Measurement.tobs)\
                , func.max(Measurement.tobs)\
                , func.round(func.AVG(Measurement.tobs),2))\
                .filter(Measurement.date >= start_date)\
                .filter(Measurement.date <= end_date)\
                .all()

    session.close()

    # Create a dictionary from the row data and append to a list of start_end_months
    start_end_months = []
    for min, max, avg in results:
        start_dict = {}
        start_dict["min"] = min
        start_dict["max"] = max
        start_dict["avg"] = avg
        start_end_months.append(start_dict)

    return jsonify(start_end_months)

if __name__ == '__main__':
    app.run(debug=True)