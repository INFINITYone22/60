from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the database engine
engine = create_engine('sqlite:///mydatabase.db', echo=True)

# Define the base class for declarative models
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age})>"

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create new users
john = User(name='John Doe', age=30)
jane = User(name='Jane Smith', age=25)

# Add the users to the session
session.add_all([john, jane])

# Commit the changes to the database
session.commit()

# Query the users
users = session.query(User).all()
print("Users:")
for user in users:
    print(user)

# Close the session
session.close()
