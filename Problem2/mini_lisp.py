from yacc import yacc

def parse(program):
    result = yacc.parse(program)
    if result != None:
        return result

################ Environments
Symbol = str          # A Lisp Symbol is implemented as a Python str
List   = list         # A Lisp List is implemented as a Python list
Number = (int, float) # A Lisp Number is implemented as a Python int or float

def standard_env():
    "An environment with some Scheme standard procedures."
    import math, operator as op
    env = Env()
    env.update(vars(math)) # sin, cos, sqrt, pi, ...
    env.update({
        '+':       lambda *x: sum(x),
        '-':       lambda *x: x[0] - sum(x[1:]) if len(x)>1 else -x[0],
        '*':       lambda *l: reduce(lambda x,y: x*y, l),
        '/':       lambda *l: reduce(lambda x,y: x//y if x/y > 0 or x%y == 0 else x//y + 1, l) if 0 not in l[1:] else "Cannot divide by 0",
        '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq,
        '#t':      True,
        '#f':      False,
        'car':     lambda x: x[0],
        'cdr':     lambda x: x[1:],
        'cons':    lambda x,y: [x] + y,
        'eq?':     op.is_,
        'equal?':  op.eq,
        'length':  len,

        'list':    lambda *x: list(x),


        'not':     op.not_,
    })
    return env

class Env(dict):
    "An environment: a dict of {'var':val} pairs, with an outer Env."
    def __init__(self, parms=(), args=(), outer=None):
        self.update(zip(parms, args))
        self.outer = outer
    def find(self, var):
        "Find the innermost Env where var appears."
        return self if (var in self) else self.outer.find(var)

global_env = standard_env()

################ Procedures

class Procedure(object):
    "A user-defined Scheme procedure."
    def __init__(self, parms, body, env):
        self.parms, self.body, self.env = parms, body, env
    def __call__(self, *args):
        return eval(self.body, Env(self.parms, args, self.env))

################ eval

def eval(x, env=global_env):
    "Evaluate an expression in an environment."
    if isinstance(x, Symbol) and (x in env):      # variable reference
        print("LOOK UP SYMBOL:", x, "RETURN FUNCTION",env.find(x)[x])
        return env.find(x)[x]
    elif not isinstance(x, List):  # constant literal
        print("2", x)
        return x
    elif x[0] == 'if':             # (if test conseq alt)
        print("3", x)
        (_, test, conseq, alt) = x
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)
    elif x[0] == 'let':
        print("4", x)
        letDict = {}
        assignCount = 0
        functionPresent = False
        for i in range(1, len(x)):
            if x[i][0] not in env:
                assignCount += 1
                var = x[i][0]
                val = x[i][1]
                letDict[var] = val
            else:
                # Breaks assignment as soon as a known function is found in global env
                functionPresent = True
                break
        if functionPresent:
            exps = x[assignCount + 1 :]
            print("EXPRESSIONS:", exps)
            expReturns = []
            for exp in exps:
                for key in letDict.keys():
                    try:
                        # Replace variable in expression with value stored in dict
                        exp[exp.index(key)] = letDict[key]
                    except ValueError:
                        # If key is not in the expression, skip
                        continue
                expReturns.append(eval(exp,env))
            return expReturns
        else:
            return letDict
    else:                          # (proc arg...)
        print("else", x)
        proc = eval(x[0], env)
        args = [eval(exp, env) for exp in x[1:]]
        print("PROC:", proc, "ARGS:", args)
        return proc(*args)
