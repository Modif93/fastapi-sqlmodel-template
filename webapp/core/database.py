import logging

from sqlalchemy import URL
from sqlmodel import create_engine, SQLModel, Session

from webapp.core.configuration import env_config

logger = logging.getLogger(__name__)


class SessionManager:
    def __init__(self, _connect_url):
        self._engine = create_engine(_connect_url, echo=False)

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

    def __enter__(self):
        self._session = Session(self._engine)
        return self._session

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            logger.exception("Session rollback because of exception")
            self._session.rollback()
        # 세션 닫기
        self._session.close()


connect_url = SessionManager.get_db_conn_url(**env_config.datasource.model_dump())
session_manager = SessionManager(connect_url)


def get_session():
    with session_manager as session:
        yield session
