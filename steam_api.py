from flask import Flask, request, jsonify
from iapws import IAPWS97

app = Flask(__name__)

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
    app.run()


