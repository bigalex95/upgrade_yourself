"""
GOOD: Each class has a single, clear responsibility
"""
import re
from typing import Dict, Optional


class EmailValidator:
    """Single responsibility: Validate email addresses"""
    
    @staticmethod
    def validate(email: str) -> bool:
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))


class PasswordValidator:
    """Single responsibility: Validate passwords"""
    
    @staticmethod
    def validate(password: str, min_length: int = 8) -> bool:
        return len(password) >= min_length


class UserRepository:
    """Single responsibility: Store and retrieve users"""
    
    def __init__(self):
        self._users: Dict[int, dict] = {}
        self._next_id = 1
    
    def save(self, email: str, password: str, name: str) -> int:
        user_id = self._next_id
        self._users[user_id] = {
            'email': email,
            'password': password,
            'name': name
        }
        self._next_id += 1
        return user_id
    
    def get_all(self) -> Dict[int, dict]:
        return self._users.copy()


class EmailService:
    """Single responsibility: Send emails"""
    
    def send_welcome_email(self, email: str, name: str):
        print(f"[EMAIL] Sending welcome email to {email}")
        print(f"   Welcome aboard, {name}!")


class UserActivityLogger:
    """Single responsibility: Log user activities"""
    
    def log_creation(self, user_id: int, email: str):
        print(f"[LOG] User {user_id} created with email {email}")


class UserService:
    """Orchestrates user creation - delegates to specialized services"""
    
    def __init__(self, repository: UserRepository, 
                 email_service: EmailService,
                 logger: UserActivityLogger):
        self.repository = repository
        self.email_service = email_service
        self.logger = logger
    
    def create_user(self, email: str, password: str, name: str) -> int:
        # Validate
        if not EmailValidator.validate(email):
            raise ValueError("Invalid email")
        if not PasswordValidator.validate(password):
            raise ValueError("Password too short")
        
        # Save
        user_id = self.repository.save(email, password, name)
        
        # Notify
        self.email_service.send_welcome_email(email, name)
        self.logger.log_creation(user_id, email)
        
        return user_id


class UserReportGenerator:
    """Single responsibility: Generate user reports"""
    
    def __init__(self, repository: UserRepository):
        self.repository = repository
    
    def generate_summary(self) -> str:
        users = self.repository.get_all()
        report = f"Total users: {len(users)}\n"
        for uid, user in users.items():
            report += f"  {uid}: {user['email']}\n"
        return report


if __name__ == "__main__":
    # Setup - each component can be tested/replaced independently
    repository = UserRepository()
    email_service = EmailService()
    logger = UserActivityLogger()
    
    user_service = UserService(repository, email_service, logger)
    report_gen = UserReportGenerator(repository)
    
    # Use
    user_id = user_service.create_user("alice@example.com", "password123", "Alice")
    print(f"[OK] Created user: {user_id}\n")
    
    print(report_gen.generate_summary())
    
    print("\n[OK] BENEFITS:")
    print("- Each class has ONE reason to change")
    print("- Easy to test validators independently")
    print("- Can swap email service without touching other code")
    print("- Can reuse components in other contexts")

