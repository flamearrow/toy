#https://app.codesignal.com/company-challenges/instacart/xrpDSPv7GzBXB6Mpd
# Instacart customers are able to set the delivery window during which they want to receive their groceries. There are always plenty of shoppers in the area ready to take a customer's order, but unfortunately they can't always do it right away. Before taking an order a shopper wants to ensure they will make it in time. They also don't want to stay idle, so arriving early isn't an option either.
#
# Our task is to implement an algorithm that determines whether shoppers should take the given order or not.
#
# For each shopper you know their travel speed, distance to the store and the estimated amount of time they will spend there. Figure out which of them can take the order, assuming it is known when the customer wants to receive the groceries and the distance between their house and the store.
#
# Example
#
# For order = [200, 20, 15] and shoppers = [[300, 40, 5], [600, 40, 10]], the output should be
#
# solution(order, shoppers) = [false, true].
#
# The store is located 200 m away from the customer's house.
#
# The customer will be ready to receive the groceries in 20 minutes, but they shouldn't be delivered more than 15 minutes late.
#
# The first shopper is 300 m away from the store, his speed is 40 m/min, and he will spend 5 minutes in the store, which means that he will need (300 + 200) / 40 + 5 = 17.5 minutes to fulfill the order. This will leave him with 20 - 17.5 = 2.5 idle minutes, so he shouldn't take the order.
#
# The second shopper is 600 m away from the store, his speed is 40 m/min, and he will spend 10 minutes in the store, which means it will take him (600 + 200) / 40 + 10 = 30 minutes to fulfill the order. The customer can wait for 20 + 15 = 35 minutes, which means that the shopper will make it in time.
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [memory limit] 1 GB
#
# [input] array.integer order
#
# The order is given as an array of 3 positive integers. order[0] is the distance from the customer's home to the store in meters, order[1] is the time by which the customer will be ready to receive the delivery in minutes, and order[2] is the number of minutes they are willing to wait.
#
# Guaranteed constraints:
# order.length = 3,
# 1 ≤ order[i] ≤ 1000.
#
# [input] array.array.integer shoppers
#
# Each element of this array represents a shopper. For each shopper three positive integers are stored in the exact given order: their distance from the shop in meters, their speed in meters per minute and the estimated time they will spend in the store in minutes.
#
# Guaranteed constraints:
# 1 ≤ shoppers.length ≤ 5,
# shoppers[i].length = 3,
# 1 ≤ shoppers[i][j] ≤ 1000.
#
# [output] array.boolean
#
# For each shopper return if they should take the order or not.

def solution(order, shoppers):
    ret = []
    m_distance, ready_time, max_late = order
    for s_distance, speed, wait_time in shoppers:
        time_needed = (m_distance + s_distance) / speed + wait_time
        time_left = ready_time - time_needed
        print("time_left: ", time_left)
        if time_left > 0:  # has idle time, can't take
            ret.append(False)
        else:
            time_over = abs(time_left)
            ret.append(time_over <= max_late)
    return ret

