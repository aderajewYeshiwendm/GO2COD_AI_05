def correct_errors(expression):
    """
    Correct common mistakes in the expression, like extra operators.
    """
    # Example: Replace consecutive operators like "++" with "+"
    return expression.replace("++", "+").replace("**", "*")

def predict_next(expression):
    """
    Predict the next calculation based on input history.
    """
    if "+" in expression:
        return "Maybe you want to subtract next?"
    elif "*" in expression:
        return "How about division next?"
    else:
        return "Keep calculating!"
