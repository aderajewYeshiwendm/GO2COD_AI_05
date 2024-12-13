from flask import Flask, render_template, request
from ai import predict_next, correct_errors

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # Render the homepage
    return render_template("index.html", result=None, suggestion=None)

@app.route("/calculate", methods=["POST"])
def calculate():
    # Handle form submission
    result = None
    suggestion = None
    expression = request.form.get("expression", "")
    corrected_expression = correct_errors(expression)
    try:
        # Evaluate the corrected expression
        result = eval(corrected_expression)
        suggestion = predict_next(expression)
    except Exception as e:
        result = f"Error: {str(e)}"
    # Return the page with updated results
    return render_template("index.html", result=result, suggestion=suggestion)

if __name__ == "__main__":
    app.run(debug=True)
