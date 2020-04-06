
def merge_ranges(l):
    l = sorted(l)
    consolidated = []
    new_mtg = l[0]

    for mtg in l:
        start = mtg[0]
        end = mtg[1]

        if start > new_mtg[1]:
            consolidated.append(new_mtg)
            new_mtg = (start, end)
        elif end <= new_mtg[0]:
            new_mtg = (start, new_mtg[1])
        elif start >= new_mtg[0] and end <= new_mtg[1]:
            continue
        else:
            new_mtg = (new_mtg[0], end)
    consolidated.append(new_mtg)
    return consolidated


def reverse(list_of_chars, front, end):
    # Reverse the input list of chars in place
    while front < end:
        temp = list_of_chars[front]
        list_of_chars[front], list_of_chars[end] = list_of_chars[end], temp
        front += 1
        end -= 1


def reverse_words(message):
    reverse(message, 0, len(message)-1)
    current = 0
    for i in range(len(message) + 1):
        if i == len(message) or message[i] == ' ':
            reverse(message, current, i - 1)
            current = i + 1


def merge_lists(my_list, alices_list):
    # Combine the sorted lists into one large sorted list
    my_index = 0
    alice_index = 0
    merged_list = []

    while my_index < len(my_list) and alice_index < len(alices_list):
        if my_list[my_index] < alices_list[alice_index]:
            merged_list.append(my_list[my_index])
            my_index += 1
        else:
            merged_list.append(alices_list[alice_index])
            alice_index += 1

    while my_index < len(my_list):
        merged_list.append(my_list[my_index])
        my_index += 1

    while alice_index < len(alices_list):
        merged_list.append(alices_list[alice_index])
        alice_index += 1

    return merged_list


def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    # Check if we're serving orders first-come, first-served
    take_index = 0
    dine_index = 0
    served_index = 0
    served_len = len(served_orders)

    if not take_out_orders or not dine_in_orders:
        return True
    elif served_len != len(take_out_orders) + len(dine_in_orders):
        return False

    while served_index < served_len:
        if take_index < len(take_out_orders) and take_out_orders[take_index] == \
                served_orders[served_index]:
            take_index += 1
        elif dine_index < len(dine_in_orders) and dine_in_orders[dine_index] == \
                served_orders[served_index]:
            dine_index += 1
        else:
            return False
        served_index += 1
    return True

#
# m = [ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e',
#       'a', 'l' ]
# m = [ 'c', 'a', 'k', 'e', ' ',
#             'p', 'o', 'u', 'n', 'd', ' ',
#             's', 't', 'e', 'a', 'l' ]
# reverse_words(m)
# print(m)
# print(''.join(m))
