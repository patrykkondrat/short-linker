import random, string

from numpy import short

def short_link(dom="jebacpis.com", _range=13, _char=string.ascii_letters + string.digits):
    return dom +'/' + ''.join(random.SystemRandom().choice(_char) for _ in range(_range)) + '/'


if __name__ == "__main__":
    print(short_link())
    print(short_link(_char="AaBb", _range=25))
    print(short_link("sspw.pl"))
    print(short_link(_range=25))
    print(short_link('bardzokrotkilink.pl', 8))