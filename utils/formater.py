
def format_time(seconds: float) -> str:
    if seconds >= 1:
        return f"{seconds:.1f} sec"
    elif seconds >= 0.001:
        return f"{seconds * 1000:.1f} ms"
    else:
        return f"{seconds * 1_000_000:.1f} µs"