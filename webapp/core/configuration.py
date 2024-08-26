#
# from pydantic import BaseModel
# class DatabaseConfig(Base):
#
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DataSourceConfig(BaseModel):
    dialect: str
    driver: str
    username: str
    password: str
    host: str
    port: int
    database: str


class ServerConfig(BaseModel):
    host: str
    port: int


class EnvConfig(BaseSettings):
    datasource: DataSourceConfig
    server: ServerConfig

    model_config = SettingsConfigDict(env_nested_delimiter='__')


env_config = EnvConfig()
