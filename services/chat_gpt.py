"""Code section to add features related to chat_gpt
"""

import os
import sys

import openai
from services.config import OPENAI_API_KEY, OPENAI_API_ORG


def request(prompt: str) -> str:
    """Returns the response to your query one at a time

    Args:
        prompt (str): Query string to chatGPT

    Returns:
        str: Response to the query string
    """
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{prompt}",
        temperature=0.2,
        max_tokens=150,
        stop=["!!"],
    )
    return response


def gpt(query=None):
    """main function to instantiate"""
    result = None
    openai.organization = OPENAI_API_ORG
    openai.api_key = OPENAI_API_KEY
    # models = openai.Model.list()

    if query:
        response = request(query)
        result = response["choices"][0]["text"]
        print(f"Query: {query}")
        print(f"Response: {result}")
    return result.strip()


def main(query=None):
    """main function to instantiate"""
    openai.organization = OPENAI_API_ORG
    openai.api_key = OPENAI_API_KEY
    models = openai.Model.list()
    print(models)

    print("Hello I am Anant - Solution to all problems....\n")
    while True:
        query = input(">>> ")
        response = request(query)
        result = response["choices"][0]["text"].replace("\n", "\n - ")
        print(f" - {result}")
        if query.endswith("!!"):
            break


if __name__ == "__main__":
    sys.exit(main())
