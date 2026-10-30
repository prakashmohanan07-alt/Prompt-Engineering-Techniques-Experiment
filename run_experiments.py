"""Runs the same tasks with different prompting techniques and saves results."""
import os
import anthropic

MODEL = "claude-sonnet-5-5"
client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

MATH = "Ravi buys 7 pens at 12 rupees each and pays with a 100 rupee note."
REVIEW = "The delivery was late but the product is great."

EXPERIMENTS = {
    "Math - Zero-shot": MATH + " How much change does he get?",
    "Math - Chain-of-Thought": MATH + " How much change does he get? Think step by step.",
    "Math - Structured": MATH + " Reply only as JSON with keys total_cost and change.",
    "Sentiment - Zero-shot": f"Classify the sentiment of this review: {REVIEW}",
    "Sentiment - Few-shot": (
        "Review: Loved it! -> Positive\n"
        "Review: Totally broken. -> Negative\n"
        "Review: It is okay. -> Neutral\n"
        f"Review: {REVIEW} ->"
    ),
    "Sentiment - Constraint": f"Answer with one word (Positive, Negative or Neutral): {REVIEW}",
    "API - Zero-shot": "Explain what an API is.",
    "API - Role": "You are a teacher talking to a 10 year old. Explain what an API is.",
    "API - Constraint": "Explain what an API is in 3 sentences for a beginner.",
}


def ask(prompt):
    response = client.messages.create(
        model=MODEL,
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


with open("results.md", "w", encoding="utf-8") as f:
    f.write("# Results\n\n")
    for name, prompt in EXPERIMENTS.items():
        print(f"Running: {name}")
        f.write(f"## {name}\n**Prompt:** {prompt}\n\n**Output:**\n{ask(prompt)}\n\n---\n\n")

print("Done. See results.md")
