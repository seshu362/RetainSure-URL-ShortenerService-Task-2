from flask import request, jsonify, redirect, abort
from app import create_app
from app.utils import generate_short_code, is_valid_url
from app.storage import URLStorage

app = create_app()
storage = URLStorage()

BASE_URL = "http://localhost:5000"  # Change if deployed somewhere else

@app.route("/")
def health_check():
    return jsonify({"status": "URL Shortener Service running"}), 200

@app.route("/api/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json(force=True)
    url = data.get("url")
    if not url:
        return jsonify({"error": "Missing URL in request body"}), 400

    if not is_valid_url(url):
        return jsonify({"error": "Invalid URL format"}), 400

    # Generate a unique short code
    for _ in range(5):  # Try max 5 times to avoid collisions
        code = generate_short_code()
        if not storage.exists(code):
            storage.add_url(code, url)
            short_url = f"{BASE_URL}/{code}"
            return jsonify({"short_code": code, "short_url": short_url}), 201

    return jsonify({"error": "Could not generate unique short code, try again"}), 500

@app.route("/<string:short_code>")
def redirect_url(short_code):
    entry = storage.get_url(short_code)
    if not entry:
        return jsonify({"error": "Short code not found"}), 404

    storage.increment_clicks(short_code)
    return redirect(entry["original_url"])

@app.route("/api/stats/<string:short_code>")
def url_stats(short_code):
    entry = storage.get_url(short_code)
    if not entry:
        return jsonify({"error": "Short code not found"}), 404

    return jsonify({
        "url": entry["original_url"],
        "clicks": entry["clicks"],
        "created_at": entry["created_at"].isoformat() + "Z"
    }), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
