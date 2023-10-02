def createTargetArray(nums, index):
    target = []

    for i in range(len(nums)):
        if index[i] == len(target):
            target.append(nums[i])  
        else:            
            new_target = []
            for j in range(len(target)):
                if j == index[i]:
                    new_target.append(nums[i])  
                new_target.append(target[j])  
            print(new_target)
            target = new_target

    return target

nums = [0,1,2,3,4]
index = [0,1,2,2,1]    
print(createTargetArray(nums,index))





