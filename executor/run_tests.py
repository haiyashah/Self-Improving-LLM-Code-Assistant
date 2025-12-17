import subprocess
import os

class TestRunner:
    def run_pytest(self, test_files: list) -> dict:
        """Executes pytest and captures detailed output."""
        results = {}
        for file in test_files:
            if not os.path.exists(file):
                results[file] = {"status": "ERROR", "output": "File not found"}
                continue
                
            cmd = ["pytest", file, "--maxfail=1", "-q"]
            process = subprocess.run(cmd, capture_output=True, text=True)
            
            results[file] = {
                "status": "PASS" if process.returncode == 0 else "FAIL",
                "output": process.stdout if process.returncode == 0 else process.stderr
            }
        return results

    def run_static_analysis(self, files: list) -> dict:
        """Runs mypy for type checking."""
        results = {}
        for file in files:
            cmd = ["mypy", file, "--ignore-missing-imports"]
            process = subprocess.run(cmd, capture_output=True, text=True)
            results[file] = {
                "exit_code": process.returncode,
                "output": process.stdout
            }
        return results
