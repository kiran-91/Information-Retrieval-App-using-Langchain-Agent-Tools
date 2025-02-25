import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv

# Arxiv and Wikipedia API Wrappers
arxiv_wrapper=ArxivAPIWrapper(top_k_results=2, doc_content_chars_max=1000)
arxiv=ArxivQueryRun(api_wrapper=arxiv_wrapper)

wiki_wrapper=WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=1000)
wiki=WikipediaQueryRun(api_wrapper=wiki_wrapper)

search=DuckDuckGoSearchRun(name="DuckDuckGo Search", top_k_results=2)

# streamlit app
st.title("Search using Langchain Agent & Tools")

# streamlit sidebar
st.sidebar.title("Settings & Configuration")
api_key=st.sidebar.text_input("Enter your GROQ APi Key", type="password")
with st.sidebar:
    st.markdown("If you encounter any tool error like `No results found` or `DuckDuckGo search error`, please reload or try again. It may be due to the tool's limitations or the search query.")

if api_key:
    st.success("GROQ API Key is set")
    if "messages" not in st.session_state:
        st.session_state["messages"]=[
            {"role":"assistant", "content":"Hello! I am your assistant. How can I help you today?"}
        ]
        
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt:=st.chat_input(placeholder="Type your message here..."):
        st.session_state.messages.append({"role":"User", "content":prompt})
        st.chat_message("User").write(prompt)
        
        llm=ChatGroq(api_key=api_key, model="Llama-3.3-70b-Versatile", streaming=True)
        tools=[search, arxiv, wiki]
        
        search_agent=initialize_agent(tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True)

        with st.chat_message("assistant"):
            st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=True)
            
            response=search_agent.run(st.session_state.messages, callbacks=[st_cb]) 
            st.session_state.messages.append({"role":"assistant", "content":response})
            st.write(response)   
else:
    st.error("Please enter your GROQ API Key")
    