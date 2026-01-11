import ollama

class LLMHandler:
    def __init__(self, model_name="llama3"):
        self.model_name = model_name
        # Check if we can connect to Ollama (optional, could just let it fail later)
        try:
            # Simple list call to check connection
            ollama.list()
            print(f"Connected to Ollama. Using model: {model_name}")
        except Exception as e:
            print(f"Warning: Could not connect to Ollama: {e}")
            print("Make sure 'ollama serve' is running.")

    def summarize(self, text):
        prompt = f"Summarize the following text concisely:\n\n{text}"
        try:
            response = ollama.chat(model=self.model_name, messages=[
                {'role': 'user', 'content': prompt},
            ])
            return response['message']['content']
        except Exception as e:
            return f"Error using Ollama: {e}"

    def decide_action(self, text):
        # Placeholder for more complex logic
        prompt = f"Analyze the following text and suggest an action (or say 'No action needed'):\n\n{text}"
        try:
            response = ollama.chat(model=self.model_name, messages=[
                {'role': 'user', 'content': prompt},
            ])
            return response['message']['content']
        except Exception as e:
            return f"Error using Ollama: {e}"
if __name__  == "__main__":
    lama = LLMHandler("gemma3:1b")
    result = lama.summarize("hi")
    print(result)