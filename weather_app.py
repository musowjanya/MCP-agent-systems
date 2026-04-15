import streamlit as st
import asyncio
from fastmcp import Client

st.title("🌦️ Weather MCP Agent")

city = st.text_input("Enter city name:")

async def call_weather(city):
    client = Client("http://localhost:8000/mcp")

    async with client:
        result = await client.call_tool(
            "get_weather",
            {"city": city}
        )
        return result

def run_async(city):
    return asyncio.run(call_weather(city))

if st.button("Get Weather"):
    if city:
        with st.spinner("Fetching weather..."):
            result = run_async(city)

            # Extract clean output
            try:
                output = result.structured_content["result"]
            except:
                output = str(result)

        st.success(output)
    else:
        st.warning("Please enter a city name")