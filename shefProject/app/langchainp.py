from dotenv import load_dotenv
import os

from langchain_cohere import ChatCohere
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate, HumanMessagePromptTemplate

load_dotenv()

secret_key=os.getenv("secret_key")






def ask(recipe_message):

    # Define the Cohere LLM
    llm = ChatCohere(
        cohere_api_key=secret_key, model="command-a-03-2025"
    )
    
    systemMessagePrompt=SystemMessagePromptTemplate.from_template(

    
    "Your Name is Riaz. You are a doctor. So first introduce yourself as Riaz a MBBS doctor. You can help by providing medical sussgestion. You only allowed to answer medical related queries. If you don't know the answer then tell I don't know the answer"
    )
    
    humanMessagePrompt=HumanMessagePromptTemplate.from_template(
        '{asked_recipe}'
    )
    
    chatPrompt=ChatPromptTemplate.from_messages([
        systemMessagePrompt, humanMessagePrompt
    ])
    
    formattedChatPrompt=chatPrompt.format_messages(

        asked_recipe=recipe_message
    )
    # current_message = [HumanMessage(recipe_message)]
    # print(current_message)
    return llm.invoke(formattedChatPrompt).content