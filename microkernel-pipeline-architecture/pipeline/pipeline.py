
# pipeline.py — Core Pipeline Architecture (Framework)
# Abstract base class for all processing stages
class Stage:
    def process(self, data):
        """
        Each stage must implement this method to perform a transformation
        on the input data and return the result to the next stage.
        """
        raise NotImplementedError("Stage must implement the process method.")

# The Pipeline class defines the execution flow
class Pipeline:
    def __init__(self):
        # Initialize an empty list to store the pipeline stages
        self.stages = []

    def add_stage(self, stage):
        """
        Add a processing stage to the pipeline.
        Stages are executed in the order they are added.
        """
        self.stages.append(stage)

    def run(self, data):
        """
        Execute the pipeline on the input data.
        Each stage transforms the data and passes it to the next.
        """
        for stage in self.stages:
            data = stage.process(data)  # Pass output to the next stage
        return data
