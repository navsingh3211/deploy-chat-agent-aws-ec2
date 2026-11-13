import warnings
warnings.filterwarnings('ignore')

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenAI model
model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

# Create agent
chat_agent = create_agent(
    model=model,
)
