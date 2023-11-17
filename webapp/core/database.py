from logging import getLogger

from sqlmodel import create_engine, SQLModel, Session

logger = getLogger(__name__)

connect_url = "sqlite:///./webapp.db"

engine = create_engine(connect_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    session = Session(engine)
    try:
        yield session
    except Exception:
        logger.exception("Session rollback because of exception")
        session.rollback()
    finally:
        session.close()
