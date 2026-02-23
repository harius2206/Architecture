import json
import os

class SimpleDataContext:
    def __init__(self, file_path="architecture_data.json"):
        self.file_path = file_path
        self.architects = []
        self.buildings = []
        self.load()

    def create_testing_data(self):
        if not self.architects:
            self.architects = [
                {"id": 1, "name": "Zaha Hadid", "license_id": "UK-001"},
                {"id": 2, "name": "Renzo Piano", "license_id": "IT-099"}
            ]
            self.buildings = [
                {"id": 1, "title": "The Shard", "address": "London", "architect_id": 2, "area": 110000.0}
            ]

    def is_empty(self):
        """Перевіряє, чи порожні списки даних"""
        return len(self.architects) == 0 and len(self.buildings) == 0

    def save(self):
        data = {
            "architects": self.architects,
            "buildings": self.buildings
        }
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Дані збережено у {self.file_path}")

    def load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.architects = data.get("architects", [])
                self.buildings = data.get("buildings", [])