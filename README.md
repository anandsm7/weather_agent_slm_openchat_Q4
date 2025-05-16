# weather_agent_slm_openchat_Q4


A weather checking Agent using 4 bit Quantized Small Language Model and Langgraph


Let's you check the weather details of all location by Agentic workflow. 


**Installtion guide:**

1. Model Setup
   1. https://huggingface.co/openchat/openchat-3.5-0106
2. Install requirements
   <pre>pip install requirements.txt</pre>
2. Setup weather API 
   1. Login in to : https://www.weatherapi.com/my/
   2. Generate API key and repalce the key in config.py
3. Run the FAST API service
    <pre>uvicorn main:app --reload</pre>




Test the endpoint
<pre>curl"http://localhost:8000/weather?q=What's the weather in miami?"</pre>

<pre>
{
    "response": {
        "input": "What's the weather in miami?",
        "location": "Miami",
        "weather": "The weather in Miami located in Florida, United States of America with a temperature of 25.3°C."
    }
}
</pre>