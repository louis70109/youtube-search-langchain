import os

from youtube import FindYoutubeVideoTool
if os.getenv('API_ENV') != 'production':
    from dotenv import load_dotenv

    load_dotenv()

import uvicorn
import logging
from fastapi import FastAPI
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType
from langchain.agents import initialize_agent


logging.basicConfig(level=os.getenv('LOG', 'WARNING'))
logger = logging.getLogger(__file__)
app = FastAPI()
model = ChatOpenAI(model="gpt-3.5-turbo-0613")
tools = [FindYoutubeVideoTool()]
open_ai_agent = initialize_agent(
    tools,
    model,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=False)


@app.get("/api")
def handle_callback(q: str):
    logging.info(f"testing...data is {q}")
    tool_result = open_ai_agent.run(q)
    return tool_result

if __name__ == "__main__":
    port = int(os.environ.get('PORT', default=8080))
    debug = True if os.environ.get(
        'API_ENV', default='develop') == 'develop' else False
    logging.info('Application will start...')
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=debug)
