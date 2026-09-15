def calculate(a: float, b: float, multiplier: float = 1.0) -> float:
    """Add two numbers, then scale the result by a multiplier.

    This stands in for 'the pipeline's job' - in a real project this
    would be your actual transformation logic.
    """
    return (a + b) * multiplier
