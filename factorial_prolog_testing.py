from pyswip import *
prolog = Prolog()
prolog.consult('factorial.pl')
q = prolog.query("factorial(5,X)")
for result in q:
    print result["X"]
