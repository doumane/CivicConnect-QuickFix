# CivicConnect QuickFix - Backend Data Processor

reports = [
    {"id": 1, "title": "Pothole on Main Street", "category": "Roads and Pavements", "priority": "High"},
    {"id": 2, "title": "Broken lamp post in Sector 4", "category": "Street Lighting", "priority": "Medium"},
    {"id": 3, "title": "Overflowing bins near the park", "category": "Sanitation & Waste", "priority": "High"}
]

def analyze_reports():
    print("--- Community Reports Analysis Report ---")
    total = len(reports)
    print(f"Total incoming reports: {total}")
    
    high_priority = [r for r in reports if r['priority'] == 'High']
    print(f"High-priority reports requiring urgent action: {len(high_priority)}")
    
    for r in high_priority:
        print(f"- [URGENT] {r['title']} (Category: {r['category']})")

if __name__ == "__main__":
    analyze_reports()
