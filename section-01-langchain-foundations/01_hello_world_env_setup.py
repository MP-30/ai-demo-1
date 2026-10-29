import  os
from dotenv import load_dotenv

load_dotenv()

def describe_secret(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        return f"{name} is missing"
    return f"{name} loaded env"

def main() -> None:
    print("Hello from future - ai demo")
    print(describe_secret("OPENAI_KEY"))
    tracing = os.environ.get("LANGSMITH _TRACING", "(not set")
    hint = (
        "tracing is optional"
        if tracing != "true"
        else " runs will appar in LangSmith"
    )
    print(f"LANGSMITH_TRACING = {tracing} {hint}")

if __name__ == "__main__":
    main()
import os
from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, APIConnectionError, APIError


# load_dotenv()
#
# def verify_openai_key(api_key: str | None = None) -> bool:
#     key = api_key or os.getenv("OPENAI_KEY")
#
#     if not key:
#         print("Error: 'OPENAI_KEY' not found in .env or environment.")
#         return False
#
#     client = OpenAI(api_key=key)
#
#     try:
#         # Lightweight metadata call to confirm authentication
#         client.models.list()
#         print("API key is valid and working.")
#         return True
#     except AuthenticationError:
#         print("Authentication failed: Invalid or revoked API key.")
#         return False
#     except APIConnectionError:
#         print("Network error: Could not reach OpenAI API endpoints.")
#         return False
#     except APIError as e:
#         print(f"OpenAI API error ({e.status_code}): {e.message}")
#         return False
#     except Exception as e:
#         print(f"Unexpected error: {e}")
#         return False
#
# if __name__ == "__main__":
#     verify_openai_key()