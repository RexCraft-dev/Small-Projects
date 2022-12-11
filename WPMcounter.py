import time

print("--------------------------------------------")
print("    Words per Minute Calculator v1.0")
print("--------------------------------------------")
print("  **WARNING** Time starts immediately!")

# Start timer by pressing any key.
start = input("         Press Enter to begin.")
start_time = time.perf_counter_ns()

prompt = "The brown fox jumped over the big red barn."
char_count = len(prompt)

print(" ")
print("--------------------------------------------")
print(prompt)
print("--------------------------------------------")

# User input
answer = input()\

# Timer stops when user finishes input.
end_time = time.perf_counter_ns()

# Determine total elapsed time.
elapsed_time = (end_time - start_time) / 1e9

# Calculate Words per Minute.
wpm = (int(len(prompt)) / 5) / (elapsed_time / 60)

# Accumulator for correct characters.
hits = 0

# Loop through answer and accumulate correct inputs.
for i in range(0, len(answer)):
    if prompt[i] == answer[i]:
        hits += 1

# Calculate accuracy.
accuracy = hits / len(prompt) * 100

# Output results.
print("--------------------------------------------")
print(f"Total Duration: {elapsed_time:.4f} seconds.")
print(f"Words per Minute (WPM): {int(wpm)}")
print(f"Accuracy: {accuracy:.2f}%")