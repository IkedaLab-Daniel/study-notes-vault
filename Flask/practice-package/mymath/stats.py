def mean(numbers):
    """
    This function returns the mean of the given list of numbers.
    The mean is calculated as the sum of all numbers divided by the count of numbers.
    """
    # Calculate the mean by summing all the numbers and dividing by the length of the list.
    # 'sum(numbers)' computes the total of all numbers in the list.
    # 'len(numbers)' gives the count of numbers in the list.
    # The mean (or average) is the total sum divided by the number of elements.
    return sum(numbers) / len(numbers)  # Return the mean value.

def median(numbers):
    """
    This function returns the median of the given list of numbers.
    The median is the middle value when the numbers are sorted.
    If there is an even number of observations, it returns the average of the two middle numbers.
    """
    # Sort the list of numbers in ascending order.
    # Sorting is necessary to find the median, as the median depends on the order of values.
    numbers.sort()

    # Check if the number of elements in the list is even.
    # len(numbers) % 2 == 0 evaluates to True if the list has an even number of elements.
    if len(numbers) % 2 == 0:
        # If the list has an even number of elements, find the two middle numbers.
        # 'len(numbers) // 2' computes the index of the second middle element in a zero-indexed list.
        # 'len(numbers) // 2 - 1' computes the index of the first middle element.
        median1 = numbers[len(numbers) // 2]  # The higher index of the two middle values.
        median2 = numbers[len(numbers) // 2 - 1]  # The lower index of the two middle values.
        
        # Calculate the median by taking the average of the two middle numbers.
        # This is done by adding the two middle values and dividing by 2.
        mymedian = (median1 + median2) / 2  # Average of the two middle values.
    else:
        # If the list has an odd number of elements, return the middle number.
        # 'len(numbers) // 2' computes the index of the middle element.
        mymedian = numbers[len(numbers) // 2]  # The middle value for lists with an odd number of elements.

    # Return the calculated median value.
    return mymedian