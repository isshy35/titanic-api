from src import db


class Person(db.Model):
    __tablename__ = "people"

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def update(self, data: dict) -> None:
        """
        Update attributes of a person.

        Parameters:
            data: dict containing attributes to be updated.
                  Missing attributes remain unchanged.
        """
        for key, value in data.items():
            setattr(self, key, value)
        db.session.commit()

    def delete(self) -> None:
        """
        Delete a person from the database.
        """
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all() -> list:
        """
        Get all people from the database.
        """
        return Person.query.all()

    @staticmethod
    def get_by_id(person_uuid: str) -> "Person":
        """
        Get a person by UUID.
        """
        return Person.query.get(person_uuid)

    def __str__(self) -> str:
        """
        Human-readable string representation.
        """
        return f"<Person {self.id}>"
