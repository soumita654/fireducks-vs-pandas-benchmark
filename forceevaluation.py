def evaluate(label, func):
    import time
    start = time.time()
    result = func()
    end = time.time()
    print(f"{label}: {end - start:.4f} sec")
    return result
