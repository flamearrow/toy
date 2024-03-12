# https://app.codesignal.com/company-challenges/instacart/NTEbfWAkqNnoHJGcF
# The FDA recommends that for a healthy, balanced diet, a person on average needs around 2,000 Kcal a day to maintain their weight. As a result, Instacart is set to release a new feature that will help customers control their daily intake of calories. Given a list of items in a customer's cart, it will show the items that can be consumed in one day such that their total caloric value is as close to 2000 as possible.
#
# Knowing the caloricValue of each bought item, return the 0-based indices of the items to be consumed in one day. If there is more than one option, return the lexicographically smallest one.
#
# Example
#
# For caloricValue = [400, 800, 400, 500, 350, 350], the output should be
# solution(caloricValue) = [0, 2, 3, 4, 5].
#
# Caloric value of items [1, 3, 4, 5] and [0, 2, 3, 4, 5] both sum up to 2000 but since [0, 2, 3, 4, 5] is lexicographically smaller than [1, 3, 4, 5], the answer is [0, 2, 3, 4, 5].
#
# For caloricValue = [150, 900, 1000], the output should be
# solution(caloricValue) = [0, 1, 2].
#
# The total sum of all items (i.e. 2050) is 50 Kcal larger than 2000, so the answer is [0, 1, 2].
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [memory limit] 1 GB
#
# [input] array.integer caloricValue
#
# Caloric value of each item in the cart. The total sum of all items is not greater than 104.
#
# Guaranteed constraints:
# 1 ≤ caloricValue.length ≤ 30,
# 2 ≤ caloricValue[i] ≤ 104.
#
# [output] array.integer
#
# The items to consume in a day.


def solution(caloricValue):
    calculatedResults = {}
    residue, indices = do_calculate(caloricValue, 0, 2000, calculatedResults)
    return indices


# return residue, [indices]
def do_calculate(caloricValue, currentIndex, targetValue, calculatedResults):
    buffered_result = calculatedResults.get(
        (targetValue, currentIndex))  # use targetValue, currentIndex as a composite key
    if buffered_result is not None:
        return buffered_result['residue'], buffered_result['indices']
    if targetValue <= 0:  # don't take anymore
        return targetValue, []
    elif currentIndex == len(caloricValue) - 1:
        resultWithCurrent = abs(targetValue - caloricValue[currentIndex])
        resultWithoutCurrent = targetValue
        if resultWithCurrent < resultWithoutCurrent:  # chose the smaller one
            calculatedResults[(targetValue, currentIndex)] = {'residue': resultWithCurrent, 'indices': [currentIndex]}
            return resultWithCurrent, [currentIndex]
        else:
            calculatedResults[(targetValue, currentIndex)] = {'residue': resultWithoutCurrent, 'indices': []}
            return resultWithoutCurrent, []
    else:
        residue_with_current, indices_with_current = do_calculate(caloricValue, currentIndex + 1,
                                                                  targetValue - caloricValue[currentIndex],
                                                                  calculatedResults)
        residue_without_current, indices_without_current = do_calculate(caloricValue, currentIndex + 1, targetValue,
                                                                        calculatedResults)
        # chose the smaller residue
        if abs(residue_with_current) <= abs(residue_without_current):
            indices_with_current.insert(0, currentIndex)
            calculatedResults[(targetValue, currentIndex)] = {'residue': residue_with_current,
                                                              'indices': [indices_with_current]}
            return residue_with_current, indices_with_current
        else:
            calculatedResults[(targetValue, currentIndex)] = {'residue': residue_without_current,
                                                              'indices': [indices_without_current]}
            return residue_without_current, indices_without_current

