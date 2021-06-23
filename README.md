# CS-210-Project3

### Description

The purpose of this project is to take a file containing a list of items and create usable outputs based on it.
Prompts a user with a list of options to select from. Based on the user's input, it will display one of three things:

1. Print a list of all products and quantities sold.
2. Allows user to specify a product to look for, if product is found, return quantity sold.
3. Display histogram of all products and their quantities sold.

### What was done well

I think the creation of a usable data structure that can both be written to a file and printed to a console with relative ease was a strong part of this project.

### Where could improvements me made

There are some caveats of the current iteration of code, such as requiring a very specific input format, that the code does not error handle, and will run with undesireable outputs. Error handling in general throughout the code could be beefed up to handle invalid user and file input.

### Most challenging part

The most challenging part was definitely creating a working, well formatted, histogram to print to the console. As this involved string formatting in C++ to get the desired information from a file stream, a bit more brain power was needed. This was overcome by just figuring out a valid solution to the problem, googling how to parse input strings, and applying said Google-fu to the project at hand.

### Transferrable skills

I think the best takeaway from this project is handling input streams, such as from a file, and being able to generate a data structure that can be used in several different ways. I feel that most computer science related work will involve around a concept such as that.

### Code maintainence

Compartmentalizing code into relatively modular functions will make being able to maintain and add functionality trivial compared to programming it all in one monolithic structure. Solid commenting will also allow my future self, or others, to be able to visit the code and navigate it easily.
