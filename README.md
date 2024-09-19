# FastAPI + SQLModel Layered Architecture Example

---

Based on [FastAPI](https://fastapi.tiangolo.com) and [SQLModel](https://sqlmodel.tiangolo.com/)

It has [Spring](https://spring.io/)-Like Layered Architecture Structure

FastAPI's default `Depends()` is used for Dependency Injection.


using [ColorLog](https://github.com/borntyping/python-colorlog) for timestamped log



---

using dotenv as configuration

```shell

DATASOURCE__DIALECT=sqlite
DATASOURCE__DRIVER=
DATASOURCE__USERNAME=
DATASOURCE__PASSWORD=
DATASOURCE__HOST=
DATASOURCE__PORT=
DATASOURCE__DATABASE=./webapp.db

SERVER__HOST=0.0.0.0
SERVER__PORT=8000

SECURITY__TOKENIZE__ALGORITHM=
SECURITY__TOKENIZE__SECRET_KEY=
SECURITY__TOKENIZE__REFRESH_SECRET_KEY=
SECURITY__TOKENIZE__EXPIRE_MIN=
SECURITY__TOKENIZE__REFRESH_HOURS=

```

set those parameters to set configuration
