from fastapi import FastAPI

app=FastAPI()

@app.get("/laya")

def hi():
    return {"message":"hello world"}




