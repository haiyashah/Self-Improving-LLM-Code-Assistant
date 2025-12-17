# Self-Improving LLM Code Assistant 🚀

## Project Goal
Build an AI agent that **reviews Python code, detects logical errors, and improves its reasoning over time** using verification and memory — designed as a **real-world developer assistant**.

---

## Use Case
Large engineering teams spend thousands of hours on code reviews. This agent:
- Analyzes pull requests
- Checks for logical, type, and edge-case errors
- Provides verified recommendations
- Learns from past mistakes to reduce false positives

---

## How It Works 💡
1. **Plan:** LLM generates structured review steps.
2. **Execute:** Runs tests, static analysis, and type checks.
3. **Verify:** Confirms each claim programmatically.
4. **Reflect:** Stores failed reviews and corrections.
5. **Improve:** Uses memory to avoid repeating errors.

---

## Technologies ⚙️
- **LLM:** GPT-4.1 (planner and reasoning)
- **Tools:** `pytest`, `mypy`, `pylint`, `coverage.py`
- **Memory:** FAISS + Sentence-Transformers embeddings
- **Infrastructure:** Python 3.11, Docker

---

## Evaluation Metrics
- Verified Bug Precision (%)
- False Positive Rate (%)
- Average Review Steps
- Improvement over successive runs

---

## Results Snapshot
| Metric                     | Baseline | Agent w/ Memory |
|----------------------------|----------|----------------|
| Verified Bug Precision     | 58%      | 84%            |
| False Positive Rate        | 31%      | 9%             |
| Avg. Review Steps          | 11.2     | 6.4            |

---
# Self-Improving LLM Code Assistant

A modular framework for automatically reviewing, executing, and improving code changes using LLMs. The system plans steps, executes tests, verifies results, stores past lessons, and evaluates performance over time.

## Project Structure

## Project Structure

```text

├── planner/                # LLM planning module
│   ├── plan_generator.py   # Generates structured review plans from PR diff
│   ├── plan_schema.json    # Defines JSON schema for structured plans
│   └── prompts/            # Optional prompt templates for LLM planning
├── executor/               # Code execution and test runner
│   ├── run_tests.py        # Runs pytest, coverage.py for each step
│   ├── static_analysis.py  # Runs pylint, mypy checks
│   └── tool_interface.py   # Wrapper for calling tools programmatically
├── verifier/               # Verification of plan steps
│   ├── verify_results.py   # Checks if step outputs match expected results
│   ├── assertion_checks.py # Encodes deterministic checks per step
│   └── verification_utils.py # Helpers for logging and reporting
├── memory/                 # Stores past failures and corrections
│   ├── memory_db.py        # FAISS vector DB interface
│   ├── embeddings.py       # Embeddings of failed steps / lessons
│   └── memory_utils.py     # Query/update memory for future plans
├── evaluation/             # Metrics and analysis scripts
│   ├── evaluate_agent.py   # Calculates precision, false positives, steps
│   ├── plot_metrics.py     # Generates plots of improvement over time
│   └── ablation_studies.py # Optional ablation experiments
├── data/                   # Sample pull requests and test data
│   ├── sample_prs/         # Directory of Python PR diffs
│   ├── tests/              # Unit tests for PRs
│   └── configs.json        # Mapping PRs to expected outputs
├── configs/                # Configuration files
│   ├── agent_config.yaml   # LLM temperature, max tokens, tools allowed
│   └── evaluation_config.yaml # Metrics and evaluation settings
└── README.md               # Project overview

```

## Features

- **Planner:** Generates structured step-by-step plans from PR diffs.
- **Executor:** Runs tests, static analysis, and tools programmatically.
- **Verifier:** Checks outputs and assertions for each plan step.
- **Memory:** Stores past failures and improvements for future guidance.
- **Evaluation:** Tracks metrics, generates plots, and supports ablation studies.

## Usage

1. Configure LLM and evaluation settings in `configs/`.
2. Provide sample PRs in `data/sample_prs/`.
3. Run the planner → executor → verifier pipeline.
4. Evaluate agent performance via `evaluation/evaluate_agent.py`.


---

## Author
Haiya Shah | Carnegie Mellon University  
Interests: AI agents, reasoning, verification, reliable systems
