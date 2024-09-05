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


class TokenConfig(BaseModel):
    algorithm: str
    secret_key: str
    refresh_secret_key: str
    expire_min: int
    refresh_hours: int


class SecurityConfig(BaseModel):
    tokenize: TokenConfig


class EnvConfig(BaseSettings):
    datasource: DataSourceConfig
    server: ServerConfig
    security: SecurityConfig

    model_config = SettingsConfigDict(env_nested_delimiter='__')


env_config = EnvConfig()
