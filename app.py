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

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant", "content":"Hello! I am your assistant. How can I help you today?"}
    ]
    
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt:=st.chat_input(placeholder="Type your message here..."):
    st.session_state.messages.append({"role":"User", "content":prompt})
    st.chat_message("User").write(prompt)
    
    llm=ChatGroq(api_key=api_key, model="Llama3-8b-8192", streaming=True)
    tools=[search, arxiv, wiki]
    
    search_agent=initialize_agent(tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handling_parsing_errors=True)

    with st.chat_message("assistant"):
        st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=True)
        
        response=search_agent.run(st.session_state.messages, callbacks=[st_cb]) 
        st.session_state.messages.append({"role":"assistant", "content":response})
        st.write(response)   
    