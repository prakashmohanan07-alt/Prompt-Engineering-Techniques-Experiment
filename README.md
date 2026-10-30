# Prompt Engineering Techniques Experiment

A small project that compares common prompt engineering techniques on the same tasks, to see how the way we ask changes the quality of an AI model's answer.

## Objective
- Understand popular prompt engineering techniques.
- Run the same task with different prompting styles.
- Compare the outputs and record which technique works best.

## Techniques Covered
| # | Technique | Idea |
|---|-----------|------|
| 1 | Zero-shot | Ask directly, no examples |
| 2 | Few-shot | Give 2-3 examples before the task |
| 3 | Chain-of-Thought | Ask the model to reason step by step |
| 4 | Role prompting | Assign the model a role or persona |
| 5 | Structured output | Ask for a fixed format (JSON, table) |
| 6 | Constraint prompting | Add limits (word count, tone, audience) |

## Project Structure
```
prompt-engineering-experiment/
├── README.md            # Project overview
├── experiments.md       # Prompts, observations and results
├── run_experiments.py   # Script to run all prompts automatically
└── requirements.txt     # Python dependencies
```

## How to Run (optional)
```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY="your-key-here"
python run_experiments.py
```
Results are saved to `results.md`. You can also run the prompts manually in any chat AI and paste outputs into `experiments.md`.

## Methodology
1. Pick a task (summarising, math reasoning, classification).
2. Write one prompt per technique for the same task.
3. Run each prompt and record the output.
4. Score each output (1-5) on accuracy, clarity and format.
5. Compare and conclude.

## Key Findings
See the Conclusion section in `experiments.md`.

## Author
Your Name | VAC Project
