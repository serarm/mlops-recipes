# Notes from Module1 Lesson2 : Coding Best Practices

1. Code needs to be broken down in to `functions` and `modules`.
2. `Clean code`: Code that is readable, simple, and concise. Clean production-quality code is crucial for collaboration and maintainability in software development.
3. `Modular code`: Code that is logically broken up into functions and modules. Modular production-quality code that makes your code more organized, efficient, and reusable.
4. `Module`: A file. Modules allow code to be reused by encapsulating them into files that can be imported into other files.
5. Use meaningful names:
   + `Be descriptive and imply type`: For booleans, you can prefix with is_ or has_ to make it clear it is a condition. You can also use parts of speech to imply types, like using verbs for functions and nouns for variables.
   + `Be consistent but clearly differentiate`: age_list and age is easier to differentiate than ages and age.
   + `Avoid abbreviations and single letters`
   + `Long names aren't the same as descriptive names`
6. Uses spaces propery.Refer to [`PEP8 standards`](https://www.python.org/dev/peps/pep-0008/?#code-lay-out)

## Writing modular code

+ DRY (Don't Repeat Yourself)
+ Abstract out logic to improve readability
+ Minimize the number of entities (functions, classes, modules, etc.)
+ Functions should do one thing
+ Arbitrary variable names can be more effective in general functions and can actually make the code more readable.
+ Try to use fewer than three arguments per function
Optimizing code to be more efficient can mean making it:
+ Execute faster
+ Take up less space in memory/storage
+ Check the tips in [ex2_optimization folder](ex2_optimization)

## Documentation

Several types of documentation can be added at different levels of your program:
+ `Inline comments` - line level
+ `Docstrings` - module and function level
   + [PEP 257 Docstring convention](https://www.python.org/dev/peps/pep-0257/)
+ `Project documentation` - project level example readme
   + [Scikit-learn](https://github.com/scikit-learn/scikit-learn)
   + [Bootstrap](https://github.com/twbs/bootstrap)

## Auto-PEP8 and Linting

+ Once you have a working solution in a notebook, it is useful to make your code reusable by creating a function.
+ You can then add a if `__name__ == "__main__"` block to your script to be run for testing or showing how the functions in your script work.
+ Running your script from the terminal can be done with ipython script_name.py or python script_name.py
+ Two ways to automate clean code are with
 + pylint
 + autopep8
+ `pylint script_name.py` will provide feedback on updates to make to your code, as well as a score out of 10 that can help you understand which improvements are most important.
+ `autopep8 --in-place --aggressive --aggressive script_name.py` will attempt to automatically clean up your code
+ Refer to scripts in [ex3_linting folder](ex3_linting).Use following command to check for PEP8
```Bash
pylint holiday_gifts_mysol.py 
autopep8 --in-place --aggressive --aggressive
```
+ Files details under folder [ex3_linting](ex3_linting):
  + [Excercise instruction file](ex3_linting/holiday_gifts.py)
  + [Udacity provided solution](ex3_linting/holiday_gifts_solution.py)
  + [My solution](ex3_linting/holiday_gifts_mysol.py)


## Key Terms

+ `Refactoring` - the process of writing code that improves its maintainability, speed, and readability without changing its functionality.
+ `Modular` - the logical partition of software into smaller programs for the purpose of improved maintainability, speed, and readability.
+ `Efficiency` - using the resources optimally where resources could be memory, CPU, time, files, connections, databases, etc. [Source]
+ `Optimization` - a way of writing code to be more efficient.
+ `Documentation` - written material or illustration that explains computer software.
+ `Linting` - the automated checking of your source code for programmatic, syntactic, or stylistic errors. 
+ `PEP8` - a document providing guidelines and best practices for writing Python code.