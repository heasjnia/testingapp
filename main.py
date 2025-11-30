from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/check")
def check_endpoint(param: str = Query(...)):
    """
    Endpoint that checks if the param is 'ping' and returns 'pong'
    """
    if param == "ping":
        return JSONResponse({"message": "pong"})
    else:
        return JSONResponse({"message": "invalid parameter"})
