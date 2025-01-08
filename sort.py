arr =  [1,3,2,0,7,8,6]


def sort(arr):
    s_arr = arr.copy()
    for i in range(0, len(s_arr)):


        for j in range( i+1,len(s_arr)):

            if(s_arr[i]>s_arr[j]):

                c = s_arr[i]
                s_arr[i] = s_arr[j]
                s_arr[j] = c

    return s_arr

sorted_arr =  sort(arr)

print(arr)
print(sorted_arr)