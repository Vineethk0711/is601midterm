from calculator.main import Calculator
from calculator.plugins import square
import calculator.plugins.sqrt as sqrt_plugin
import calculator.plugins.power as power_plugin
import calculator.plugins.log as log_plugin

def test_sqrt():
    assert sqrt_plugin.run(16) == 4

def test_power():
    assert power_plugin.run(2, 3) == 8

def test_log():
    assert log_plugin.run(100, 10) == 2

def test_square():
    assert square.run(4) == 16

def test_plugin_loading_error():
    calculator = Calculator()
    result = calculator.execute_plugin("non_existent_plugin", 5)
    assert result is None, "Expected None for non-existent plugin"