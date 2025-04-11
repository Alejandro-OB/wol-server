from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return "🌐 Wake-on-LAN Server activo. Usa /wake para encender tu PC."

@app.route("/wake")
def wake():
    mac = os.environ.get("MAC_ADDR")
    port = os.environ.get("WOL_PORT", "9000")

    if not mac:
        return "❌ MAC_ADDR no está definida en las variables de entorno."

    try:
        subprocess.run(
            ["wakeonlan", "-i", "127.0.0.1", "-p", port, mac],
            check=True
        )
        return f"✅ Paquete mágico enviado a {mac} en el puerto {port}."
    except subprocess.CalledProcessError as e:
        return f"❌ Error al enviar el paquete mágico: {e}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway asigna este puerto
    app.run(host="0.0.0.0", port=port)
