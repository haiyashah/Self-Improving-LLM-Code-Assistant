import logging

class AblationStudy:
    def __init__(self, agent):
        self.agent = agent

    def run_experiment(self, pr_list, config_type: str):
        """
        config_type: 'full_system', 'no_memory', 'no_verification'
        """
        logging.info(f"Starting Ablation Study: {config_type}")
        
        # Temporary modifications to agent behavior
        original_memory = self.agent.memory
        if config_type == 'no_memory':
            self.agent.memory = None # Disable memory lookup
            
        results = []
        for pr in pr_list:
            outcome = self.agent.run_review(pr['id'], pr['diff'])
            results.append(outcome)
            
        # Restore original state
        self.agent.memory = original_memory
        return results
