# Lab 02 CLI comparison journal

Do not include passwords, tokens, API keys, or complete authentication output.

## Tool check

### GitHub Copilot CLI

It is installed. Authenticated through GitHub with /login, version 1.0.83.

### Antigravity CLI

It is installed. Authenticated with Google OAuth. Version 1.2.2.

## Shared task

### Shared prompt
```text
Please provide me with a python  function count_vowels. It should take an inputed string and count  a, e, i, o, and u without regard to case; do not count y.
```
### Copilot CLI observations

def count_vowels(text: str) -> int:
    """Count the letters a, e, i, o, and u in text, ignoring case."""
    return sum(char.lower() in "aeiou" for char in text)

It lowercased each character inside the loop rather than converting the whole string once


### Antigravity CLI observations

    def count_vowels(text: str) -> int:
        """Count a, e, i, o, and u without regard to case; do not count y."""
        vowels = set("aeiou")
        return sum(1 for char in text.lower() if char in vowels)


### Comparison

Both Antigravity and Copilot gave correct answers. Antigravity explained the code better and gave examples, while Copilot kept the code shorter and simpler. Copilot’s description did not mention that y should not be counted. Both solutions work well. I ended up using Antigravities anwser.

## Test-guided implementation

I checked that the function counts a, e, i, o, and u correctly, including uppercase letters. Both versions passed these checks. I kept the code simple and kept the description clearly explaining what the function does. The final code follows the instructions and returns the correct number of vowels in a string. 

## Preferred tool combination

A browser chat is useful for explanations. Copilot CLI is helpful for working in the terminal. Antigravity can inspect files and provide more detailed explanations. I currently prefer using a browser chat for simple tasks and a CLI tool for working with project files. But my favorite method is using a tool in VS Code so it can edit the code dirrectly like GitHub Copilot or Claude. I have been using cluade for my previous projects in VS Code. 