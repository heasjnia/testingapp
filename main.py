from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/check")
def check_endpoint(param: str = Query(...)):
    """
    Endpoint that checks if the param is 'ping' and returns 'pong'
    """
    if param == "ping":
        return PlainTextResponse("pong")
    else:
        return PlainTextResponse("invalid parameter")
