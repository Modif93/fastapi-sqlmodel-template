from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel,Field,Column, SmallInteger,DateTime


class Audit(SQLModel, table=True):
    state: Optional[int] = Field(sa_column=Column(SmallInteger, nullable=False))
    reg_dt: Optional[datetime] = Field(sa_column=Column(DateTime))
    mod_dt: Optional[datetime] = Field(sa_column=Column(DateTime))
    del_dt: Optional[datetime] = Field(sa_column=Column(DateTime))