import subprocess
import json
import re

class StaticAnalyzer:
    def __init__(self):
        # Maps tool to specific regex for error parsing
        self.error_patterns = {
            "mypy": r"error: .*",
            "pylint": r"([A-Z]\d{4}): (.*)"
        }

    def run_mypy(self, file_path: str) -> dict:
        """Runs mypy and counts type errors."""
        result = subprocess.run(["mypy", file_path, "--strict"], capture_output=True, text=True)
        errors = re.findall(self.error_patterns["mypy"], result.stdout)
        return {
            "file": file_path,
            "error_count": len(errors),
            "raw_output": result.stdout,
            "passed": result.returncode == 0
        }

    def run_pylint(self, file_path: str) -> dict:
        """Runs pylint and extracts the numerical score."""
        result = subprocess.run(["pylint", file_path], capture_output=True, text=True)
        score_match = re.search(r"Your code has been rated at (-?\d+\.\d+)/10", result.stdout)
        score = float(score_match.group(1)) if score_match else 0.0
        return {
            "file": file_path,
            "score": score,
            "passed": score > 8.0  # Threshold defined in agent_config
        }
