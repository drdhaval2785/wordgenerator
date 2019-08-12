import sys
import codecs
import re
import random
from indic_transliteration import sanscript

def createWordList(headwordfile):
	with open(headwordfile, 'r') as fin:
		result = [x.split(':')[0].rstrip() for x in fin]
	return result

def guj_to_slp1(lst):
	return [sanscript.transliterate(x, 'gujarati', 'slp1') for x in lst]

def pruneByPatterns(hwList, requiredPatterns, prohibitedPatterns):
	result = []
	for hw in hwList:
		if re.search(requiredPatterns, hw) and not re.search(prohibitedPatterns, hw):
			result.append(hw)
	return result

if __name__ == "__main__":
	requiredPatterns = sys.argv[1]
	prohibitedPatterns = sys.argv[2]
	number = int(sys.argv[3])
	length = int(sys.argv[4])
	#hwList = createWordList('sanhw1.txt')
	hwList = createWordList('gujaratiwords.txt')
	hwList = guj_to_slp1(hwList)
	prunedList = pruneByPatterns(hwList, requiredPatterns, prohibitedPatterns)
	result = [x for x in prunedList if len(x) <= length]
	result1 = [sanscript.transliterate(x, 'slp1', 'gujarati') for x in result]
	if len(result1) > number:
		result2 = random.sample(result1, number)
	else:
		result2 = result1
	for res in result2:
		print(res)

