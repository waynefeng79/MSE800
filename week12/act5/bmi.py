from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Set default values for the initial page load
    bmi = "0.0"
    category = "--"
    error = None

    if request.method == 'POST':
        try:
            weight_input = request.form.get('weight', '')
            height_input = request.form.get('height', '')

            if not weight_input or not height_input:
                error = "Please fill in both fields."
            else:
                weight = float(weight_input)
                height = float(height_input)

                if weight <= 0 or height <= 0:
                    error = "Values must be greater than zero."
                else:
                    calculated_bmi = weight / (height ** 2)
                    bmi = f"{calculated_bmi:.1f}"

                    if calculated_bmi < 18.5:
                        category = "Underweight"
                    elif 18.5 <= calculated_bmi < 25:
                        category = "Normal weight"
                    elif 25 <= calculated_bmi < 30:
                        category = "Overweight"
                    else:
                        category = "Obese"
        except ValueError:
            error = "Please enter valid numbers."

    return render_template('index.html', bmi=bmi, category=category, error=error)

if __name__ == '__main__':
    app.run(debug=True)