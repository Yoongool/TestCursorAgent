"""
Circle Calculator

This module provides functionality to calculate the circumference and area
of a circle given its radius.
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


def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Args:
        radius (float): The radius of the circle
        
    Returns:
        float: The area of the circle
        
    Formula:
        area = π * radius²
    """
    # Use the formula: area = π * radius²
    # math.pi provides an accurate value of π
    area = math.pi * radius ** 2
    return area


def main():
    """
    Main function that demonstrates circle calculations with different radius values.
    
    This function calculates and prints both the circumference and area for various
    circle radii, showing how the calculate_circumference and calculate_area functions
    work with different inputs.
    """
    print("Circle Calculator")
    print("=" * 40)
    print()
    
    # Example 1: Small circle with radius 1
    radius1 = 1
    circumference1 = calculate_circumference(radius1)
    area1 = calculate_area(radius1)
    print(f"Radius: {radius1} units")
    print(f"Circumference: {circumference1:.2f} units")
    print(f"Area: {area1:.2f} square units")
    print()
    
    # Example 2: Medium circle with radius 5
    radius2 = 5
    circumference2 = calculate_circumference(radius2)
    area2 = calculate_area(radius2)
    print(f"Radius: {radius2} units")
    print(f"Circumference: {circumference2:.2f} units")
    print(f"Area: {area2:.2f} square units")
    print()
    
    # Example 3: Large circle with radius 10
    radius3 = 10
    circumference3 = calculate_circumference(radius3)
    area3 = calculate_area(radius3)
    print(f"Radius: {radius3} units")
    print(f"Circumference: {circumference3:.2f} units")
    print(f"Area: {area3:.2f} square units")
    print()
    
    # Example 4: Circle with decimal radius
    radius4 = 7.5
    circumference4 = calculate_circumference(radius4)
    area4 = calculate_area(radius4)
    print(f"Radius: {radius4} units")
    print(f"Circumference: {circumference4:.2f} units")
    print(f"Area: {area4:.2f} square units")
    print()


# Entry point: Run the main function when script is executed directly
if __name__ == "__main__":
    main()
