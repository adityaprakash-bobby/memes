import math

horizontal = "_________"

vertical_sep = "|"

horizontal_sep = "_"

def find_max_length(arr):

    cur_len = 0
    max_len = 0

    for i in range(0,arr.__len__()):

        if arr[i] == 2:
            cur_len = 0
            
        else:
            cur_len += 1
            max_len = max(cur_len,max_len)

    return (max_len + 1)

def draw_diag(stack):
    print(vertical_sep, end="")
    max_len = find_max_length(stack)
    ctr = 0
    for i in stack:
        if i == 1:
            ctr += 1
        else:
            ctr += 1
            extra_segment = max_len - ctr 
            for i in range(0, ctr):
                print(horizontal + ((extra_segment*horizontal)[:math.ceil((extra_segment*horizontal).__len__() / ctr)]) + vertical_sep, end="")
            print("\n" + vertical_sep, end="")
            ctr = 0
    ctr += 1
    extra_segment = max_len - ctr 
    for i in range(0, ctr):
        print(horizontal + ((extra_segment*horizontal)[:math.ceil((extra_segment*horizontal).__len__() / ctr ) + 1 ]) + vertical_sep, end="")
    # print("\n" + vertical_sep, end="")
        # if i == 1:
        #     print(horizontal + ((2*horizontal)[:(2*horizontal).__len__() // 3]) + vertical_sep, end="")
        # if i == 2:
        #     print("\n" + vertical_sep + horizontal + vertical_sep, end="")
    # print(horizontal + vertical_sep, end="")
    print("\n")
stack = [1,1,2,2,1,1,1]

# find_max_length(stack)
draw_diag(stack)


# print(horizontal[:horizontal.__len__() // 2])

