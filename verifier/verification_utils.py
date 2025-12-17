import datetime
import json

def generate_verification_report(results_list: list, pr_id: str):
    """Saves a detailed summary of the agent's verification performance."""
    report = {
        "pr_id": pr_id,
        "timestamp": str(datetime.datetime.now()),
        "summary": {
            "total_steps": len(results_list),
            "passed": sum(1 for r in results_list if r['verified']),
            "failed": sum(1 for r in results_list if not r['verified'])
        },
        "details": results_list
    }
    
    filename = f"reports/verify_{pr_id}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(report, f, indent=4)
    print(f"✅ Report generated: {filename}")
