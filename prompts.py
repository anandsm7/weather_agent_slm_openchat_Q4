def generate_location_prompt(state):

    LOCATION_PROMPT = f"""You are an information extraction system that returns only structured JSON data.
    
    Your task is to extract the **city or geographic location** from the given query. Return exactly one JSON object with a single key `"location"`.
    
    ### Rules:
    - Return only the location as a string (city, town, or well-known geographic place).
    - Do not return country, state, or general region unless that is the only location mentioned.
    - If no location is clearly mentioned, return `"unknown"`.
    - Do NOT include any additional explanation or text. Only output JSON.
    
    ### Format:
    {{"location": "<city_or_location>"}}
    
    ### Example:
    Query: "What is the weather like in Mumbai?"
    Output: {{"location": "Mumbai"}}
    
    Query: "{state['input']}"
    """
    return LOCATION_PROMPT