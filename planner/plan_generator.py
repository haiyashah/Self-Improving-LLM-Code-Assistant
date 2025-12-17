import json
import logging
from typing import List, Dict

class PlanGenerator:
    def __init__(self, llm_client):
        self.llm = llm_client
        self.logger = logging.getLogger(__name__)

    def _generate_prompt(self, pr_diff: str, past_failures: List[Dict]) -> str:
        memory_context = ""
        if past_failures:
            memory_context = "\nLessons from past failures:\n" + "\n".join(
                [f"- Avoid {f['reason']} in {f['step']['files']}" for f in past_failures]
            )

        return f"""
        You are an expert Python QA Architect. Analyze the following PR diff and generate a verification plan.
        {memory_context}
        
        PR DIFF:
        {pr_diff}

        Return a JSON list of steps. Each step must include:
        - step_id: integer
        - intent: objective of the check
        - files: list of files to analyze
        - tools: ['pytest', 'mypy', or 'pylint']
        - expected_signal: specific string to look for in output.
        """

    def generate_plan(self, pr_diff: str, past_failures: List[Dict] = None) -> List[Dict]:
        prompt = self._generate_prompt(pr_diff, past_failures)
        try:
            # Simulated LLM call returning JSON
            response = self.llm.chat(prompt) 
            plan = json.loads(response)
            self.logger.info(f"Generated plan with {len(plan)} steps.")
            return plan
        except json.JSONDecodeError:
            self.logger.error("LLM returned invalid JSON.")
            return []

    def save_plan(self, plan: List[Dict], filename="plan.json"):
        with open(filename, "w") as f:
            json.dump(plan, f, indent=4)
