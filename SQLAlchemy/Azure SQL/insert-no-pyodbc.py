# import the necessary modules
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# define the connection string
connection_string = "mssql+pymssql://{username}:{password}@{server}.database.windows.net/{database}"

# create the engine
engine = create_engine(connection_string)

# create the base class for the ORM classes
Base = declarative_base()

# define the ORM class for the table
class User(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True)
  name = Column(String)
  age = Column(Integer)

# create the table in the database
Base.metadata.create_all(engine)

# create a session
Session = sessionmaker(bind=engine)
session = Session()

# create a new user object
user = User(name="John", age=30)

# add the user to the session
session.add(user)

# commit the changes to the database
session.commit()