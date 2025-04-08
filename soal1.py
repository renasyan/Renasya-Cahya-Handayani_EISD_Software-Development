def olah_data_review(data):
    mean = sum(data)/len(data)
    top = max(data)
    bottom = min(data)
    return bottom, top, mean

# data = [4.5, 2.0, 1.5, 3.0, 2.5, 4.0, 5.0, 3.5, 2.0, 1.0] 
data = [5,4,2.5,5,3.6,1.1,3.6,4,4.2,1.5] 


print(olah_data_review(data))