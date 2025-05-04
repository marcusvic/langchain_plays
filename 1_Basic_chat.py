from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
import os
# we're using this to parse the outputs of the model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate  # creates prompt templates
os.environ

# Loading the .env file. Using full path to use it in the interactive shell
load_dotenv("C:\\Users\\MarcusChiri\\Dropbox\\Repositories\\Langchain\\.env")

# Loarding the environment variables
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

model = ChatOpenAI(model="gpt-4")

messages = [
    SystemMessage(
        content="Translate the following from English into Portuguese:"),
    HumanMessage(content="see you later!"),
]

message_detail = model.invoke(messages)

# creating a new instance of the parser, which is used to parse the output of the model
parser = StrOutputParser()

# here we're passing the output of the model to the parser, which will convert it into a string
parser.invoke(message_detail)

# however, the magic in langchain is chaining stuff:
chain = model | parser
# this is a chain that takes the output of the model and passes it to the parser

chain.invoke(messages)

system_template = "Translate the following into {Language}:"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

result = prompt_template.invoke({"language": "italian", "text": "hi"})

result
