# Week 3 Assignment: Conditions and Loops

## File Descriptions
* `grade_reporter.py`: Processes student scores using a `for` loop and `if/elif/else` conditions to calculate grades, pass/fail counts, and average score.
* `bug_hunt.py`: Contains a fixed `while` loop script with `# BUG:` comments explaining syntax and logic errors.

## Bug Analysis
The hardest bug to find in Part B was the logic error in the condition `while count < 5`. Because it produced no syntax error message, the code executed successfully but printed an incorrect sum of 10 instead of 15. I identified something was wrong by comparing the actual printed output against the expected mathematical result of summing numbers 1 through 5.