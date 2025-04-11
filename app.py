from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route("/wake")
def wake():
    mac = os.environ.get("MAC_ADDR")
    port = os.environ.get("WOL_PORT", "9000")
    try:
        subprocess.run(["wakeonlan", "-i", "127.0.0.1", "-p", port, mac], check=True)
        return "Magic packet sent!"
    except subprocess.CalledProcessError:
        return "Failed to send magic packet."
