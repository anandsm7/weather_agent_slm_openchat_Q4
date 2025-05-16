from fastapi import FastAPI
from agent import weather_agent

app = FastAPI()
agent = weather_agent()

@app.get("/health")
def check_weather():
    return {"status": 200}

@app.get("/weather")
def check_weather(q: str):
    result = agent.invoke({"input": q})
    return {"response": result}