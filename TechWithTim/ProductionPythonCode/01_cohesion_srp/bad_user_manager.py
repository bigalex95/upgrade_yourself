"""
BAD: Violates SRP - One class doing too many unrelated things
"""
import re
import smtplib


class UserManager:
    """This class does EVERYTHING - validation, DB, email, reporting"""
    
    def __init__(self):
        self.users = {}
    
    def create_user(self, email, password, name):
        # Validation logic
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email")
        if len(password) < 8:
            raise ValueError("Password too short")
        
        # Database logic
        user_id = len(self.users) + 1
        self.users[user_id] = {
            'email': email,
            'password': password,
            'name': name
        }
        
        # Email sending logic
        self._send_welcome_email(email, name)
        
        # Reporting logic
        self._log_user_creation(user_id, email)
        
        return user_id
    
    def _send_welcome_email(self, email, name):
        """Email sending mixed with user management"""
        print(f"Sending email to {email}...")
        # Imagine SMTP code here
        print(f"Welcome {name}!")
    
    def _log_user_creation(self, user_id, email):
        """Reporting mixed with user management"""
        print(f"LOG: User {user_id} created with email {email}")
    
    def generate_user_report(self):
        """Even more unrelated responsibility!"""
        report = f"Total users: {len(self.users)}\n"
        for uid, user in self.users.items():
            report += f"  {uid}: {user['email']}\n"
        return report


if __name__ == "__main__":
    # Problem: Hard to test just validation, or swap email provider, or change DB
    manager = UserManager()
    
    user_id = manager.create_user("alice@example.com", "password123", "Alice")
    print(f"Created user: {user_id}")
    
    print("\n" + manager.generate_user_report())
    
    print("\n[X] PROBLEMS:")
    print("- Can't test validation without triggering emails")
    print("- Can't change database without touching email code")
    print("- Can't reuse email sender for other purposes")
    print("- 4+ reasons for this class to change!")

