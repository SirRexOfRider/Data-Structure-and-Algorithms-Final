def basic_key(title):
    """ 
    A basic key generator that just sums the ord value of the characters of the title. 
    Not the best at preventing collisions. 
    """
    return sum(map(ord, title))
