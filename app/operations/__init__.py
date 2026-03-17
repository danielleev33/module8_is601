from typing import Union
import logging

Number = Union[int, float]

logger = logging.getLogger(__name__)

def add(a: Number, b: Number) -> Number:
    logger.info("Adding %s and %s", a, b)
    result = a + b
    logger.info("Addition result: %s", result)
    return result

def subtract(a: Number, b: Number) -> Number:
    logger.info("Subtracting %s from %s", b, a)
    result = a - b
    logger.info("Subtraction result: %s", result)
    return result

def multiply(a: Number, b: Number) -> Number:
    logger.info("Multiplying %s and %s", a, b)
    result = a * b
    logger.info("Multiplication result: %s", result)
    return result

def divide(a: Number, b: Number) -> float:
    logger.info("Dividing %s by %s", a, b)
    if b == 0:
        logger.error("Division by zero attempted: a=%s, b=%s", a, b)
        raise ValueError("Cannot divide by zero!")
    result = a / b
    logger.info("Division result: %s", result)
    return result
