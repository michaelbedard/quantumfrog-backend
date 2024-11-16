

def get_proximity_index(firefly, frog):
    # inner product
    inner_product = firefly.inner(frog)

    # proximity index from 0 to 1: 0 -> orthogonal states; 1 -> identical states (ignoring the global phase factor)
    # It's the probability that the 2 states would be aligned if measured
    proximity_index = abs(inner_product) ** 2
    return proximity_index