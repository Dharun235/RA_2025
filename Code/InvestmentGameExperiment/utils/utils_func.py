import numpy as np
import random
import math
import time
from datetime import datetime

# Function to generate a normal distribution of returns
def normal_random(investment):
    """ Function to generate a normal distribution of returns. 
    This function simulates a normal distribution of returns based on the investment amount."""
    # Define the range of possible return values
    max_return = 3 * (investment)
    min_return = 0
    
    # Define the midpoint of the range
    mid_point = (max_return) // 2
    
    # Set the standard deviation for the normal distribution - Standard deviation controls the spread. A smaller value gives a narrower peak, and a larger value gives a wider one.
    std_dev = max_return / 6  # This is a typical choice for normalization

    # Generate a random number from a normal distribution centered at mid_point
    value = np.random.normal(mid_point, std_dev)
    
    # Clip the value to ensure it's within the valid range [min_return, max_return]
    value = max(min_return, min(max_return, round(value)))
    
    return value

def timestamp():
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
