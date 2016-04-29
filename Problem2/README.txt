PARSE AND EVAL FUNCTIONS WRITTEN SEPARATELY. TO RUN:
	>>> import mini_lisp
	>>> program = "(enter program here)"
	>>> mini_lisp.eval(mini_lisp.parse(program))

Arithmetic functions support multiple arguments as well as negatives.
   - Minus also supports unary minus.
   - Division rounds quotients towards 0 after each division. Can't divide by 0.

Let allows assignments to multiple variables
   - Returns local dictionary of value assignments if no expressions to be evaluated using those variables. (Resets each time let is called)
   - Multiple expressions return the value of the last expression evaluated.
	i.e supports "(let (a 3)(b 2))", "(let (a 3)(b 2)(+ 1 a)(- 2 b))"

Concat
   - Can concatenate strings/ints to each other but only lists to lists
	i.e "(concat '(1 2 3) '(a b c))" --> [1, 2, 3, 'a', 'b', 'c']
	    "(concat 1 2 3 4 5)" --> '12345'
	    "(concat 'abc' 1 2 3)" --> 'abc123'
