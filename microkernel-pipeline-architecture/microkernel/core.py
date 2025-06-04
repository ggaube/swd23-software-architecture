# Base class that defines the plugin interface
class Plugin:
    def process(self, text: str) -> str:
        """
        This method should be overridden by all plugins.
        It receives a string and returns a modified version of it.
        """
        raise NotImplementedError("Plugins must implement the 'process' method.")


# The core system that manages and runs plugins
class TextProcessor:
    def __init__(self):
        # Initialize an empty list to store plugin instances
        self.plugins = []

    def register_plugin(self, plugin: Plugin):
        """
        Register a plugin to be included in the processing pipeline.
        The plugin must be an instance of a subclass of Plugin.
        """
        self.plugins.append(plugin)

    def run(self, text: str) -> str:
        """
        Process the input text by sequentially applying all registered plugins.
        Each plugin transforms the text and passes it to the next.
        """
        for plugin in self.plugins:
            text = plugin.process(text)
        return text
