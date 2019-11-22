import os
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


# Database Setup
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/bellybutton.sqlite"
db = SQLAlchemy(app)
# reflect database 
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)
# Save references to each table
Samples_Metadata = Base.classes.sample_metadata
Samples = Base.classes.samples


@app.route("/")
def index():
    return render_template("index2.html")


@app.route("/lifeexp")
def names():
    # Use Pandas to perform the sql query
    query_please = db.session.query(Samples).statement
    df = pd.read_sql_query(query_please, db.session.bind)

    return jsonify()


@app.route("/esgdata/<sample>")
def sample_metadata(sample):

    # Add query data to dictionary 
    sel = [Samples_Metadata.sample, Samples_Metadata.sample2]
    results = db.session.query(*sel).filter(Samples_Metadata.sample == sample).all()

    # Pass data to dictionary
    sample_metadata = {}
    for result in results:
        sample_metadata["sample"] = result[0]
        sample_metadata["sample2"] = result[1]

    print(sample_metadata)
    return jsonify(sample_metadata)




if __name__ == "__main__":
    app.run()
