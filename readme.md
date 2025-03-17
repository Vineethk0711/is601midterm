# **IS601_Midterm_24: Advanced Python Calculator**  

## **Project Overview**  
This project is an advanced Python-based calculator developed for the IS601 midterm. It features essential arithmetic operations, history management, and a dynamic plugin system, all accessible through a command-line REPL interface.  

## **Calculator Features**  
- **Basic Operations**: Addition, subtraction, multiplication, and division.  
- **History Management**: Stores calculation history using Pandas, with options to load, save, and clear history.  
- **Plugin System**: Supports dynamically loading custom math functions without modifying core code.  
- **Modular Command System**: Operations such as addition and subtraction are structured as modular commands.  

## **Project Structure**  
- `calculator/` – Core functionality and REPL interface.  
- `commands/` – Additional operations implemented as plugins.  
- `tests/` – Unit tests for the calculator and its plugins.  
- `data/` – Stores calculation history in CSV format.  

## **Installation**  
1. Clone the repository.  
2. Install dependencies:  
   ```sh
   pip install -r requirements.txt
   ```  
3. Run the calculator using the REPL interface:  
   ```sh
   python calculator/main.py
   ```  

## **Usage Example**  
- Perform calculations using commands like:  
  ```sh
  3 + 5
  ```  
- Use plugins for extended operations:  
  ```sh
  sqrt 16
  ```  
- Manage history with commands: `save`, `load`, `history`, `clear`.  

## **Running Tests & Coverage Report**  
- Execute unit tests:  
  ```sh
  pytest
  ```  
- Generate a test coverage report:  
  ```sh
  pytest --cov=calculator
  ```  

## **Design Patterns Used**  
- **Facade Pattern**: Simplifies Pandas-based history management.  
- **Command Pattern**: Provides a structured approach for REPL commands.  
- **Plugin Pattern**: Enables easy extension of functionalities via dynamic loading.  

## **Environment Variables**  
Configuration settings, including logging levels, are managed through environment variables in a `.env` file:  
- **LOG_LEVEL** – Controls log verbosity (e.g., `LOG_LEVEL=INFO`).  
https://github.com/Vineethk0711/is601midterm/blob/605d91d7509640c68f4da2344ec7246bf5555bdd/calculator/main.py#L9

## **Logging System**  
Logging is dynamically configured based on environment variables. It records important informational messages and error handling details for debugging.  
    https://github.com/Vineethk0711/is601midterm/blob/605d91d7509640c68f4da2344ec7246bf5555bdd/calculator/main.py#L36

## **Error Handling**  
This project follows two key error-handling strategies:  
- **Look Before You Leap (LBYL)**: Checks conditions like file existence before performing operations.  
- **Easier to Ask for Forgiveness than Permission (EAFP)**: Uses `try/except` blocks to handle errors in plugin loading.
https://github.com/Vineethk0711/is601midterm/blob/605d91d7509640c68f4da2344ec7246bf5555bdd/calculator/main.py#L65  

## **Video Demonstration**  
A video walkthrough showcasing the calculator’s functionality, REPL interface, and key features is available here:  
[Video Link]https://drive.google.com/file/d/188CsmvZbcARXd7b9kWhdSFt6A6OejzBJ/view?usp=sharing)  
