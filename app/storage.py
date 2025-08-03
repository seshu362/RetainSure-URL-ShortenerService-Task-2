import threading
from datetime import datetime

class URLStorage:
    def __init__(self):
        self._lock = threading.Lock()
        self._store = {}  # short_code -> {original_url, created_at, clicks}

    def add_url(self, short_code, original_url):
        with self._lock:
            self._store[short_code] = {
                "original_url": original_url,
                "created_at": datetime.utcnow(),
                "clicks": 0,
            }

    def get_url(self, short_code):
        with self._lock:
            return self._store.get(short_code)

    def increment_clicks(self, short_code):
        with self._lock:
            if short_code in self._store:
                self._store[short_code]["clicks"] += 1

    def exists(self, short_code):
        with self._lock:
            return short_code in self._store
