import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "Your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    
    flags = []
    question = []

    for arg in args:
        if "--" in arg:
            flags.append(arg)
        else:
            question.append(arg)

    prompt = " ".join(question)

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]

    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

    p_tokens = response.usage_metadata.prompt_token_count # type: ignore
    r_tokens = response.usage_metadata.candidates_token_count # type: ignore

    print(response.text)

    if "--verbose" in flags:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {p_tokens}")
        print(f"Response tokens: {r_tokens}")


main()