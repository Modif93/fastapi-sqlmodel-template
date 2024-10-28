from typing import Optional

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DataSourceConfig(BaseModel):
    dialect: str
    driver: Optional[str] = Field(default=None)
    username: Optional[str] = Field(default=None)
    password: Optional[str] = Field(default=None)
    host: Optional[str] = Field(default=None)
    port: Optional[int] = Field(default=None)
    database: str


class ServerConfig(BaseModel):
    host: str
    port: int


class TokenConfig(BaseModel):
    algorithm: str
    secret_key: str
    expire_min: int
    issuer: Optional[str] = Field(default=None)



class HashingConfig(BaseModel):
    time_cost: Optional[int] = Field(default=None)
    memory_cost: Optional[int] = Field(default=None)
    parallelism: Optional[int] = Field(default=None)
    hash_len: Optional[int] = Field(default=None)
    salt_len: Optional[int] = Field(default=None)


class SecurityConfig(BaseModel):
    access_token: TokenConfig
    refresh_token: TokenConfig
    hashing: Optional[HashingConfig] = Field(default=None)


class EnvConfig(BaseSettings):
    datasource: DataSourceConfig
    server: ServerConfig
    security: SecurityConfig

    model_config = SettingsConfigDict(env_nested_delimiter='__')


env_config = EnvConfig()
