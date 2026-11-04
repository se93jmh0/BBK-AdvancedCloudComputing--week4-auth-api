from database import get_db
from sqlalchemy.orm import Session


def test_get_db():
    session = next(get_db())

    assert isinstance(session, Session)
