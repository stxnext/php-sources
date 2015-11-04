# -*- coding: utf-8 -*-
''' COMPREHENSIONS '''

[ EXPRESSION for VARIABLE in SEQUENCE if CONDITION ]

[ n**2 for n in range(10) if n % 2==0 ]

[ n for n in range(10) ]

{key: value for key, value in enumerate('abcde')}




''' LAMBDA '''

lambda VARIABLES: EXPRESSION
lambda x: x**2
lambda x, y, z: (x**2 + y) / z


data = [{
    'name': 'Book',
    'price': '10',
}, {
    'name': 'Phone',
    'price': '20',
}]

sorted(data, key=lambda x: x['price'])




''' GENERATORY - YIELD '''

def squares():
    x = 1
    while True:
        yield x
        yield x**2
        x = x + 1

sq = squares()
for x in range(100):
    import pdb; pdb.set_trace() # put PDB here and step into functions
    print "number %s" % sq.next()
    print "square %s" % sq.next()
