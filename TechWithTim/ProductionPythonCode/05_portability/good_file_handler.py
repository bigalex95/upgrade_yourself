"""
GOOD: Portable across platforms and environments
"""
import os
from pathlib import Path
from typing import Optional


class Config:
    """Configuration abstraction - can load from env, file, etc."""
    
    def __init__(self):
        # Use environment variables with sensible defaults
        self.input_dir = Path(os.getenv("INPUT_DIR", "./data"))
        self.output_dir = Path(os.getenv("OUTPUT_DIR", "./output"))
        
        self.db_host = os.getenv("DB_HOST", "localhost")
        self.db_port = int(os.getenv("DB_PORT", "5432"))
        
        self.api_url = os.getenv("API_URL", "http://localhost:8000/api")
        
        # Ensure directories exist
        self.input_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    @classmethod
    def from_file(cls, config_path: str):
        """Load configuration from file"""
        # Could load from JSON, YAML, INI, etc.
        # For demo, just showing the pattern
        config = cls()
        print(f"(Could load config from {config_path})")
        return config


class DataProcessor:
    """Portable - works on any platform"""
    
    def __init__(self, config: Optional[Config] = None):
        self.config = config or Config()
    
    def process_file(self, filename: str) -> Path:
        # Cross-platform path handling with pathlib
        input_path = self.config.input_dir / filename
        
        # Platform-independent path manipulation
        output_filename = Path(filename).stem + ".csv"
        output_path = self.config.output_dir / output_filename
        
        print(f"Processing: {input_path}")
        print(f"Output to: {output_path}")
        
        # Simulate processing
        print(f"Connecting to database at {self.config.db_host}:{self.config.db_port}...")
        print(f"Calling API at {self.config.api_url}...")
        
        return output_path


def demonstrate_portability():
    """Show how it works in different scenarios"""
    
    print("=== Scenario 1: Default configuration ===")
    processor = DataProcessor()
    processor.process_file("sample.txt")
    
    print("\n=== Scenario 2: Custom environment (e.g., Production) ===")
    # Simulate setting environment variables
    os.environ["INPUT_DIR"] = "/var/app/data"
    os.environ["OUTPUT_DIR"] = "/var/app/output"
    os.environ["DB_HOST"] = "prod-db.example.com"
    os.environ["DB_PORT"] = "5432"
    os.environ["API_URL"] = "https://api.example.com/v1"
    
    prod_config = Config()
    prod_processor = DataProcessor(prod_config)
    prod_processor.process_file("sample.txt")
    
    # Clean up env vars
    for key in ["INPUT_DIR", "OUTPUT_DIR", "DB_HOST", "DB_PORT", "API_URL"]:
        os.environ.pop(key, None)
    
    print("\n=== Scenario 3: Platform-independent paths ===")
    print(f"Current OS: {os.name}")
    print(f"Path separator: {os.sep}")
    
    # pathlib handles this automatically!
    demo_path = Path("data") / "subfolder" / "file.txt"
    print(f"Cross-platform path: {demo_path}")
    print(f"Absolute path: {demo_path.absolute()}")
    
    # Works the same on Windows, Linux, Mac!


if __name__ == "__main__":
    demonstrate_portability()
    
    print("\n[OK] BENEFITS:")
    print("- Works on Windows, Linux, and Mac without changes")
    print("- Environment-specific config via env vars")
    print("- No hard-coded paths or servers")
    print("- Easy to test with different configurations")
    print("- pathlib provides cross-platform path handling")
    print("- Can deploy to any environment (dev/staging/prod)")

