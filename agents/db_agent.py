# agents/db_agent.py
class DBAgent:
    def __init__(self):
        self.storage = {}

    def run(self, data):
        action = data.get("action")
        user_id = data.get("user_id")

        if action == "save":
            self.storage[user_id] = data.get("content")
            return f"💾 Saved for {user_id}"
        elif action == "get":
            return self.storage.get(user_id, "⚠️ No data found")
        else:
            return "⚠️ Unknown DB action"
