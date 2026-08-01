from flask import Flask, render_template, request
from converter import convert_length, convert_weight, convert_temperature, LENGTH_RATIOS, WEIGHT_RATIOS

app = Flask(__name__)

TEMPERATURE_UNITS = ['celsius', 'fahrenheit', 'kelvin']

def process_conversion_request(category: str, convert_func, available_units: list):
    result = None
    error = None
    
    val_input = request.form.get('value', '')
    from_unit = request.form.get('from_unit', available_units[0]).lower().strip()
    to_unit = request.form.get('to_unit', available_units[1 if len(available_units) > 1 else 0]).lower().strip()

    if request.method == 'POST':
        print("\n--- DEBUG START ---")
        print(f"Raw Input: '{val_input}' (Type: {type(val_input)})")
        print(f"From Unit: '{from_unit}'")
        print(f"To Unit:   '{to_unit}'")
        print("--------------------\n")
        # Step 1: Validate numeric float conversion separately
        try:
            clean_value = val_input.replace(',', '').strip()
            numeric_value = float(clean_value)
        except ValueError:
            error = "Please enter a valid numeric value (e.g., 1000 or 1000.5)."
            
        # Step 2: Execute conversion logic only if number input was valid
        if not error:
            try:
                calc_result = convert_func(numeric_value, from_unit, to_unit)
                result = round(calc_result, 6)
            except ValueError as ve:
                error = str(ve)  # Shows exact unit mismatch message from converters.py
            except Exception as e:
                error = f"An unexpected error occurred: {str(e)}"

    return {
        'category': category,
        'units': available_units,
        'value': val_input,
        'from_unit': from_unit,
        'to_unit': to_unit,
        'result': result,
        'error': error
    } 

@app.route('/')
@app.route('/length', methods=['GET', 'POST'])
def length():
    ctx = process_conversion_request('Length', convert_length, list(LENGTH_RATIOS.keys()))
    return render_template('length.html', **ctx)

@app.route('/weight', methods=['GET', 'POST'])
def weight():
    ctx = process_conversion_request('Weight', convert_weight, list(WEIGHT_RATIOS.keys()))
    return render_template('weight.html', **ctx)

@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    ctx = process_conversion_request('Temperature', convert_temperature, TEMPERATURE_UNITS)
    return render_template('temperature.html', **ctx)

if __name__ == '__main__':
    app.run(debug=True)