Following integer calculations as referenced from https://www.gnu.org/software/emacs/manual/html_node/elisp/Arithmetic-Operations.html
All arithmetic functions support integer type fully (including negatives)

- Minus: has support for unary minus as well as subtraction
- Multiply: Allows 0+ arguments
	- 0 arguments = returns 1
	- 1 argument  = returns the value itself
	- 2+ arguments = successive multiplication
- Division: Allows 1+ arguments
	- 1 argument: returns reciprocal of the value
	- Rounds quotients towards 0 after each division

- Let allows multiple operators and will return the last evaluated expression
	(let (a 3)(+ 1 a)(- 2 a)) --> -1

- If only supports #t/#f or True False but can evaluate expressions as the consequence/alternative
	(if #t 3 2) --> 3
	(if #f (let (a 3)(+ 1 a))(let (a 4)(- 2 a))) --> -2