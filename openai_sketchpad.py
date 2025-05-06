import argparse
from openai import OpenAI

"""
This script sends a question to OpenAI's GPT-4.1-nano model
and prints the response.

Usage:
    python openai_sketchpad.py --question "What is the capital of France?"
"""

def main():
    parser = argparse.ArgumentParser(
        description=(
            "Send a question to OpenAI GPT-4.1-nano and "
            "print the response."
        )
    )
    parser.add_argument(
        "--question",
        help="The question or prompt to send to the model")
    args = parser.parse_args()

    client = OpenAI()

    response = client.responses.create(
        model="gpt-4.1-nano",
        input=args.question
    )

    print(response.output_text)


if __name__ == "__main__":
    main()
