
# Experiment 4: Gradient Descent Algorithm
#
# Problem Statement:
# Implement Gradient Descent to find the minimum
# value of the function:
#
# f(x) = x^2 + 4x + 5
#
# The minimum point is x = -2.
# Minimum function value is f(-2) = 1.


# --------------------------------------------------
# Step 1: Define the Objective Function
# --------------------------------------------------

# Theory:
# An objective function is a mathematical function
# that we want to minimize or maximize.
#
# Here, we want to find the minimum value of:
#
# f(x) = x^2 + 4x + 5
#
# This is a quadratic function.

def f(x):
    return x**2 + 4*x + 5


# --------------------------------------------------
# Step 2: Calculate the Derivative
# --------------------------------------------------

# Theory:
# Derivative represents the rate of change of a function.
# It tells us the slope of the function at a given point.
#
# Given function:
# f(x) = x^2 + 4x + 5
#
# Differentiating:
#
# f'(x) = 2x + 4
#
# The derivative is used to determine
# the direction of movement towards the minimum.

def derivative(x):
    return 2*x + 4


# --------------------------------------------------
# Step 3: Input Initial Parameters
# --------------------------------------------------

# Initial x = Starting point of the algorithm.
# Learning Rate = Controls the step size.
# Iterations = Number of update steps.

x = float(input("Initial x: "))

learning_rate = float(
    input("Learning rate (e.g. 0.1): ")
)

iterations = int(
    input("Number of iterations: ")
)

''' Initial x: 10
Learning rate: 0.1
Number of iterations: 100'''

# --------------------------------------------------
# Step 4: Implement Gradient Descent
# --------------------------------------------------

# Theory:
# Gradient Descent is an optimization algorithm.
# It finds the minimum of a function by repeatedly
# updating the value of x in the opposite direction
# of the gradient (derivative).
#
# Gradient Descent Formula:
#
# x_new = x_old - learning_rate * f'(x)
#
# Where:
# x_old = Current value of x
# x_new = Updated value of x
# Learning Rate = Step size
# f'(x) = Derivative of the function
#
# For our function:
#
# x_new = x_old - learning_rate * (2*x_old + 4)
#
# The process continues until the required
# number of iterations is completed.

for i in range(iterations):

    # Update x using Gradient Descent formula
    x = x - learning_rate * derivative(x)

    # Display progress after regular intervals
    if i % max(1, iterations // 10) == 0:

        print(
            f"Iteration {i+1}: "
            f"x={x:.6f}, f(x)={f(x):.6f}"
        )


# --------------------------------------------------
# Step 5: Display Final Minimum Value
# --------------------------------------------------

# After completing all iterations,
# x approaches the minimum point.
#
# At minimum:
# f'(x) = 0
#
# 2x + 4 = 0
# 2x = -4
# x = -2
#
# Substituting x = -2:
#
# f(-2) = (-2)^2 + 4(-2) + 5
#       = 4 - 8 + 5
#       = 1

print("\nApproximate minimum:")
print(f"x = {x:.6f}")
print(f"f(x) = {f(x):.6f}")


# --------------------------------------------------
# Step 6: Final Result
# --------------------------------------------------

print("\nGradient Descent Completed Successfully!")
print("Expected minimum: x = -2")
print("Expected minimum value: f(x) = 1")
