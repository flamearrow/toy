# As part of an Instacart beta testing group, Sara is trying out a brand new feature that automatically estimates the combined cost of the items in her handwritten shopping list. Her list contains both items and their prices. All Sara has to do is snap a photo of her list with the Instacart app, and she gets a quick estimate of what everything will cost.
#
# Sara asked for your help, so it is up to you to devise an algorithm that calculates the cost after the image is converted into plain text. All you need to do is extract all numbers from the given string items and sum them up.
#
# Example
#
# For items = "Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4", the output should be
# solution(items) = 7.48;
# For items = "blue suit for 24$, cape for 12.99$ & glasses for 15.70", the output should be
# solution(items) = 52.69.
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [memory limit] 1 GB
#
# [input] string items
#
# A shopping list given as a string. It is guaranteed that the only numbers in it are dollar prices for different items.
# Note that although each price is given in dollars, you do not know their exact form. Each of them can either be an integer, or a decimal number with one or two decimal places and it may or may not be followed by a dollar sign.
# However, you may assume that if there is a period ('.') between two digits, then it's a decimal mark.
#
# Guaranteed constraints:
# 0 ≤ items.length ≤ 6 · 104.
#
# [output] float
#
# The total cost of all items.

def solution(items):
    start = -1
    on = False
    point_seen = False
    result = 0
    for current in range(len(items)):
        current_char = items[current]
        if is_valid(current_char):
            if ord('.') == ord(current_char):
                if point_seen:  # reset
                    on = False
                    point_seen = False
                    continue
                else:  # not seen point
                    if not on:  # first match is a point, invalid
                        continue
                    else:  # saw number, then point
                        point_seen = True
            else:
                if not on:
                    on = True
                    start = current
        else:
            if on:
                on = False
                point_seen = False
                result += parse(items, start, current - 1)

    if on:
        result += parse(items, start, len(items) - 1)
    return result


def is_valid(char):
    ascii_value = ord(char)
    return ascii_value == ord('.') or (ascii_value >= ord('0') and ascii_value <= ord('9'))


def parse(items, start, end_inclusive):
    print("parsing", items[start:end_inclusive + 1])
    return float(items[start:end_inclusive + 1])

