"""
Geometry Calculator and Utilities

This module provides functionality to calculate the circumference and area
of a circle given its radius, the area of a square given its side length,
and to find the maximum value in a list.
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


def calculate_square_area(side_length):
    """
    Calculate the area of a square given its side length.
    
    Args:
        side_length (float): The side length of the square
        
    Returns:
        float: The area of the square
        
    Formula:
        area = side_length²
    """
    # Use the formula: area = side_length²
    area = side_length ** 2
    return area


def get_max_value(numbers):
    """
    Find the maximum value in a list of numbers.
    
    Args:
        numbers (list): A list of numbers (int or float)
        
    Returns:
        int or float: The maximum value in the list
        
    Raises:
        ValueError: If the list is empty
    """
    # Check if the list is empty
    if not numbers:
        raise ValueError("Cannot find maximum value of an empty list")
    
    # Use Python's built-in max() function to find the maximum value
    max_value = max(numbers)
    return max_value


def main():
    """
    Main function that demonstrates geometry calculations and utility functions.
    
    This function calculates and prints the circumference and area for various
    circles, the area for various squares, and demonstrates finding maximum values
    in lists.
    """
    print("Geometry Calculator and Utilities")
    print("=" * 40)
    print()
    
    print("CIRCLE CALCULATIONS:")
    print("-" * 40)
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
    
    print("SQUARE CALCULATIONS:")
    print("-" * 40)
    print()
    
    # Example 1: Small square with side length 3
    side1 = 3
    square_area1 = calculate_square_area(side1)
    print(f"Side length: {side1} units")
    print(f"Area: {square_area1:.2f} square units")
    print()
    
    # Example 2: Medium square with side length 8
    side2 = 8
    square_area2 = calculate_square_area(side2)
    print(f"Side length: {side2} units")
    print(f"Area: {square_area2:.2f} square units")
    print()
    
    # Example 3: Large square with side length 15
    side3 = 15
    square_area3 = calculate_square_area(side3)
    print(f"Side length: {side3} units")
    print(f"Area: {square_area3:.2f} square units")
    print()
    
    print("LIST MAXIMUM VALUE:")
    print("-" * 40)
    print()
    
    # Example 1: List of integers
    list1 = [10, 45, 23, 89, 12, 67]
    max1 = get_max_value(list1)
    print(f"List: {list1}")
    print(f"Maximum value: {max1}")
    print()
    
    # Example 2: List of floats
    list2 = [3.14, 2.71, 9.81, 1.41, 6.28]
    max2 = get_max_value(list2)
    print(f"List: {list2}")
    print(f"Maximum value: {max2}")
    print()
    
    # Example 3: Mixed positive and negative numbers
    list3 = [-15, 8, -3, 22, -40, 5]
    max3 = get_max_value(list3)
    print(f"List: {list3}")
    print(f"Maximum value: {max3}")
    print()


# Entry point: Run the main function when script is executed directly
if __name__ == "__main__":
    main()
