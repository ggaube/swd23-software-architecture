
# stages.py — Processing Stages (Plugin/Extension Layer)

import string
from pipeline import Stage

# Stage 1: Converts text to lowercase
class LowerCaseStage(Stage):
    def process(self, data):
        """
        Transform the input text to lowercase.
        Example: "Hello" → "hello"
        """
        return data.lower()

# Stage 2: Removes punctuation characters from the text
class RemovePunctuationStage(Stage):
    def process(self, data):
        """
        Strip punctuation from the input string using str.translate().
        Example: "hello!" → "hello"
        """
        return data.translate(str.maketrans('', '', string.punctuation))

# Stage 3: Splits the string into a list of words
class TokenizeStage(Stage):
    def process(self, data):
        """
        Tokenize the text by splitting on whitespace.
        Example: "hello world" → ["hello", "world"]
        """
        return data.split()
