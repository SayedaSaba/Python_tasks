'What’s the output? explain'

def foo():
    print("foo")
    return False
def bar():
    print("bar")
    return True

if foo() and bar():
    print("Hello")

'It checks foo first and it prints foo and returns false value , it does not checks bar and does not print hello as we are using and operator'