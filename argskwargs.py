#!/usr/local/bin/python3

# function for args

def args_explain(*args, **kwargs):
    print("Results for args:\n", args)

# function for kwargs

def kwargs_explain(*args, **kwargs):
    print("Result for kwargs:", kwargs)
    print("Fetching the first argument:", kwargs.get('natural_num'))
    print("Fetching the second argument:", kwargs.get('even_num'))

# calculating the list for n natural numbers

natural_num_list = list()
for num in range(10):
    natural_num_list.append(num)

# calculating list for n even numbers
even_num_list = list()
for num in range(10):
    if num%2 == 0:
        even_num_list.append(num)

# executing the main program
if __name__ == '__main__':
    args_explain(natural_num_list, even_num_list)
    kwargs_explain(natural_num=natural_num_list, even_num=even_num_list)
