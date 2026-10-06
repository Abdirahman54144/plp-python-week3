count = 1
total = 0

# BUG: The original loop condition was 'count < 5', which stopped before adding 5. Changed to 'count <= 5' so it includes numbers 1 through 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: The original code attempted to concatenate a string with an integer using '+', causing a TypeError. Fixed by using an f-string or converting 'total' to str.
# BUG: Also fixed the logic bug above so the total equals 15 instead of 10.
print(f"Sum of 1 to 5 is: {total}")