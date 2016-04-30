import mini_lisp as ml
import sys


def printFail(program, expected= None , actual = None,e = None):
    print '****FAILED****'
    if expected and actual:
        print 'Expected: ' + str(expected) + ', Actual: ' + str(actual)
    if e:
        print 'Exception: ' + str(e)



def test(program,expected):
    print 'Excecuting: ' + str(program)
    try:
        actual = ml.eval(ml.parse(program))
        if expected != actual:
            printFail(program,expected,actual)
        else:
            print 'PASS'
    except:
        e = sys.exc_info()
        printFail(program,e)


program = "(car '(1 2))"
test(program, 1)

program = "(cdr '(1 2 3 4))"
test(program,[2,3,5])

program = "(cons "



ml.eval(ml.parse(program))


