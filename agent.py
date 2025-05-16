from langgraph.graph import StateGraph, END
from typing import TypedDict
from model_runner import call_model
from weather_tool import get_weather
from prompts import generate_location_prompt
import re
import json


class WeatherState(TypedDict):
    input: str
    location: str
    weather: str


def extract_location_from_model_output(text: str) -> str:
    """
    Extracts the 'location' field from model output, even if the output is malformed or truncated.
    """
    try:
        # Remove 'Output:' or similar prefix
        text = text.strip().replace("Output:", "").strip()
        # Attempt to fix unclosed JSON
        if not text.endswith("}"):
            text += "}"
        # Match using regex fallback if not valid JSON
        json_match = re.search(r'\{"location"\s*:\s*"([^"}]+)', text)
        if json_match:
            return json_match.group(1).strip()
        # Final fallback: try parsing as JSON if it's close
        data = json.loads(text)
        return data.get("location", "unknown")

    except Exception:
        return "unknown"


def extract_location(state: WeatherState) -> WeatherState:
    prompt = generate_location_prompt(state)
    output = call_model(prompt, max_tokens=10).strip()
    location = extract_location_from_model_output(output)

    return {**state, "location": location}


def fetch_weather(state: WeatherState) -> WeatherState:
    city = state["location"]
    weather_info = get_weather(city)

    return {**state, "weather": weather_info}



def format_response(state: WeatherState) -> dict:
    #TODO : Add generated response from state
    report = state
    return report


def weather_agent():
    builder = StateGraph(WeatherState)

    builder.add_node("extract_location", extract_location)
    builder.add_node("fetch_weather", fetch_weather)
    builder.add_node("final_response", format_response)

    builder.set_entry_point("extract_location")
    builder.add_edge("extract_location", "fetch_weather")
    builder.add_edge("fetch_weather", "final_response")
    builder.set_finish_point("final_response")

    return builder.compile()