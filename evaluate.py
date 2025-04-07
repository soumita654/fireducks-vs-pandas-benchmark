import time

def evaluate(label, func):
    start = time.time()
    result = func()
    end = time.time()
    print(f"{label}: {end - start:.4f} sec")
    return result
