from datetime import datetime
def log_call(func):
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("log.txt", "a") as file:
            file.write(
                f"{timestamp} | {func.__name__} | args={args} | kwargs={kwargs}\n"
            )
        return func(*args, **kwargs)
    return wrapper
def greet(name):
    print(f"Hello {name}")
@log_call
def add(a, b):
    print(f"Sum = {a + b}")
@log_call
def multiply(a, b):
    print(f"Product = {a * b}")
def read_logs():
    counts = {}
    with open("log.txt", "r") as file:
        for line in file:
            parts = line.split("|")
            function_name = parts[1].strip()
            counts[function_name] = counts.get(function_name, 0) + 1
    print("\nFunction Call Summary")
    print("-" * 25)
    for func, count in counts.items():
        print(f"{func}: {count} calls")
greet("Rahees")
greet("Ali")
add(10, 20)
add(5, 15)
multiply(3, 4)
multiply(2, 8)
read_logs()