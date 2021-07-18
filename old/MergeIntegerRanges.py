def merge_ranges(input_range_list):
    res=list()
    for i in range(len(input_range_list)):
        isMatched=False
        for j in range(len(res)):
            #case A
            if input_range_list[i].lower_bound==res[j].lower_bound \
            and input_range_list[i].upper_bound==res[j].upper_bound:
                isMatched=True
            
            #case B
            if input_range_list[i].lower_bound>=res[j].lower_bound \
            and input_range_list[i].lower_bound<=res[j].upper_bound:
                isMatched=True
                res[j].lower_bound=(min(res[j].lower_bound, input_range_list[i].lower_bound))
                res[j].upper_bound=(max(res[j].upper_bound, input_range_list[i].upper_bound))

            #case C            
            if input_range_list[i].upper_bound>=res[j].lower_bound \
            and input_range_list[i].upper_bound<=res[j].upper_bound:
                isMatched=True
                res[j].lower_bound=(min(res[j].lower_bound, input_range_list[i].lower_bound))
                res[j].upper_bound=(max(res[j].upper_bound, input_range_list[i].upper_bound))
            
            #case D
            if input_range_list[i].lower_bound<=res[j].lower_bound \
            and input_range_list[i].upper_bound>=res[j].upper_bound:
                isMatched=True
                res[j].lower_bound=(min(res[j].lower_bound, input_range_list[i].lower_bound))
                res[j].upper_bound=(max(res[j].upper_bound, input_range_list[i].upper_bound))


            if input_range_list[i].lower_bound>=res[j].lower_bound \
            and input_range_list[i].upper_bound<=res[j].upper_bound:
                isMatched=True
                res[j].lower_bound=(min(res[j].lower_bound, input_range_list[i].lower_bound))
                res[j].upper_bound=(max(res[j].upper_bound, input_range_list[i].upper_bound))
                            

        if not isMatched:
            res.append(Range(input_range_list[i].lower_bound,input_range_list[i].upper_bound))
    return res


# [[1,4], [3,7], [5,10], [11,15]]
        
