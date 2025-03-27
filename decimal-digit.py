# 8.	Decimal Digit Transformation
# Write a function in an Object Orientated Programming language of your choice that, when passed a decimal digit X, calculates and returns the value of X + XX + XXX + XXXX. For example, if X is 3, the function should return 3702 (3 + 33 + 333 + 3333). Ensure the function handles valid inputs and provides meaningful error messages for invalid inputs.

class DecimalDigitTransformation:
    def __init__(self, X):
        self.X = X

    def calculate_transformation(self):

        #Calculate and return the value of X + XX + XXX + XXXX.

        result = self.X + int(f"{self.X}{self.X}") + int(f"{self.X}{self.X}{self.X}") + int(f"{self.X}{self.X}{self.X}{self.X}")
        return result

def get_user_input():

    # Get user input and ensure it is a single decimal digit (0-9).
    while True:
        try:
            X = int(input("Enter a single decimal digit (0-9): "))
            if 0 <= X <= 9:
                return X
            else:
                print("Invalid input. Please enter a single decimal digit (0-9).")
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    # Get user input
    X = get_user_input()
    
    # Create an instance of DecimalDigitTransformation
    transformation = DecimalDigitTransformation(X)
    
    # Calculate the transformation
    result = transformation.calculate_transformation()
    
    # Print the result
    print(f"The result of the transformation for {X} is: {result}")