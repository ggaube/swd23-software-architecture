
# main.py — Application Logic (Execution Layer)

from pipeline import Pipeline
from stages import LowerCaseStage, RemovePunctuationStage, TokenizeStage

# Create the pipeline instance
pipeline = Pipeline()

# Add processing stages in the desired order
pipeline.add_stage(LowerCaseStage())          # Step 1: Convert to lowercase
pipeline.add_stage(RemovePunctuationStage())  # Step 2: Remove punctuation
pipeline.add_stage(TokenizeStage())           # Step 3: Split into words

# Input text to be processed
text = "Hello, SWD23! Last lecture is near."

# Run the data through the pipeline
result = pipeline.run(text)

# Display the processed output
print("Processed Output:", result)

