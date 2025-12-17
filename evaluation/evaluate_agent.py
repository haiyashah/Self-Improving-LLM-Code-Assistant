class EvaluationEngine:
    def __init__(self):
        self.history = []

    def record_run(self, verified_steps, total_steps, false_positives):
        self.history.append({
            "verified": verified_steps,
            "total": total_steps,
            "fp": false_positives
        })

    def get_report(self):
        if not self.history:
            return "No data recorded."

        total_runs = len(self.history)
        avg_precision = sum(r['verified']/r['total'] for r in self.history) / total_runs
        avg_fp_rate = sum(r['fp']/r['total'] for r in self.history) / total_runs
        
        return f"""
        --- AGENT PERFORMANCE REPORT ---
        Total Runs Evaluated: {total_runs}
        Precision:            {avg_precision:.2%}
        False Positive Rate:  {avg_fp_rate:.2%}
        -------------------------------
        """
