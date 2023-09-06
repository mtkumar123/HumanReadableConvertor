## Task Description

Create a python script that accepts command line arguments. The first argument will be a string with characters of only S and T. The second argument will be a variable sequence of integers. Using the input arguments output a string where S is Soft and T is Tough following the string pattern provided with a length determined by the input integer.

Example input:  
SST 5 2

Example output:  
Soft, Soft, Tough, Soft and Soft.  
Soft and Soft.

## Running the script

To run the script do the following:

`python main.py STS 2 3 5`

The first argument is the string of characters S and T. The second argument is the sequence of integers.

The above execution will result in the following output:

```
Soft and Tough.
Soft, Tough and Soft.
Soft, Tough, Soft, Soft and Tough.
```
To view more details about the script

`python main.py -h`

Output:

```
usage: main.py [-h] text numbers [numbers ...]

positional arguments:
  text        Enter string of S and T to format output
  numbers     Enter a sequence of integers separated by a space

options:
  -h, --help  show this help message and exit
```

## Running tests

Tests have been written using pytest. Make sure pytest is installed - requirements-dev.txt has the requirement if need be. Make sure you are in the project root folder:

1. pip install -r requirements-dev.txt
2. pytest .

You should see all tests passing:

```
collected 6 items
test_main.py ......
6 passed in 0.01s
```

## Thoughts

Time taken: ~3 hours  
Writing the code took around 1.5 hours. I think I started off with using quotient and remainder approach first, but then realized this would be better as a recursive function. Had to do some reading of the argparse library documentation. Overall I think it was straightforward.
Writing the test cases and documentation took another 1.5 hours.

### Assumptions 
- If integer provided is a negative or 0 number then a blank string is outputted.
