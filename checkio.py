def create_intervals(data):
    data=sorted(list(data))
    intervals=[]  #intervaly
    temp=[]       #temp group of nums
    group=[]      #postupkove

    for i in range(len(data)):
        cur_num=data[i]
        if i==0 or cur_num -1!=data[i-1]:
            if len(group)>0:
                temp.append(group[0]),temp.append(group[-1]),intervals.append(tuple(temp))
                temp=[]
                group=[]
        group.append(cur_num)

    if len(group)>0:
        temp.append(group[0]),temp.append(group[-1]), intervals.append(tuple(temp))
    return intervals

nums1={1,2,3,4,5,7,8,12,9}
nums2={1,2,3,7,8,15,25,26,27}
nums3={}
print(create_intervals(nums1), "\n", create_intervals(nums2), "\n", create_intervals(nums3))
