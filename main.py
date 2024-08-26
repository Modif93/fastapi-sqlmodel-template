import uvicorn
import os

if __name__ == '__main__':
    host = os.getenv("SERVER__HOST")
    port = os.getenv("SERVER__PORT")
    uvicorn.run("webapp.application:app",
                host=host,
                port=int(port), reload=True,

                log_config="log.ini")
