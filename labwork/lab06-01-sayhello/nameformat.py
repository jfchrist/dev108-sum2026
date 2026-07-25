# This is where you will code your three functions 
# Be sure to write documentation for this module. Refer to your book chapter for instructions on how to do this.

# sayHello() ex: Hello Tony!
def sayHello(firstName):
    """Program will greet the user using only their first name"""
    print(f"Hello, {firstName}!")


# fullName() ex: Tony Stark
def fullName(firstName, lastName):
    """Program will print user's full name using provided inputs"""
    print(firstName,lastName)


# lastNameFirst() ex: Stark, Tony
def lastNameFirst(lastName, firstName):
    """Program will output user's full name in following format: last name, first name"""
    print(f"{lastName}, {firstName}")