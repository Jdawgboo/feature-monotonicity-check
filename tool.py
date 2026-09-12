def violations(values: list[float], direction: str='increasing') -> list[int]:
    sign=1 if direction=='increasing' else -1
    return [i for i in range(1,len(values)) if sign*(values[i]-values[i-1])<0]
