from langchain.chat_models import ChatOpenAI

# Set up the agent from LangChain with LLM Model and parameters

def setup_agent(temperature=0.7):
    """
        This function sets up or initiates the GPT LLM agent
    """
    agent = ChatOpenAI(model="gpt-3.5-turbo", temperature=temperature)
    return agent
