# Goal
Solve Problems from https://projecteuler.net/  in python, R, javascript, sql (postgres) to gain better understanding of the languages. No libraries/packages allowed (except for unit testing libraries). Each function is developed using test driven development.

# Structure
Each Problem has its own folder given by the ID of the problem. Each folder contains a funcs file, a testing file and a script file.


# Python
Using python 3 and unittest package.

# Javascript
Using browser to run js. Thats why each problem includes a tests.html for running tests (using QUnit library) and Script.html to run the solution to the problem itself in the browser. Solution given as console.log().

# SQL
Using a postgres server to create databases and for running the scripts.

# R
Using unittest library.

# Funcs file
Each funcs file contains all functions needed for the problem. This means functions can repeat in different problems. For clarity I allow that.

# Testing file
For each function I first think of tests to validate the output of the function. Only after I have defined tests, I start the coding. Each function has tests associated with it as I use Test Driven Development (unit tests).

# Script file
Each script file solves the given problem when executed and returns the answer as a printed value (console.log for javascript).
