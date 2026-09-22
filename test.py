from agentic_chatbot_backend import chatbot
from langchain_core.messages import BaseMessage, HumanMessage



CONFIG = {'configurable': {'thread_id': 'thread-1'}}

# By using the invoke method, you can get the entire response at once.
# response = chatbot.invoke(
#     {'messages': [HumanMessage(content="Generate a blog about Machine learning")]},
#     config=CONFIG
# )
# print(response['messages'][-1].content)

for message_chunk, metadata in chatbot.stream(
    {'messages': [HumanMessage(content="Generate a blog about Machine learning")]},
    config=CONFIG,
    stream_mode='messages'
):
    if message_chunk.content:
        print(message_chunk.content, end=" ", flush=True)
    

