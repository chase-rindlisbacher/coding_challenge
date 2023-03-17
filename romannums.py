romdict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
def romantonumbers(dict,roman):
    bCont = True
    while bCont == True:
        nums = []
        value = 0
        count = 0
        for c in range(0,len(roman),1) :
            num = dict[roman[c]]
            if count > 0 :
                if num > ((10 * nums[count - 1]) + 1):
                    nums.append(num)
                else:
                    print("Invalid Roman Numeral")
                    bCont = False
            else:
                nums.append(num)

        if bCont == True:
            count = 0
            count2 = 1
            if count2 <= len(nums) -1:
                while count2 < len(nums) -1:
                    if nums[count] < nums[count2]:
                        value += nums[count2] - nums[count]
                        count += 2
                        count2 += 2
                    else:
                        if ((count2 + 1) <= len(nums) - 1) and (nums[count2] < nums[count2 + 1]):
                            temp = nums[count2 + 1] - nums[count2]
                            value += nums[count] + temp
                            count += 3
                            count2 += 3
                        elif ((count2 + 1 <= len(nums) -1) and (nums[count2] > nums[count2 + 1])):
                            value += nums[count2] + nums[count2 + 1]
                            count += 2
                            count2 += 2
                        else:
                            break
                if count2 <= len(nums) -1:
                    try:
                        if nums[count] < nums[count2]:
                            value += nums[count2] - nums[count]
                            count2 +=1
                        else:
                            value += nums[count] + nums[count2]
                            count2 +=1
                    except:
                        if count <= len(nums) -1:
                            value += nums[count]
                elif count <= len(nums) -1:
                    value += nums[count]
            else:
                value += nums[count]          
            print(f'Roman Input: {roman}\nNumber:{value}')
            bCont = False

romantonumbers(romdict,"XLVI")