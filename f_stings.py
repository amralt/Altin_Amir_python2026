def format_number(n):
    s = f"{n:_.3f}".replace('_', ' ')
    stars = '*' * ((30 - len(s))//2)
    return stars + s + stars

print(format_number(123488482390.28174))
