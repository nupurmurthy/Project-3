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
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/db_country.sqlite"
db = SQLAlchemy(app)
# reflect database 
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)
# Save references to each tableO?
# Save references to each table
Samples_Metadata = Base.classes.merged_data
#Samples = Base.classes.GDP


@app.route("/")
def index():
    return render_template("index2.html")


@app.route("/lifeexp")
def lifeexp():
    # Use Pandas to perform the sql query
    query_please = db.session.query(Samples_Metadata).statement
    dataframe = pd.read_sql_query(query_please, db.session.bind)

    return jsonify(list(dataframe.columns)[2:])


@app.route("/test")
def merged_data():
  
    sel = [
        Samples_Metadata.Country_Code,
        Samples_Metadata.Country_Name,
        # Samples_Metadata.Year,
        # Samples_Metadata.Value_Population,
        # Samples_Metadata.Value_Life,
        # Samples_Metadata.Value_GDP,
        
    ]

    results = db.session.query(*sel).all()
    
    # Create a dictionary entry for each row of metadata information
    merged_data = []
    for result in results:
        country = {}
        country["Country_Code"] = result[0]
        country["Country_Name"] = result[1]
        # merged_data["Country_Code"] = result[0]
        # merged_data["Country_Name"] = result[1]
        # merged_data["Year"] = result[2]
        # merged_data["Value_Population"] = result[3]
        # merged_data["Value_Life"] = result[4]
        # merged_data["Value_GDP"] = result[5]
        merged_data.append(country)
    return jsonify(merged_data)



if __name__ == "__main__":
    app.run()