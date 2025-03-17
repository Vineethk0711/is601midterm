import os
import logging
import importlib
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)

class Calculator:
    def __init__(self):
        self.history = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])
        self.plugins = {}
        self.load_plugins()

    def add(self, a, b):
        result = a + b
        self._save_history("add", a, b, result)
        return result

    def subtract(self, a, b):
        result = a - b
        self._save_history("subtract", a, b, result)
        return result

    def multiply(self, a, b):
        result = a * b
        self._save_history("multiply", a, b, result)
        return result

    def divide(self, a, b):
        if b == 0:
            logger.error("Division by zero error")
            raise ValueError("Cannot divide by zero")
        result = a / b
        self._save_history("divide", a, b, result)
        return result

    def _save_history(self, operation, a, b, result):
        new_record = {"operation": operation, "operand1": a, "operand2": b, "result": result}
        self.history = pd.concat([self.history, pd.DataFrame([new_record])], ignore_index=True)

    def save_history(self, file_name="history.csv"):
        self.history.to_csv(file_name, index=False)
        logger.info(f"History saved to {file_name}")

    def load_history(self, file_name="history.csv"):
        self.history = pd.read_csv(file_name)
        logger.info(f"History loaded from {file_name}")

    def clear_history(self):
        self.history = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])
        logger.info("History cleared")

    def show_history(self):
        print(self.history)
    def load_plugins(self):
        plugin_folder = 'calculator/plugins'
        for filename in os.listdir(plugin_folder):
            if filename.endswith('.py') and filename != '__init__.py':
                plugin_name = filename[:-3]  # Strip off '.py'
                try:
                    module = importlib.import_module(f'calculator.plugins.{plugin_name}')
                    self.plugins[plugin_name] = module
                    logger.info(f"Loaded plugin: {plugin_name}")
                except Exception as e:
                    logger.error(f"Failed to load plugin {plugin_name}: {e}")

    def execute_plugin(self, plugin_name, *args):
        if plugin_name in self.plugins:
            try:
                result = self.plugins[plugin_name].run(*args)
                return result
            except AttributeError as e:
                logger.error(f"Plugin {plugin_name} missing 'run' function: {e}")
            except Exception as e:
                logger.error(f"Error in plugin {plugin_name}: {e}")
        else:
            logger.error(f"Plugin {plugin_name} not found")
        return None

if __name__ == "__main__":
    calculator = Calculator()
    calculator.repl()  # Start the REPL from the Calculator instance
