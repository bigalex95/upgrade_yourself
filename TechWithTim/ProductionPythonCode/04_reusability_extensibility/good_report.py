"""
GOOD: Extensible and reusable design using Strategy pattern
"""
from abc import ABC, abstractmethod
from typing import List, Dict


class ReportFormatter(ABC):
    """Abstract formatter - define the interface"""
    
    @abstractmethod
    def format(self, data: List[Dict]) -> str:
        """Format data into a report"""
        pass


class TextFormatter(ReportFormatter):
    """Reusable text formatter"""
    
    def format(self, data: List[Dict]) -> str:
        report = "===== REPORT =====\n"
        for item in data:
            report += f"- {item['name']}: ${item['value']}\n"
        report += "==================\n"
        return report


class CSVFormatter(ReportFormatter):
    """Reusable CSV formatter"""
    
    def format(self, data: List[Dict]) -> str:
        if not data:
            return ""
        
        # Extract headers from first item
        headers = data[0].keys()
        report = ",".join(headers) + "\n"
        
        for item in data:
            values = [str(item[h]) for h in headers]
            report += ",".join(values) + "\n"
        
        return report


class HTMLFormatter(ReportFormatter):
    """Reusable HTML formatter"""
    
    def format(self, data: List[Dict]) -> str:
        if not data:
            return "<html><body><p>No data</p></body></html>"
        
        headers = data[0].keys()
        
        report = "<html><body><table>\n"
        report += "<tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr>\n"
        
        for item in data:
            report += "<tr>"
            report += "".join(f"<td>{item[h]}</td>" for h in headers)
            report += "</tr>\n"
        
        report += "</table></body></html>\n"
        return report


# NEW FORMAT - No modification to existing code!
class JSONFormatter(ReportFormatter):
    """New formatter - added without touching existing code!"""
    
    def format(self, data: List[Dict]) -> str:
        import json
        return json.dumps(data, indent=2)


# NEW FORMAT - Markdown!
class MarkdownFormatter(ReportFormatter):
    """Another new formatter - still no changes to existing code!"""
    
    def format(self, data: List[Dict]) -> str:
        if not data:
            return "No data"
        
        headers = data[0].keys()
        
        # Header row
        report = "| " + " | ".join(headers) + " |\n"
        # Separator
        report += "| " + " | ".join("---" for _ in headers) + " |\n"
        # Data rows
        for item in data:
            report += "| " + " | ".join(str(item[h]) for h in headers) + " |\n"
        
        return report


class ReportGenerator:
    """Generator that works with any formatter - extensible!"""
    
    def __init__(self, formatter: ReportFormatter):
        self.formatter = formatter
    
    def generate(self, data: List[Dict]) -> str:
        """Generate report using the configured formatter"""
        return self.formatter.format(data)
    
    def set_formatter(self, formatter: ReportFormatter):
        """Change formatter at runtime"""
        self.formatter = formatter


if __name__ == "__main__":
    data = [
        {"name": "Product A", "value": 100},
        {"name": "Product B", "value": 200},
        {"name": "Product C", "value": 150},
    ]
    
    # Create generator with text formatter
    generator = ReportGenerator(TextFormatter())
    
    print("Text format:")
    print(generator.generate(data))
    
    # Switch to CSV - no code changes needed!
    print("\nCSV format:")
    generator.set_formatter(CSVFormatter())
    print(generator.generate(data))
    
    # Switch to HTML
    print("\nHTML format:")
    generator.set_formatter(HTMLFormatter())
    print(generator.generate(data))
    
    # NEW: JSON format - no modifications to existing classes!
    print("\nJSON format (NEW!):")
    generator.set_formatter(JSONFormatter())
    print(generator.generate(data))
    
    # NEW: Markdown format
    print("\nMarkdown format (NEW!):")
    generator.set_formatter(MarkdownFormatter())
    print(generator.generate(data))
    
    # Can even reuse formatters directly in other contexts
    print("\n[OK] Reusing CSV formatter elsewhere:")
    csv_formatter = CSVFormatter()
    other_data = [{"id": 1, "status": "active"}, {"id": 2, "status": "inactive"}]
    print(csv_formatter.format(other_data))
    
    print("\n[OK] BENEFITS:")
    print("- Add new formats WITHOUT modifying existing code")
    print("- Each formatter is reusable in any context")
    print("- Can swap formatters at runtime")
    print("- Easy to test each formatter independently")
    print("- Open for extension, closed for modification")
    print("- No if/else chains or coupling")

