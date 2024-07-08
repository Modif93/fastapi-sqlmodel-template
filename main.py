import uvicorn



if __name__ == '__main__':
    uvicorn.run("webapp.application:app",log_config="log.ini")

