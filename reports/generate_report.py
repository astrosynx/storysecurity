from datetime import datetime

def generate_report(name, metrics):
    with open("chaos_report.md", "w") as f:
        f.write(f"# Chaos Report\n\n")
        f.write(f"Scenario: {name}\n")
        f.write(f"Generated: {datetime.utcnow()} UTC\n\n")
        for k,v in metrics.items():
            f.write(f"- {k}: {v}\n")
