"""Minimal HTTP service for a Cloud Run deployment."""

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            body = {"status": "ok"}
        elif self.path == "/":
            body = {
                "service": "vectra3d-google-workspace",
                "message": "Cloud Run service is running. Workspace integration is not configured.",
            }
        else:
            self.send_error(404, "Not Found")
            return

        payload = json.dumps(body).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()
