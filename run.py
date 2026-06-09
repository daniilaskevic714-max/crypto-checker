from app import app

if __name__ == "__main__":
    # WARNING: for production use nginx/traefik, this is dev SSL only
    app.run(
        host="0.0.0.0",
        port=5000,
        ssl_context="adhoc"
    )