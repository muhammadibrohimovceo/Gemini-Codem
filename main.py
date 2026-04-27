from google import genai
from google.genai import types
from termcolor import colored
from agent_tools import read_file_defenition

class CodemAgent():
    def __init__(self):
        self.client = genai.Client()
        self.tools = [read_file_defenition]

    def get_message(self):
        try:
            user_input = input()
            return user_input, bool(user_input)
        except Exception:
            return "", False


    def run_inference(self, conversation):

        tools = [{
            "function_declarations": [
                {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.input_schema
                }
            ]
        } for tool in self.tools]

        return self.client.models.generate_content(
            model="gemini-3.1-flash-lite-preview",
            contents=conversation,
            tools=tools
        )


    def run(self):
        conversation = [] 
        print("Chat with Gemini (use 'ctrl+d' to quit)")
 
        while True:
            print(colored("You: ", "blue"), end="")

            user_input, ok = self.get_message()
            if not ok:
                break

            user_message = {
                "role": "user",
                "parts": [{"text": user_input}]
            }
            conversation.append(user_message)

            message = self.run_inference(conversation)
            reply = message.text

            conversation.append({
                "role": "model",
                "parts": [{"text": reply}],
            })

            print(reply)


def main():
    codem = CodemAgent()
    codem.run()


if __name__ == "__main__":
    main()

