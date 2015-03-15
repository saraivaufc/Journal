# -*- encoding=utf-8 -*-
class Search():
	def kmp(text, pattern):
		pattern = list(pattern)
	 
		shifts = [1] * (len(pattern) + 1)
		shift = 1
		for pos in range(len(pattern)):
			while shift <= pos and pattern[pos] != pattern[pos-shift]:
				shift += shifts[pos-shift]
			shifts[pos+1] = shift
	 
		startPos = 0
		matchLen = 0
		for c in text:
			while matchLen == len(pattern) or \
				  matchLen >= 0 and pattern[matchLen] != c:
				startPos += shifts[matchLen]
				matchLen -= shifts[matchLen]
			matchLen += 1
			if matchLen == len(pattern):
				yield startPos

	def search(phrase, text):
		phrase_split = phrase.split()
		phrase_weight = 0
		for i in phrase_split:
			phrase_weight += kmp(i, text)
		return phrase_weight


