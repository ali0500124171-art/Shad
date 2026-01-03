from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def health_check():
    """Health check endpoint for Render"""
    return jsonify({
        "status": "Bot is running",
        "timestamp": datetime.now().isoformat(),
        "service": "R3D Bot - Telegram Bot Service"
    }), 200

@app.route('/api/status', methods=['GET'])
def bot_status():
    """Get bot status"""
    return jsonify({
        "bot_running": True,
        "mode": "polling",
        "version": "1.0.0"
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
