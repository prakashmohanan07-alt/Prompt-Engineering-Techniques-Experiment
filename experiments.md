# Experiments

## Experiment 1: Math Reasoning
**Task:** A shop sells pens at 12 rupees each. Ravi buys 7 pens and pays with a 100 rupee note. How much change does he get?

| Technique | Prompt | Observation | Score (1-5) |
|-----------|--------|-------------|-------------|
| Zero-shot | "Ravi buys 7 pens at 12 rupees each and pays 100. Change?" | Short answer, little explanation | |
| Chain-of-Thought | "...Think step by step before answering." | Shows 7 x 12 = 84, then 100 - 84 = 16 | |
| Structured | "...Reply as JSON with keys: total_cost, change." | Clean machine-readable output | |

## Experiment 2: Sentiment Classification
**Task:** Classify the review: "The delivery was late but the product is great."

| Technique | Prompt | Observation | Score (1-5) |
|-----------|--------|-------------|-------------|
| Zero-shot | "Classify the sentiment of this review." | May say Mixed or Positive | |
| Few-shot | Add 3 labelled example reviews first | More consistent labels | |
| Constraint | "Answer with exactly one word: Positive, Negative or Neutral." | One-word answer | |

## Experiment 3: Explaining a Concept
**Task:** Explain what an API is.

| Technique | Prompt | Observation | Score (1-5) |
|-----------|--------|-------------|-------------|
| Zero-shot | "Explain what an API is." | Generic explanation | |
| Role prompting | "You are a teacher explaining to a 10 year old. Explain what an API is." | Simple, uses analogy | |
| Constraint | "Explain an API in 3 sentences for a beginner." | Short and focused | |

## Conclusion
- Chain-of-Thought improves accuracy on reasoning tasks.
- Few-shot improves consistency for classification.
- Role and constraint prompting control tone and length.
- Structured output is best when the result is used by another program.
- Clear, specific prompts almost always beat vague ones.

*Fill in the Observation and Score columns with your own results after running the prompts.*
