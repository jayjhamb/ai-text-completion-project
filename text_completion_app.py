import openai
import os

def load_api_key():
    ## Load API key securely from environment variable.
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")
    return api_key

def get_user_prompt():
    ## Prompt user for input and validate it.
    prompt = input("\nEnter your prompt (or type 'exit' to quit): ").strip()
    if not prompt:
        print("Prompt cannot be empty. Try again.")
        return get_user_prompt()
    return prompt

def get_model_parameters():
    ## Allow user to customize temperature and max_tokens.
    try:
        temperature = float(input("Set temperature (0.0 - 1.0, default=0.7): ") or 0.7)
        max_tokens = int(input("Set max tokens (default=150): ") or 150)
        return temperature, max_tokens
    except ValueError:
        print("Invalid input. Using default parameters.")
        return 0.7, 150

def generate_completion(prompt, temperature=0.7, max_tokens=150):
    ## Send request to OpenAI API and return generated text.
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  ## Use gpt-4 if you have access
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Welcome to the AI Text Completion App (OpenAI GPT-3.5)")
    openai.api_key = load_api_key()

    while True:
        prompt = get_user_prompt()
        if prompt.lower() == "exit":
            print("Goodbye!")
            break

        temperature, max_tokens = get_model_parameters()
        print("\nGenerating response...\n")
        output = generate_completion(prompt, temperature, max_tokens)
        print(f"Response:\n{output}\n")

if __name__ == "__main__":
    main()
