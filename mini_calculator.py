class Calculator:
    def __init__(self):
        self.operator = None
        self.numbers = []

    def select_operator(self):
        print(
            "What kind of calculation do you want to perform?\n"
            "Press 1 for Addition\n"
            "Press 2 for Subtraction\n"
            "Press 3 for Multiplication\n"
            "Press 4 for Division"
        )
        try:
            self.operator = int(input("Enter the operator number: "))
            if self.operator not in {1, 2, 3, 4}:
                raise ValueError("Invalid operator selected!")
        except ValueError as e:
            print(f"Error: {e}")
            self.operator = None
            self.select_operator()

    def get_ordinal_suffix(self, n):
        if 11 <= n % 100 <= 13:
            return "th"
        elif n % 10 == 1:
            return "st"
        elif n % 10 == 2:
            return "nd"
        elif n % 10 == 3:
            return "rd"
        else:
            return "th"

    def get_numbers(self):
        try:
            total_numbers = int(input("How many numbers do you want to calculate? "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            return self.get_numbers()

        self.numbers = []
        for N in range(1, total_numbers + 1):
            while True:
                try:
                    num = float(
                        input(f"Enter the {N}{self.get_ordinal_suffix(N)} number: ")
                    )
                    self.numbers.append(num)
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid number.")

    def perform_calculation(self):
        if len(self.numbers) < 2:
            print("You need at least two numbers to perform a calculation.")
            return

        result = self.numbers[0]
        for num in self.numbers[1:]:
            if self.operator == 1:
                result += num
            elif self.operator == 2:
                result -= num
            elif self.operator == 3:
                result *= num
            elif self.operator == 4:
                if num == 0:
                    print("Error: Division by zero is not allowed!")
                    return
                result /= num

        print(f"Result: {result}")

    def check_operator(self):
        operators = {1: "+", 2: "-", 3: "*", 4: "/"}
        return operators.get(self.operator, None)

    def run(self):
        self.select_operator()
        if self.operator:
            self.get_numbers()
            self.perform_calculation()


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
