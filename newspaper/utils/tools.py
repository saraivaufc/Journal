def filterList(list, index=0, tam=0):
	if index <= 0:
		return list[:tam]
	if index == None:
		index = 1
	if tam <= 0:
		return list
	list_return = list[(index*tam)-tam:index * tam]	
	return list_return