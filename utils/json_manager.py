import json
import os


class JSONManager:
    def __init__(self, filename: str):
        self.filepath = os.path.join("data", filename)

        if not os.path.exists(self.filepath):
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4, ensure_ascii=False)

    def read(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def write(self, data: list):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
