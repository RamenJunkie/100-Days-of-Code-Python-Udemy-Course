class Post:

    def __init__(self, payload):
        self.id = payload["id"]
        self.body = payload["body"]
        self.title = payload["title"]
        self.subtitle = payload["subtitle"]
