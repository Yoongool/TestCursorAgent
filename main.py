"""
Circle Circumference Calculator

This module provides functionality to calculate the circumference of a circle
given its radius.
"""

import math


def calculate_circumference(radius):
    """
    Calculate the circumference of a circle given its radius.
    
    Args:
        radius (float): The radius of the circle
        
    Returns:
        float: The circumference of the circle
        
    Formula:
        circumference = 2 * π * radius
    """
    # Use the formula: circumference = 2 * π * radius
    # math.pi provides an accurate value of π
    circumference = 2 * math.pi * radius
    return circumference


def main():
    """
    Main function that demonstrates the circumference calculation with different radius values.
    
    This function calculates and prints the circumference for various circle radii,
    showing how the calculate_circumference function works with different inputs.
    """
    print("Circle Circumference Calculator")
    print("=" * 40)
    print()
    
    # Example 1: Small circle with radius 1
    radius1 = 1
    circumference1 = calculate_circumference(radius1)
    print(f"Radius: {radius1} units")
    print(f"Circumference: {circumference1:.2f} units")
    print()
    
    # Example 2: Medium circle with radius 5
    radius2 = 5
    circumference2 = calculate_circumference(radius2)
    print(f"Radius: {radius2} units")
    print(f"Circumference: {circumference2:.2f} units")
    print()
    
    # Example 3: Large circle with radius 10
    radius3 = 10
    circumference3 = calculate_circumference(radius3)
    print(f"Radius: {radius3} units")
    print(f"Circumference: {circumference3:.2f} units")
    print()
    
    # Example 4: Circle with decimal radius
    radius4 = 7.5
    circumference4 = calculate_circumference(radius4)
    print(f"Radius: {radius4} units")
    print(f"Circumference: {circumference4:.2f} units")
    print()


# Entry point: Run the main function when script is executed directly
if __name__ == "__main__":
    main()
