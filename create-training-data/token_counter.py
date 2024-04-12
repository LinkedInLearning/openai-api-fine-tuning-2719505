import numpy as np
import tiktoken

# Initialize the TikToken encoding
encoding = tiktoken.get_encoding("cl100k_base")


def num_tokens_from_messages(messages, tokens_per_message=3, tokens_per_name=1):
    """Calculate the total number of tokens for given messages."""
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3
    return num_tokens

def num_assistant_tokens_from_messages(messages):
    """Calculate the number of tokens for messages where the role is 'assistant'."""
    num_tokens = 0
    for message in messages:
        if message["role"] == "assistant":
            num_tokens += len(encoding.encode(message["content"]))
    return num_tokens

def print_distribution(values, name):
    """Print statistical distribution metrics of the given values."""
    print(f"\n#### Distribution of {name}:")
    print(f"min / max: {min(values)}, {max(values)}")
    print(f"mean / median: {np.mean(values)}, {np.median(values)}")
    print(f"p5 / p95: {np.quantile(values, 0.05)}, {np.quantile(values, 0.95)}")

