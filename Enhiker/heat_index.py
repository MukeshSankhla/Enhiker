def calculate_heat_index(temperature, humidity):
    # Constants for the heat index formula, based on the Rothfusz regression.
    c1 = -8.78469475556
    c2 = 1.61139411
    c3 = 2.33854883889
    c4 = -0.14611605
    c5 = -0.012308094
    c6 = -0.0164248277778
    c7 = 0.002211732
    c8 = 0.00072546
    c9 = -0.000003582

    # Assign temperature and humidity to more readable variables
    T = temperature  # Temperature in degrees Celsius
    R = humidity     # Relative humidity in percentage

    # Calculate the heat index using the formula.
    # The formula is a polynomial regression that estimates the apparent temperature 
    # (what humans perceive as the temperature) based on the actual temperature and humidity.
    heat_index = (
        c1 + 
        (c2 * T) + 
        (c3 * R) + 
        (c4 * T * R) + 
        (c5 * T**2) + 
        (c6 * R**2) + 
        (c7 * T**2 * R) + 
        (c8 * T * R**2) + 
        (c9 * T**2 * R**2)
    )

    # Return the heat index value rounded to two decimal places.
    return round(heat_index, 2)
