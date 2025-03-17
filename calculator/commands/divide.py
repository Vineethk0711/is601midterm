def run(a, b):
    if float(b) == 0:
        raise ValueError("Cannot divide by zero")
    return float(a) / float(b)
