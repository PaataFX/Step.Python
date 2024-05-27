# Object-relational mapping (ORM)
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine

Base = declarative_base()

class Person(Base):
    __tablename__ = "persons"

    id = Column("id", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    house = Column("house", String)
    patronus = Column("patronus", String)
    blood_status = Column("blood_status", String)

    def __init__(self, id, firstname, lastname, house, patronus, blood_status):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.house = house
        self.patronus = patronus
        self.blood_status = blood_status

    def __repr__(self):
        return f"{self.id} / {self.firstname} / {self.lastname} / {self.house} / {self.patronus} / {self.blood_status}"

# sqlite
# engine = create_engine("sqlite:///mydb.db")
engine = create_engine("sqlite:///")
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


characters = [
    Person(1, "Harry", "Potter", "Gryffindor", "Stag", "Half-Blood"),
    Person(2, "Hermione", "Granger", "Gryffindor", "Otter", "Muggle-Born"),
    Person(3, "Ron", "Weasley", "Gryffindor", "Jack Russell Terrier", "Pure-Blood"),
    Person(4, "Draco", "Malfoy", "Slytherin", None, "Pure-Blood"),
    Person(5, "Severus", "Snape", "Slytherin", "Doe", "Half-Blood"),
    Person(6, "Albus", "Dumbledore", "Gryffindor", "Phoenix", "Half-Blood"),
    Person(7, "Voldemort", "Riddle", "Slytherin", None, "Half-Blood"),
    Person(8, "Sirius", "Black", "Gryffindor", "German Shepherd", "Pure-Blood"),
    Person(9, "Luna", "Lovegood", "Ravenclaw", "Hare", "Pure-Blood"),
    Person(10, "Neville", "Longbottom", "Gryffindor", "Non-corporeal", "Pure-Blood")
]

for character in characters:
    session.add(character)

session.commit()

info = session.query(Person).all()
for per in info:
    print(per)
