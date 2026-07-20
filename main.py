from dotenv import load_dotenv
from langchain_core import __version__ as core_version
from langchain_openai import ChatOpenAI

print(f"lang version: {core_version}")

load_dotenv()

def main():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    response = llm.invoke("Say 'setup complete' in one word")
    print(f"Response from LLM: {response}")


if __name__ == "__main__":
    main()
