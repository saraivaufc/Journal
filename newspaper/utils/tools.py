def filterList(list, index=1, tam=0):
	if index == None:
		index = 1
	if tam <= 0:
		return list
	list_return = list[(index*tam)-tam:index * tam]	
	if len(list_return) <= 0:
		list_return = filterList(list, index-1, tam)
	return list_return
