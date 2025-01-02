# Information Retrieval App using Langchain Agent & Tools

## Project Overview
This project is a **Streamlit-based web application** that integrates with LangChain tools to provide users with efficient, multi-source information retrieval. The app allows users to query academic papers, Wikipedia articles, and web search results using ArXiv, Wikipedia, and DuckDuckGo APIs. It also supports conversational interaction using a large language model (LLM) through the GROQ API.

## Features

- **Conversational Interface**: Engage with a chatbot for natural language queries and responses.
- **Multi-Source Search Tools**:
  - **ArXiv API**: Fetches academic paper summaries from ArXiv.
  - **Wikipedia API**: Provides concise Wikipedia article summaries.
  - **DuckDuckGo API**: Conducts web searches.
- **Streamlit Sidebar**: Includes a configuration panel for users to input their GROQ API key securely.
- **Dynamic Message Handling**: Maintains chat history and processes user prompts seamlessly.
- **LLM Integration**: Powered by the GROQ API for natural language understanding and generating responses.


## Project Structure

```
📁 Project Folder
├── app.py                  # Main entry point for Streamlit
├── .env                    # To store the API keys
├── requirements.txt        # Dependencies for the app
├── Dockerfile              # For docker containerization
└── README.md
```


## Installation

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/kiran-91/Langchain-Agent-Tools-Unlocking-Conversational-AI.git
   cd Langchain-Agent-Tools-Unlocking-Conversational-AI
   ```

2. Create a virtual environment and activate it:
   ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/MacOS
    venv\Scripts\activate  # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your GROQ API key and HuggingFace API key:
   ```env
   GROQ_API_KEY=<GROQ API KEY>
   HF_API_KEY=<HuggingFace API KEY>
   ```

5. Run the application:
   ```bash
   streamlit run app.py
   ```

## How It Works

1. **API Integration**:
   - ArXiv and Wikipedia API Wrappers are initialized with configuration options such as the number of results (`top_k_results`) and content truncation limit (`doc_content_chars_max`).
   - The DuckDuckGo API wrapper is used for broader web search results.

2. **Streamlit Interface**:
   - A sidebar is provided for API key input and configuration.
   - The main chat interface displays the conversation between the user and the chatbot.

3. **LLM and Agent Setup**:
   - The `ChatGroq` class is used to interact with the GROQ-powered LLM.
   - LangChain’s `initialize_agent` function configures the multi-tool agent in a Zero-Shot React framework.

4. **User Interaction**:
   - User inputs are processed via the `st.chat_input` field.
   - The app dynamically updates chat history and displays responses from the integrated agent.



## Usage

1. Start the application by running `streamlit run app.py`.
2. Enter your GROQ API key in the sidebar.
3. Use the chat interface to ask questions or search for information.
4. View the results sourced from ArXiv, Wikipedia, or web searches.

## Dependencies

- **Streamlit**: For building the web interface.
- **LangChain**: For managing tools and LLM integration.
- **ArXiv API Wrapper**: For academic paper search.
- **Wikipedia API Wrapper**: For article summaries.
- **DuckDuckGo Search API**: For web searches.

## Future Enhancements

- Add user authentication for enhanced security.
- Increase the range of tools integrated, such as YouTube or PubMed.
- Optimize LLM usage for better response generation.
- Improve user experience with visual enhancements and loading indicators.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [LangChain](https://www.langchain.com/): For providing a flexible framework for integrating AI tools.
- [Streamlit](https://streamlit.io/): For enabling fast and interactive app development.
- [GROQ API](https://www.groq.com/): For LLM support.

## Contact

For further questions or collaboration, feel free to reach out!

