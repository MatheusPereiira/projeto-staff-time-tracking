import json
import os


class JsonManager:
    def __init__(self, file_path: str):
        self.file_path = file_path

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4, ensure_ascii=False)

    def read(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def write(self, data):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
