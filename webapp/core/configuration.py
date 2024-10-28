from typing import Optional

from pydantic import BaseModel, Field
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


class HashingConfig(BaseModel):
    time_cost: Optional[int] = Field(default=None)
    memory_cost: Optional[int] = Field(default=None)
    parallelism: Optional[int] = Field(default=None)
    hash_len: Optional[int] = Field(default=None)
    salt_len: Optional[int] = Field(default=None)


class SecurityConfig(BaseModel):
    tokenize: TokenConfig
    hashing: Optional[HashingConfig] = Field(default=None)


class EnvConfig(BaseSettings):
    datasource: DataSourceConfig
    server: ServerConfig
    security: SecurityConfig

    model_config = SettingsConfigDict(env_nested_delimiter='__')


env_config = EnvConfig()
