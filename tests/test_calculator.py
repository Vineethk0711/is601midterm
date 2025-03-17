# tests/test_calculator.py

import pytest
import os
import pandas as pd
from calculator.main import Calculator
from unittest.mock import patch

@pytest.fixture
def calculator():
    return Calculator()

# Test basic operations
def test_add(calculator):
    assert calculator.add(3, 2) == 5

def test_subtract(calculator):
    assert calculator.subtract(3, 2) == 1

def test_multiply(calculator):
    assert calculator.multiply(3, 2) == 6

def test_divide(calculator):
    assert calculator.divide(6, 2) == 3

def test_divide_large_numbers(calculator):
    result = calculator.divide(1e10, 2)
    assert result == 5e9

def test_divide_small_numbers(calculator):
    result = calculator.divide(1e-10, 2)
    assert result == 5e-11

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(6, 0)

# Test saving history
def test_save_history(calculator, tmpdir):
    test_file = os.path.join(tmpdir, 'test_history.csv')
    calculator.add(1, 2)  # Sample operation
    calculator.save_history(test_file)
    
    assert os.path.exists(test_file)
    
    history_data = pd.read_csv(test_file)
    assert len(history_data) == 1
    assert history_data.iloc[0]["operation"] == "add"

# Test loading history
def test_load_history(calculator, tmpdir):
    test_file = os.path.join(tmpdir, 'test_history.csv')
    sample_data = pd.DataFrame([{"operation": "subtract", "operand1": 5, "operand2": 2, "result": 3}])
    sample_data.to_csv(test_file, index=False)
    calculator.load_history(test_file)
    
    assert len(calculator.history) == 1
    assert calculator.history.iloc[0]["operation"] == "subtract"

# Test clearing history
def test_clear_history(calculator):
    calculator.add(1, 2)
    calculator.clear_history()
    
    assert calculator.history.empty

# Test plugin loading
def test_load_plugins(calculator):
    calculator.load_plugins()
    assert "sqrt" in calculator.plugins
    assert "power" in calculator.plugins
    assert "log" in calculator.plugins

# Test executing a valid plugin
def test_execute_plugin_success(calculator):
    result = calculator.execute_plugin("sqrt", 16)
    assert result == 4

# Test executing a nonexistent plugin
def test_execute_plugin_failure(calculator):
    result = calculator.execute_plugin("nonexistent", 2)
    assert result is None

# Test for handling invalid REPL command (simulated)
def test_invalid_command_in_repl(calculator, capfd):
    calculator.add(3, 5)
    calculator.clear_history()
    assert calculator.history.empty

def test_show_history(calculator, capsys):
    calculator.add(1, 2)
    calculator.show_history()
    captured = capsys.readouterr()
    assert "add" in captured.out
    assert "1" in captured.out  # Check operand 1
    assert "2" in captured.out  # Check operand 2
    assert "3" in captured.out  # Check result

def test_invalid_plugin_missing_run(calculator):
    calculator.plugins['invalid_plugin'] = object()
    result = calculator.execute_plugin('invalid_plugin', 5)
    assert result is None 

def test_repl_exit():
    pass
