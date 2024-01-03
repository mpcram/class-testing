# python file to test classes

def main():
    John = Person("John", 50)

    John.age = 69

    John.personfunction()
    print(John)

class Person:
    def __init__(var_1, name : str, age : int):
        var_1.name = name
        var_1.age  = age

    def __str__(var_2):
        return f"{var_2.name}({var_2.age})"
    
    def personfunction(var_3):
        print(var_3.name + " is an idiot.")
    

# run code after initialising fucnitons
if __name__ == "__main__":
    main()