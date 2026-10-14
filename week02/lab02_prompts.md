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

It lowercased each character inside the loop rather than converting the whole string once. It returned four lines with no explanation, no worked examples, no mention of what it assumed.


### Antigravity CLI observations

    def count_vowels(text: str) -> int:
        """Count a, e, i, o, and u without regard to case; do not count y."""
        vowels = set("aeiou")
        return sum(1 for char in text.lower() if char in vowels)

It converted the entire string to lowercase before counting vowels, rather than lowercasing each character individually. It used a set to check for vowels and included a clear description of what the function does. It also provided an explanation and worked examples, making the code easier to understand.

### Comparison

Antigravity read test_lab02.py and the existing lab02.py before answering, while Copilot did not. Both responses provided correct solutions to the prompt. Antigravity explained the code better and included examples, while Copilot kept the code shorter and simpler. Copilot’s description did not mention that y should not be counted, even though its code handled it correctly. I chose Antigravity’s answer because it was easier to understand and explained how the function worked. Testing both versions under the same conditions matters because it helps determine whether each solution meets the requirements and makes the comparison fairer and more reliable.

## Test-guided implementation

The nine Python tests passed on the first run using Antigravity’s code. However, the journal tests failed because the required sections did not fully meet the assignment rules. The tests first flagged placeholder markers that had not been replaced, then a missing code fence around the code, and later word counts that were too short in individual sections. I used each failure to identify what needed fixing and revised the journal accordingly. I also learned that git diff does not show untracked files, which explained why it showed nothing before the first commit. These checks made sure they were working properly.

## Preferred tool combination

A browser chat is useful for explanations. Copilot CLI is helpful for working in the terminal. Antigravity can inspect files and provide more detailed explanations. I currently prefer using a browser chat for simple tasks and a CLI tool for working with project files. But my favorite method is using a tool in VS Code so it can edit the code dirrectly like GitHub Copilot or Claude. I have been using Claude for my previous projects in VS Code, and I like how it helps me write, debug, and improve my code without constantly switching between applications. Makes it a lot cleaner.