def velocidad(e: float,t: float) -> float:
    v = e / t
    return v


def aceleracion(V: float, v: float, t: float) -> float:
    A = (V - v ) / t
    return A
