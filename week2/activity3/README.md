# Week2 Activity 3

This is a simple calculator example which includes a Calculator class, 2 input helper functions and a main entry function.

## Class Calculator
The Calculator class provides 6 methods to support 6 kinds of operations including add, minus, multiply, divide, modulo and
factorial, allowing calculation from integer, float and complex types if possible. Moreover, 2 additional result print methods
are available to allow formatted output during the calculation.
The class also includes a member variable error to indicate violation in the caculation.

## Application
The application provides 2 helper input functions with error handling to ensure valid operation and number inputs. It creates
an instance of Calculator class for the real calculation and result output.

## Sample output
== Calculator application: ==  
  
Operations:  
1. add  
2. minus  
3. multiply  
4. divide  
5. modulo  
6. factorial  
7. quit  
Select(1/2/3/4/5/6/7): 1  
x = 4.5  
y = 6  
4.5 + 6 = 10.5  
  
Operations:  
1. add  
2. minus  
3. multiply  
4. divide  
5. modulo  
6. factorial  
7. quit  
Select(1/2/3/4/5/6/7): 1  
x = 4a  
Wrong number 4a, try again...  
x = 4 + 4j  
Wrong number 4 + 4j, try again...  
x = 4+4j  
y = 5.3  
(4+4j) + 5.3 = (9.3+4j)  
  
Operations:  
1. add  
2. minus  
3. multiply  
4. divide  
5. modulo  
6. factorial  
7. quit  
Select(1/2/3/4/5/6/7): 2  
x = 5.4  
y = 2  
5.4 - 2 = 3.4000000000000004  
  
Operations:  
1. add  
2. minus  
3. multiply  
4. divide  
5. modulo  
6. factorial  
7. quit  
Select(1/2/3/4/5/6/7): 3  
x = 4-3j  
y = 4+3j  
(4-3j) * (4+3j) = (25+0j)  
  
Operations:  
1. add  
2. minus  
3. multiply  
4. divide  
5. modulo  
6. factorial  
7. quit  
Select(1/2/3/4/5/6/7): 4  
x = 2  
y = 0+0j  
2 / 0j error: Divide by zero  
  
Operations:  
1. add  
2. minus  
3. multiply  
4. divide  
5. modulo  
6. factorial  
7. quit  
Select(1/2/3/4/5/6/7): 4  
x = 3  
y = 2.4  
3 / 2.4 = 1.25  
  
Operations:  
1. add  
2. minus  
3. multiply  
4. divide  
5. modulo  
6. factorial  
7. quit  
Select(1/2/3/4/5/6/7): 4  
x = 4-2j  
y = 2+3j  
(4-2j) / (2+3j) = (0.15384615384615383-1.2307692307692308j)  
  
Operations:  
1. add  
2. minus  
3. multiply  
4. divide  
5. modulo  
6. factorial  
7. quit  
Select(1/2/3/4/5/6/7): 5  
x = 4.5  
y = 2  
4.5 % 2 = 0.5  
  
Operations:  
1. add  
2. minus  
3. multiply  
4. divide  
5. modulo  
6. factorial  
7. quit  
Select(1/2/3/4/5/6/7): 6  
x = 1-j  
(1-1j)! error: complex not supported  
  
Operations:  
1. add  
2. minus  
3. multiply  
4. divide  
5. modulo  
6. factorial  
7. quit  
Select(1/2/3/4/5/6/7): 6  
x = 4  
4! = 24  
  
Operations:  
1. add  
2. minus  
3. multiply  
4. divide  
5. modulo  
6. factorial  
7. quit  
Select(1/2/3/4/5/6/7): 7  
