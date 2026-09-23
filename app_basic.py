from agentic_chatbot_backend import chatbot
from langchain_core.messages import BaseMessage, HumanMessage
import streamlit as st

st.title("Agentic Chatbot with Langgraph")

CONFIG = {'configurable': {'thread_id': '1'}}



if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []


#loading conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])
          


user_input = st.chat_input('Type here')


if user_input:
    #first add the message to message history
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message("user"):
        st.text(user_input)


    #response = chatbot.invoke({'messages':[HumanMessage(content=user_input)]},config=CONFIG)

  #  ai_message = response['messages'][-1].content
    #first add the message to message history

    
#gemini model returns structured content, so we need to extract the text from the structured content
def extract_text(message_chunk):
    content = message_chunk.content

    # Normal string content
    if isinstance(content, str):
        yield content

    # Structured content
    elif isinstance(content, list):
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                text = block.get("text", "")
                if text:
                    yield text


with st.chat_message("assistant"):
    ai_message = st.write_stream(
        text
        for message_chunk, metadata in chatbot.stream(
            {'messages': [HumanMessage(content=user_input)]},
            config=CONFIG,
            stream_mode='messages'
        )
        for text in extract_text(message_chunk)
    )


    st.session_state['message_history'].append({'role':'assistant','content':ai_message})
   # with st.chat_message("assistant"):
   #     st.text(ai_message)
       

    