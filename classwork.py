class Mathematics:
    def addition(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        return x / y

    def exponentiation(self, x, y):
        return x ** y


class Physics:
    def velocity(self, distance, time):
        return distance / time

    def acceleration(self, initial_velocity, final_velocity, time):
        return (final_velocity - initial_velocity) / time

    def force(self, mass, acceleration):
        return mass * acceleration

    def momentum(self, mass, velocity):
        return mass * velocity

    def work(self, force, distance):
        return force * distance


mathematics = Mathematics()
physics = Physics()

category = input("Which subject would you like to calculate - Mathematics or Physics? ")
operation = input("Which operation would you like to perform? ")

if category.lower() == "mathematics":
    if operation.lower() == "addition":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = mathematics.addition(a, b)
        print("Result:", result)

    elif operation.lower() == "subtraction":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = mathematics.subtraction(a, b)
        print("Result:", result)

    elif operation.lower() == "multiplication":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = mathematics.multiplication(a, b)
        print("Result:", result)

    elif operation.lower() == "division":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = mathematics.division(a, b)
        print("Result:", result)

    elif operation.lower() == "exponentiation":
        a = float(input("Enter base number: "))
        b = float(input("Enter exponent: "))
        result = mathematics.exponentiation(a, b)
        print("Result:", result)

    else:
        print("Invalid operation selected.")

elif category.lower() == "physics":
    if operation.lower() == "velocity":
        distance = float(input("Enter distance: "))
        time = float(input("Enter time: "))
        result = physics.velocity(distance, time)
        print("Result:", result)

    elif operation.lower() == "acceleration":
        initial_velocity = float(input("Enter initial velocity: "))
        final_velocity = float(input("Enter final velocity: "))
        time = float(input("Enter time: "))
        result = physics.acceleration(initial_velocity, final_velocity, time)
        print("Result:", result)

    elif operation.lower() == "force":
        mass = float(input("Enter mass: "))
        acceleration = float(input("Enter acceleration: "))
        result = physics.force(mass, acceleration)
        print("Result:", result)

    elif operation.lower() == "momentum":
        mass = float(input("Enter mass: "))
        velocity = float(input("Enter velocity: "))
        result = physics.momentum(mass, velocity)
        print("Result:", result)

    elif operation.lower() == "work":
        force = float(input("Enter force: "))
        distance = float(input("Enter distance: "))
        result = physics.work(force, distance)
        print("Result:", result)

    else:
        print("Invalid selection.")

else:
    print("Invalid category selection.")