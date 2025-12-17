import logging
from planner.plan_generator import PlanGenerator
from executor.run_tests import TestRunner
from verifier.verify_results import Verifier
from memory.memory_db import ReasoningMemory
from memory.embeddings import embed_text

# Setup logging for a "tangible" console output
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("CodeAssistant")

class AIAgent:
    def __init__(self):
        self.memory = ReasoningMemory()
        self.planner = PlanGenerator(llm_client=None) # Replace with actual LLM client
        self.executor = TestRunner()
        self.verifier = Verifier()

    def run_review(self, pr_id, pr_diff):
        logger.info(f"--- Starting Review for {pr_id} ---")

        # 1. Retrieve Past Lessons from Memory
        query_vector = embed_text(pr_diff)
        past_lessons = self.memory.query(query_vector)
        logger.info(f"Retrieved {len(past_lessons)} relevant lessons from memory.")

        # 2. Generate Plan (LLM would use past_lessons in prompt)
        plan = self.planner.generate_plan(pr_diff, past_failures=past_lessons)
        
        # Mocking a plan for demonstration
        if not plan:
            plan = [
                {
                    "step_id": 1,
                    "intent": "Check for type safety in calculation",
                    "files": ["logic.py"],
                    "tools": ["mypy"],
                    "expected_signal": "Success: no issues found"
                }
            ]

        results_summary = []

        # 3. Execution & Verification Loop
        for step in plan:
            logger.info(f"Executing Step {step['step_id']}: {step['intent']}")
            
            # Run tools
            if "mypy" in step['tools']:
                exec_output = self.executor.run_static_analysis(step['files'])
            elif "pytest" in step['tools']:
                exec_output = self.executor.run_pytest(step['files'])
            else:
                exec_output = {}

            # Verify output
            is_verified = self.verifier.verify_step(step, exec_output)
            results_summary.append({"step": step, "verified": is_verified})

            # 4. Reflection: If verification fails, store in memory
            if not is_verified:
                logger.warning(f"Step {step['step_id']} failed verification. Storing lesson.")
                failure_context = f"Tool output did not contain: {step['expected_signal']}"
                self.memory.add(embed_text(str(step)), {"step": step, "reason": failure_context})

        logger.info(f"--- Review Complete for {pr_id} ---")
        return results_summary

if __name__ == "__main__":
    # Sample Input
    sample_diff = """
    --- a/logic.py
    +++ b/logic.py
    @@ -1,5 +1,5 @@
    -def calculate(val):
    -    return val * 10
    +def calculate(val: int) -> int:
    +    return val * 10
    """
    
    agent = AIAgent()
    agent.run_review("PR_001", sample_diff)
