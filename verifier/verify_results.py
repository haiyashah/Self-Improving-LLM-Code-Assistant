import logging

class Verifier:
    def __init__(self):
        self.logger = logging.getLogger("Verifier")

    def verify_step(self, step: dict, executor_results: dict) -> bool:
        """
        Validates if the output of the tool matches the plan's requirements.
        """
        intent = step['intent']
        expected = step['expected_signal'].lower()
        success = False

        for file, result in executor_results.items():
            actual_output = str(result.get("output", "")).lower()
            
            # Logic: Check if the expected signal is a substring of the output
            if expected in actual_output:
                success = True
                self.logger.info(f"Step {step['step_id']} Verified: Found '{expected}' in {file}")
                break
        
        if not success:
            self.logger.warning(f"Step {step['step_id']} Failed: Expected signal not found.")
            
        return success
