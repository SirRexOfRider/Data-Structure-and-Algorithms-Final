def basic_key(title):
    """ 
    A basic key generator that just sums the ord value of the characters of the title. 
    Not the best at preventing collisions. 
    """
    return sum(map(ord, title))

def positional_ord(title):
    """ 
    A more complex key generator that sums the product of the ord values and the positions of the title characters. 
    Better at preventing collisions. 
    """
    return sum(map(lambda i: ord(i[1]) * i[0], enumerate(title)))
