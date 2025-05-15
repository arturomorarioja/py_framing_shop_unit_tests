# Price calculation of picture framing based on width and height of the picture (in centimeters). 
# - The valid width of the picture is between 30 and 100 cm inclusive. 
# - The valid height of the picture is between 30 and 60 cm inclusive. 
# The system calculates the area of the image as the product of width and height. 
# - If the surface area exceeds 1600 cm2, the framing price is 3500 kr. 
# - Otherwise, the framing price is 3000 kr.
def calculate_framing_price(width, height):
    if not 30 <= width <= 100:
        raise ValueError('Width must be between 30 cm and 100 cm.')
    if not 30 <= height <= 60:
        raise ValueError('Height must be between 30 cm and 60 cm.')
    
    if width * height > 1600:
        return 3500
    return 3000