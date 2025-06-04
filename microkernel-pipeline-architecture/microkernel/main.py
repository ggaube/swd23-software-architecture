

# main.py

from core import TextProcessor
from plugins import UppercasePlugin, ReversePlugin

# Create the central processing engine (microkernel)
processor = TextProcessor()

# Register plugins in a specific order:
# First, text is converted to uppercase, then it's reversed
processor.register_plugin(UppercasePlugin())
processor.register_plugin(ReversePlugin())

# Define the input text
input_text = "Hello SWD23"

# Execute the plugin chain on the input text
output_text = processor.run(input_text)

# Print the original and final results
print("Input:", input_text)
print("Output:", output_text)


