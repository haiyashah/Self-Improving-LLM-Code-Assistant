import subprocess
from typing import List, Dict

class ToolInterface:
    def __init__(self):
        self.available_tools = {
            "pytest": ["pytest", "--tb=short"],
            "mypy": ["mypy", "--ignore-missing-imports"],
            "pylint": ["pylint", "--disable=C0114,C0116"] # Disable docstring warnings
        }

    def execute(self, tool_name: str, files: List[str]) -> Dict:
        """Runs the specified tool on files and returns a standardized result."""
        if tool_name not in self.available_tools:
            return {"status": "ERROR", "output": f"Tool {tool_name} not supported"}

        base_cmd = self.available_tools[tool_name]
        results = {}

        for file in files:
            full_cmd = base_cmd + [file]
            try:
                process = subprocess.run(full_cmd, capture_output=True, text=True, timeout=30)
                results[file] = {
                    "tool": tool_name,
                    "exit_code": process.returncode,
                    "output": process.stdout if process.returncode == 0 else process.stderr,
                    "status": "SUCCESS" if process.returncode == 0 else "FAILED"
                }
            except subprocess.TimeoutExpired:
                results[file] = {"status": "TIMEOUT", "output": "Execution timed out"}
        
        return results
