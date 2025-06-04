
# plugin.py

from core import Plugin

# Plugin that converts the entire text to uppercase
class UppercasePlugin(Plugin):
    def process(self, text: str) -> str:
        """
        Converts all characters in the input text to uppercase.
        Example: "hello" -> "HELLO"
        """
        return text.upper()


# Plugin that reverses the entire text
class ReversePlugin(Plugin):
    def process(self, text: str) -> str:
        """
        Reverses the input string.
        Example: "hello" -> "olleh"
        """
        return text[::-1]
