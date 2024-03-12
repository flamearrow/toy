from datetime import datetime, timedelta


def solution(shoppers, orders, leadTime):
    windows = []
    for i in range(len(orders)):
        # order_start, order_end = orders[i]
        order_start = datetime.strptime(orders[i][0], "%H:%M")
        order_end = datetime.strptime(orders[i][1], "%H:%M")
        current_lead = int(leadTime[i])  # in minutes
        # left most possible window: (order_start, earliest_end)

        earliest_end = order_start + timedelta(minutes=current_lead)
        # right most possible window: (latest_start, order_end)
        latest_start = order_end - timedelta(minutes=current_lead)
        windows.append((earliest_end, latest_start, current_lead))
    return do_search(shoppers, windows)


def do_search(shoppers, windows):
    if not windows:
        return True
    else:
        for i in range(len(windows)):
            # (order_start, earliest_end), (latest_start, order_end), all in dateimte format
            current_pair = windows[i]
            # remove and return index
            index, shopper_start, shopper_end = find_valid_shopper(shoppers, current_pair)
            if index >= 0:  # find a shopper for windows[0], try use it and continue
                # remove and search
                removed_shopper = shoppers.pop(index)
                removed_window = windows.pop(i)
                # try search for windows-1 and shopper-1

                # if can exhaust, return True
                if do_search(shoppers, windows):
                    return True
                # cannot exhaust, add removed back and continue
                else:
                    shoppers.insert(index, removed_shopper)
                    windows.insert(i, removed_window)
                    # return False
            else:  # can't find a shopper for windows[0], not use it, try next
                continue
        return False


# shoppers: [["15:10", "16:00"], ["17:50", "22:30"], ["13:00", "14:40"]]
# current_pari: (order_start, earliest_end), (latest_start, order_end)
def find_valid_shopper(shoppers, current_pair):
    (earliest_end, latest_start, current_lead) = current_pair
    print("comparing current_pair:")
    print("earliest_end", earliest_end.time())
    print("latest_start", latest_start.time())
    print("current_lead", current_lead) # in minutes

    for i in range(len(shoppers)):
        # shopper_start, shopper_end = shoppers[i]
        shopper_start = datetime.strptime(shoppers[i][0], "%H:%M")
        shopper_end = datetime.strptime(shoppers[i][1], "%H:%M")
        shopper_range = (shopper_end - shopper_start).seconds / 60
        if shopper_range >= current_lead and shopper_start <= latest_start and shopper_end >= earliest_end:
            return i, shopper_start, shopper_end
        else:
            continue
    return -1, -1, -1


if __name__ == '__main__':
    ret = solution([["15:10","16:00"], ["17:40","22:30"]], [["17:30","18:00"], ["15:00","15:45"]], [15, 30])
    # ret = solution(
    #     [["15:10", "16:00"], ["17:50", "22:30"], ["13:00", "14:40"]],
    #     [["14:30", "15:00"]],
    #     [15]
    # )
    print(ret)
