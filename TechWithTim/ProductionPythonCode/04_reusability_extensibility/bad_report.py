"""
BAD: Hard-coded, not reusable or extensible
"""


class ReportGenerator:
    """Monolithic report generator - hard to extend"""
    
    def generate_report(self, data: list, format_type: str):
        """Generate report - must modify this method to add new formats!"""
        
        if format_type == "text":
            # Text format logic
            report = "===== REPORT =====\n"
            for item in data:
                report += f"- {item['name']}: ${item['value']}\n"
            report += "==================\n"
            return report
        
        elif format_type == "csv":
            # CSV format logic
            report = "name,value\n"
            for item in data:
                report += f"{item['name']},{item['value']}\n"
            return report
        
        elif format_type == "html":
            # HTML format logic
            report = "<html><body><table>\n"
            report += "<tr><th>Name</th><th>Value</th></tr>\n"
            for item in data:
                report += f"<tr><td>{item['name']}</td><td>${item['value']}</td></tr>\n"
            report += "</table></body></html>\n"
            return report
        
        
        else:
            raise ValueError(f"Unknown format: {format_type}")
        
        # Want JSON format? Must modify this method!
        # Want XML format? Must modify this method!
        # Want Markdown format? Must modify this method!


if __name__ == "__main__":
    data = [
        {"name": "Product A", "value": 100},
        {"name": "Product B", "value": 200},
        {"name": "Product C", "value": 150},
    ]
    
    generator = ReportGenerator()
    
    print("Text format:")
    print(generator.generate_report(data, "text"))
    
    print("\nCSV format:")
    print(generator.generate_report(data, "csv"))
    
    print("\nHTML format:")
    print(generator.generate_report(data, "html"))
    
    print("\n[X] PROBLEMS:")
    print("- Must modify ReportGenerator to add new formats")
    print("- Violates Open/Closed Principle")
    print("- Can't reuse formatting logic elsewhere")
    print("- Can't combine or compose formatters")
    print("- Growing if/else chain")
    print("- All formats coupled in one class")

