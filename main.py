import app
from app.models import Author, Book
from app.database import Session

session = Session()

new_author = Author(name="John Smith")
session.add(new_author)
session.commit

authors = session.query(Author).all()
for author in authors:
    print(author.name)

author_to_update = session.query(Author).filter_by(name="John Smith").first()
author_to_update.name = "John Doe"
session.commit()

author_to_delete = session.query(Author).filter_by(name="John Doe").first()
session.delete(author_to_delete)
session.commit()


