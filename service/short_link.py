import random, string

def short_link(dom : str="short-link.com", _range : int=13, _char : str=string.ascii_letters + string.digits):
    return 'http://' + dom +'/' + ''.join(random.SystemRandom().choice(_char) for _ in range(_range)) + '/'


if __name__ == "__main__":
    print(short_link())
    print(short_link(_char="AaBb", _range=25))
    print(short_link("sspw.pl"))
    print(short_link(_range=25))
    print(short_link('bardzokrotkilink.pl', 8))