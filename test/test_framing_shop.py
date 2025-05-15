import pytest
from app.framing_shop import calculate_framing_price

class TestFramingShop():

    #
    # Positive testing
    #

    @pytest.mark.parametrize('width, height, price', [
        
        # Width
        (30, 45, 3000),         # Width valid partition: lower boundary value with height valid partition middle value
        (31, 45, 3000),
        (70, 45, 3500),         # 3150 cm2 exceeds 1600 cm2
        (99, 45, 3500),
        (100, 45, 3500),        # Width valid partition: upper boundary value with height valid partition middle value
        
        # Height
        (70, 30, 3500),         # Height valid partition: lower boundary value with width valid partition middle value. 2100 cm2 exceeds 1600 cm2
        (70, 31, 3500),
        # (70, 45, 3500),       # This test case was already defined when addressing the width
        (70, 59, 3500),
        (70, 60, 3500),         # Height valid partition: upper boundary value with width valid partition middle value

        # Area
        (39, 41, 3000),         
        (40, 40, 3000),         # Partition 0-1600: upper boundary value
        (50, 50, 3500)

        # The lower boundary value for the area partitions 0-1600 and 1601-MAX INTEGER cannot be tested,
        # as the width and height values that produce said areas are out of range
    ])
    def test_framing_shop_passes(self, width, height, price):
        assert calculate_framing_price(width, height) == price

    #
    # Negative testing
    #

    # Width
    @pytest.mark.parametrize('width, height', [

        # Invalid partition 0-29
        (0, 45),        # Lower boundary value
        (1, 45),
        (28, 45),
        (29, 45),       # Upper boundary value

        # Invalid partition 101-MAX INTEGER
        (101, 45),      # Lower boundary value
        (102, 45),
        (180, 45)
    ])
    def test_framing_shop_fails(self, width, height):
        with pytest.raises(ValueError) as error_info:
            calculate_framing_price(width, height)
        assert str(error_info.value) == 'Width must be between 30 cm and 100 cm.'
    
    # Height
    @pytest.mark.parametrize('width, height', [

        # Invalid partition 0-29
        (70, 0),        # Lower boundary value
        (70, 1),
        (70, 28),
        (70, 29),       # Upper boundary value

        # Invalid partition 61-MAX INTEGER
        (70, 61),       # Lower boundary value
        (70, 62),
        (70, 95)
    ])
    def test_framing_shop_fails(self, width, height):
        with pytest.raises(ValueError) as error_info:
            calculate_framing_price(width, height)
        assert str(error_info.value) == 'Height must be between 30 cm and 60 cm.'