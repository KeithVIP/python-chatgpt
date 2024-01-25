import openai
from openai import OpenAI
import os
from dotenv import load_dotenv

# load the API key from the .env file
load_dotenv()
client = OpenAI(api_key=os.environ.get("API_KEY"))

# Load the API key from the .env file
load_dotenv()
client = OpenAI(api_key=os.environ.get("API_KEY"))

#Chatbot function
def get_chatbot_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chat session ended.")
        break
    response = get_chatbot_response(user_input)
    print("ChatGPT:", response)
# def generate_content(prompt):
#     try:
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": 'prompt' }],
#             temperature=1,
#             max_tokens=250
#         )
#         return response.choices[0].message.content
#     except Exception as e:
#         return str(e)
    
#     # Use this function to generate content
#     description = generate_content("Write a short description of a snowboard")


# "Try" to create a chat completion to handle status codes
# try:
#     chat_completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": "query"}],
#         temperature=1,
#         max_tokens=150  # Adjust the number of tokens as needed
#     )
    # print(chat_completion.choices[0].message.content)

# except openai.APIConnectionError as e:
#     print("The server could not be reached")
#     print(e.__cause__)

# except openai.RateLimitError as e:
#     print("A 429 status code was received; we should back off a bit.")

# except openai.APIStatusError as e:
#     print("Another non-200-range status code was received")
#     print(e.status_code)
#     print(e.response)
