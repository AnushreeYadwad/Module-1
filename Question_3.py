def binary(ll,item):
	start= 0
	end= len(ll)-1
	ans = False
	while(start<=end and not ans):
		mid = (start + end)//2
		if ll[mid] == item :
			ans = True
		else:
			if item < ll[mid]:
				end = mid - 1
			else:
				start = mid + 1	
	return ans
	
print(binary([49,58,93,100],108))



