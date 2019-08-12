import sys
import codecs
import re
import random
from indic_transliteration import sanscript

def createWordList(headwordfile):
	with open(headwordfile, 'r') as fin:
		result = [x.split(':')[0] for x in fin]
	return result

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
	hwList = createWordList('sanhw1.txt')
	prunedList = pruneByPatterns(hwList, requiredPatterns, prohibitedPatterns)
	result = random.sample(prunedList, number)
	result1 = [sanscript.transliterate(x, 'slp1', 'devanagari') for x in result]
	for res in result1:
		print(res)

