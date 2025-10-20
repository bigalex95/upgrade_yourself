"""
BAD: Not portable - tied to specific platform and environment
"""
import os


class DataProcessor:
    """Not portable - hard-coded Windows paths and assumptions"""
    
    def __init__(self):
        # Hard-coded Windows path!
        self.input_dir = "C:\\Users\\John\\Documents\\data"
        self.output_dir = "C:\\Users\\John\\Documents\\output"
        
        # Hard-coded database connection
        self.db_host = "localhost"
        self.db_port = 5432
        
        # Hard-coded API endpoint
        self.api_url = "http://localhost:8000/api"
    
    def process_file(self, filename: str):
        # Building path with hard-coded separator
        input_path = self.input_dir + "\\" + filename
        output_path = self.output_dir + "\\" + filename.replace(".txt", ".csv")
        
        print(f"Processing: {input_path}")
        print(f"Output to: {output_path}")
        
        # Simulate processing
        print("Connecting to database at localhost:5432...")
        print("Calling API at http://localhost:8000/api...")
        
        return output_path


if __name__ == "__main__":
    processor = DataProcessor()
    
    try:
        processor.process_file("sample.txt")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n[X] PROBLEMS:")
    print("- Hard-coded Windows paths (C:\\ drive)")
    print("- Won't work on Linux/Mac")
    print("- Can't run in different environments (dev/staging/prod)")
    print("- Can't test with different configurations")
    print("- Username 'John' hard-coded!")
    print("- Database and API endpoints hard-coded")
    print("- Path separator hard-coded (\\)")

