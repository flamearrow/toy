# To make sure that groceries can always be delivered, Instacart tries to equally distribute delivery requests throughout the day by including an additional delivery fee during busy periods.
#
# Each day is divided into several intervals that do not overlap and cover the whole day from 00:00 to 23:59. For each i the delivery fee in the intervals[i] equals fees[i].
#
# Given the list of delivery requests deliveries, your task is to check whether the delivery fee is directly correlated to the order volume in each interval i.e. the interval_fee / interval_deliveries value is constant for each interval throughout the day.
#
# Example
#
# For
# intervals = [0, 10, 22], fees = [1, 3, 1], and
#
# deliveries = [[8, 15],
#               [12, 21],
#               [15, 48],
#               [20, 17],
#               [23, 43]]
# the output should be
# solution(intervals, fees, deliveries) = true.
#
# The day is divided into 3 intervals:
#
# from 00:00 to 09:59, the first delivery was made, fees[0] / 1 = 1;
# from 10:00 to 21:59, the 2nd, 3rd and 4th deliveries were made, fees[1] / 3 = 1;
# from 22:00 to 23:59, the last delivery was made, fees[2] / 1 = 1.
# interval_fee / interval_deliveries = 1 for each interval, so the answer is true.
#
# Check out the image below for better understanding:
#
#
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [memory limit] 1 GB
#
# [input] array.integer intervals
#
# Each interval starts at xx:00 and ends at yy:59, where xx equals intervals[i] and yy equals intervals[i + 1] - 1, or 23 if intervals[i + 1] doesn't exist. intervals[i] represents the hour at which the ith interval starts. It is guaranteed that intervals[0] = 0.
#
# Guaranteed constraints:
# 1 ≤ intervals.length ≤ 24,
# 0 ≤ intervals[i] ≤ 23,
# intervals[0] = 0.
#
# [input] array.integer fees
#
# Array of non-negative integers of the same length as intervals. fees[i] is the delivery fee in the ith interval.
#
# Guaranteed constraints:
# fees.length = intervals.length,
# 0 ≤ fees[i] ≤ 105.
#
# [input] array.array.integer deliveries
#
# Deliveries in the order they were made. Each delivery is represented as the [h, m] array, h is the hour and m is the minute it was done. It is guaranteed that there were no deliveries at the same time.
#
# Guaranteed constraints:
# 1 ≤ deliveries.length ≤ 30,
# 0 ≤ deliveries[i][0] ≤ 23,
# 0 ≤ deliveries[i][1] ≤ 59.
#
# [output] boolean
#
# true if the delivery fee is directly correlated to the order volume in each interval, false otherwise.

def solution(intervals, fees, deliveries):
    avg_fee = -1
    for i in range(0, len(intervals)):
        start = 0 if i == 0 else intervals[i]
        end = 24 if i == (len(intervals) - 1) else intervals[i + 1]

        delivery_count = 0

        if not deliveries:  # if all popped up, then we ended with an additional interval that doesn't have any deliveries
            return avg_fee == -1

        while deliveries and deliveries[0][0] < end:
            delivery_count += 1
            deliveries.pop(0)

        if delivery_count > 0:
            new_avg_fee = fees[i] / delivery_count
            print("new avg fee:", new_avg_fee)
            if avg_fee < 0:
                avg_fee = new_avg_fee
            else:
                if new_avg_fee != avg_fee:
                    return False

    return True


if __name__ == '__main__':
    solution(
        [0, 10, 22],
        [1, 3, 1],
        [[8, 15],
         [12, 21],
         [15, 48],
         [20, 17]]
    )
