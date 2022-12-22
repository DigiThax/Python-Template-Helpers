import json
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# create the base class for the ORM classes
Base = declarative_base()

# load the configuration file
with open("config.json", "r") as f:
  config = json.load(f)

# iterate over the tables in the configuration
for table in config["tables"]:
  # define the ORM class for the table
  class_attrs = {}
  for column in table["columns"]:
    # map the column type to the corresponding SQLAlchemy type
    column_type = {
      "integer": Integer,
      "string": String
    }[column["type"]]

    # define the column as an attribute of the ORM class
    class_attrs[column["name"]] = Column(column_type, primary_key=column.get("primary_key", False))

  # create the ORM class
  ORMClass = type(table["name"], (Base,), class_attrs)
  globals()[table["name"]] = ORMClass
