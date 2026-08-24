# Dialog Generation with Constraints

responses = [
    "You may be unable to concentrate because you are feeling stressed about the exam. "
    "Take a short break, then focus on one topic at a time and stay confident.",

    "Since your exam is tomorrow, try to focus on the most important topics first. "
    "Take a short break when needed, and be confident because you can still prepare well.",

    "It is normal to find it hard to concentrate before an important exam. "
    "Take a break, return with better focus, and stay confident in yourself."
]

print("User: I have an important exam tomorrow but I'm not able to concentrate.")

print("\nPossible Responses:\n")

for i, response in enumerate(responses, 1):
    print(f"{i}. {response}\n")


# Simple evaluation
keywords = ["focus", "break", "confident"]

scores = []

for response in responses:
    score = 0

    # Check keyword constraint
    for word in keywords:
        if word in response.lower():
            score += 1

    # Check entity coherence
    if "exam" in response.lower() or "concentrate" in response.lower():
        score += 1

    # Check sentence count (2-3)
    sentence_count = response.count(".")
    if 2 <= sentence_count <= 3:
        score += 1

    scores.append(score)

best_index = scores.index(max(scores))

print("Scores:", scores)
print("\nBest Response:")
print(responses[best_index])