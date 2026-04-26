from google import genai
from termcolor import colored

class CodemAgent():
    def __init__(self):
        self.client = genai.Client()

    def get_message(self):
        try:
            user_input = input()
            return user_input, bool(user_input)
        except EOFError as e:
            return "", False


    def run_inference(self, conversation):
        return self.client.models.generate_content(
            model="gemini-3.1-flash-lite-preview",
            contents=conversation,
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
                "parts": [{"text": reply}]
            })

            print(reply)

            

def main():
    codem = CodemAgent()
    codem.run()


if __name__ == "__main__":
    main()

