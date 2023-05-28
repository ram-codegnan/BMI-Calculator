from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    weight_values = map(float, request.form.get('weights').split())
    height_values = map(float, request.form.get('heights').split())

    def bmi(weight, height):
        return weight / (height ** 2)

    def classify_bmi(bmi_value):
        if bmi_value >= 30:
            return "Obese"
        elif bmi_value >= 25:
            return "Overweight"
        elif bmi_value >= 18.5:
            return "Normal"
        else:
            return "Underweight"

    bmi_categories = map(classify_bmi, (bmi(w, h) for w, h in zip(weight_values, height_values) if w > 0 and h > 0))

    return render_template('result.html', bmi_categories=list(bmi_categories))

if __name__ == '__main__':
    app.run()
