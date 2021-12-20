#Font: https://www.datacamp.com/community/tutorials/decorators-python?utm_source=adwords_ppc&utm_medium=cpc&utm_campaignid=14989519638&utm_adgroupid=127836677279&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=278443377095&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=1001773&gclid=Cj0KCQiAweaNBhDEARIsAJ5hwberNxp0l51SwegvNP98usSrL9hHKYbXhUp80KCnGRStJeaLfQMjovQaAnkJEALw_wcB

print("#Decorators")
print()

print("#Assigning Functions to Variables")

def plus_one(number):
    return number + 1;
    
add_one = plus_one
print(add_one(5))

print()

print("#Defining Functions Inside other Functions")

def plus_one(number):
    def add_one(number):
        return number + 1
    
    result = add_one(number)
    return result

print(plus_one(4))

print()

print("#Passing Functions as Arguments to other Functions")

def plus_one(number):
    return number + 1
    
def function_call(function):
    number_to_add = 8
    return function(number_to_add)

print(function_call(plus_one))

print()

print("#Functions Returning other Functions")

def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
    
hello = hello_function()
print(hello())

print()

print("#Nested Functions have access to the Enclosing Function's Variable Scope")

def print_message(message):
    "Enclosing Function"
    def message_sender():
        "Nested Function"
        print(message)
        
    message_sender()

print_message("Some random message")

print()

print("#Creating Decorators")

def uppercase_decorator(function):
    
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
        
    return wrapper
     
def say_hi():
    return 'hello there'
    
decorate = uppercase_decorator(say_hi)

print(decorate())

print()

print("#Creating Decorators (using notation)")

@uppercase_decorator
def say_hi2():
    return 'hello there (with notation)'

print(say_hi2())

print()

print("#Applyin Multiple Decorators to a Single Function")

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
        
    return wrapper

@split_string
@uppercase_decorator
def say_hi3():
    return 'hello there'
    
print(say_hi3())
print()


print("#Accepting Arguments in Decorator Functions")

def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1,arg2)
    return wrapper_accepting_arguments

@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Nairobi", "Accra")

print()


print("#Accepting Arguments in Decorator Functions")

def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments
    
@a_decorator_passing_arbitrary_arguments
def function_with_no_argument(a,b,c):
    print("No arguments here.")
    
function_with_no_argument(1,2,3)

@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments():
    print("This has shown keyword arguments")

function_with_keyword_arguments(first_name="Anderson", last_name="Martins")

print()


print("#Passing Arguments to the Decorator")

def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3):
            "This is the wrapper function"
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2, decorator_arg3,
                          function_arg1, function_arg2, function_arg3))
            return func(function_arg1, function_arg2, function_arg3)
            
        return wrapper
        
    return decorator
    
pandas = "Pandas"
@decorator_maker_with_arguments(pandas, "Numpy", "Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2, function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
          " {1}" " {2}".format(function_arg1, function_arg2, function_arg3))

decorated_function_with_arguments(pandas, "Science", "Tools")         

print()
