class SessionManager:
    def __init__(self, session):
        self.session = session

    def create(self, key, value):
        self.session[key] = value
        self.session.modified = True

    def fetch(self, key: str) -> list:
        return self.session.get(key)
