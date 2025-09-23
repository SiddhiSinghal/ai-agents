# agents/auth_agent.py
class AuthAgent:
    def __init__(self):
        self.users = {}  # in-memory storage {email: password}

    def run(self, data):
        action = data.get("action")
        email = data.get("email")
        password = data.get("password")

        if action == "signup":
            self.users[email] = password
            return f"✅ User {email} signed up!"
        elif action == "login":
            if self.users.get(email) == password:
                return f"🔑 Login successful for {email}"
            return "❌ Invalid credentials"
        else:
            return "⚠️ Unknown auth action"
