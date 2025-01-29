from flask import Flask, request, jsonify
from iapws import IAPWS97

app = Flask(__name__)
HOME_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Steam Enthalpy API</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin: 50px; }
        h1 { color: #333; }
        p { color: #666; }
        .container { max-width: 600px; margin: auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to the Steam Enthalpy API</h1>
        <p>Use this API to calculate steam enthalpy based on pressure and temperature.</p>
        <p>Endpoint: <strong>/steam-enthalpy?pressure=&lt;MPa&gt;&temperature=&lt;Celsius&gt;</strong></p>
        <p>Example: <strong>/steam-enthalpy?pressure=1.0&temperature=200</strong></p>
    </div>
</body>
</html>
"""
@app.route('/')
def home():
    return render_template_string(HOME_PAGE)

@app.route('/steam-enthalpy', methods=['GET'])
def get_steam_enthalpy():

    try:
        pressure = float(request.args.get('pressure'))  # Pressure in MPa
        temperature = float(request.args.get('temperature'))  # Temperature in Celsius
        
        # Create an IAPWS97 steam state
        steam = IAPWS97(P=pressure, T=temperature + 273.15)  # Convert Celsius to Kelvin
        
        enthalpy = steam.h  # Enthalpy in kJ/kg
        
        return jsonify({"pressure": pressure, "temperature": temperature, "enthalpy": enthalpy})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)


