import sys
import time


# --------------------------------------------------
# Method 1: Read data using with open()
# --------------------------------------------------

def variance_file(filename):
    with open(filename, "r") as f:
        data = f.read().split()

    data = [float(x) for x in data]

    n = len(data)

    # Calculate mean
    mu = sum(data) / n

    # Calculate variance
    variance = sum((x - mu) ** 2 for x in data) / n

    return variance


# --------------------------------------------------
# Method 2: Read data using sys.stdin
# --------------------------------------------------

def variance_stdin():
    data = sys.stdin.read().split()

    data = [float(x) for x in data]

    n = len(data)

    # Calculate mean
    mu = sum(data) / n

    # Calculate variance
    variance = sum((x - mu) ** 2 for x in data) / n

    return variance


# --------------------------------------------------
# Compare both methods
# --------------------------------------------------

filename = "bec_513/data.txt"

# ----- File method -----
start = time.perf_counter()

var_file = variance_file(filename)

end = time.perf_counter()

file_time = end - start


# ----- stdin method -----
# This part is useful when data is piped into the program.
#
# Example:
#     cat data.txt | python variance.py
#
start = time.perf_counter()

var_stdin = variance_stdin()

end = time.perf_counter()

stdin_time = end - start


# --------------------------------------------------
# Results
# --------------------------------------------------

print("Variance using with open():", var_file)
print("Time using with open():", file_time, "seconds")

print("Variance using sys.stdin:", var_stdin)
print("Time using sys.stdin:", stdin_time, "seconds")