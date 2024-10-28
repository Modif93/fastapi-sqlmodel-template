import logging

from sqlalchemy import URL
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine, SQLModel

from webapp.core.configuration import env_config

logger = logging.getLogger(__name__)


class SessionManager:
    def __init__(self, _connect_url):
        self._engine = create_engine(_connect_url, echo=False)
        self.SessionMaker = sessionmaker(bind=self._engine)


    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self._engine)

    @staticmethod
    def get_db_conn_url(dialect, driver, username, password, host, port, database):
        if dialect == 'sqlite':
            return f"sqlite:///{database}"

        return URL.create(
            drivername=f"{dialect}+{driver}",
            username=username,
            password=password,
            host=host,
            port=port,
            database=database,
        )


connect_url = SessionManager.get_db_conn_url(**env_config.datasource.model_dump())
session_manager = SessionManager(connect_url)


def get_session():
    with session_manager.SessionMaker() as session:
        try:
            yield session
        except SQLAlchemyError as err:
            logger.exception(err)
            session.rollback()
        finally:
            session.close()
