import streamlit as st
import asyncio
from fastmcp import Client

st.title(" Wikipedia MCP Agent")

query = st.text_input("Enter topic:")

async def call_mcp(query):
    client = Client("http://localhost:8000/mcp")

    async with client:
        result = await client.call_tool(
            "search_wikipedia",
            {"query": query}
        )
        return result

# if st.button("Search"):
#     if query:
#         result = asyncio.run(call_mcp(query))
#         st.write("### Result:")
#         st.write(result)
#     else:
#         st.warning("Please enter a topic")

if st.button("Search"):
    if query:
        result = asyncio.run(call_mcp(query))
        
        # ✅ Extract clean text
        try:
            clean_output = result.structured_content["result"]
        except:
            clean_output = str(result)

        st.write("### Result:")
        st.write(clean_output)
    else:
        st.warning("Please enter a topic")

        