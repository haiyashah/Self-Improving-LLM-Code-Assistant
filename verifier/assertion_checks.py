import re

def check_no_debug_prints(file_content: str) -> bool:
    """Ensure no 'print()' statements remain in production code."""
    if re.search(r'print\(.*\)', file_content):
        return False
    return True

def check_coverage_threshold(pytest_output: str, threshold: float = 80.0) -> bool:
    """Parses pytest-cov output to ensure coverage is above threshold."""
    match = re.search(r'TOTAL\s+\d+\s+\d+\s+(\d+)%', pytest_output)
    if match:
        return float(match.group(1)) >= threshold
    return False

def verify_deterministic_rules(file_path: str) -> List[str]:
    """Runs a suite of deterministic checks on a file."""
    issues = []
    with open(file_path, 'r') as f:
        content = f.read()
        if not check_no_debug_prints(content):
            issues.append("Contains debug print statements.")
    return issues
