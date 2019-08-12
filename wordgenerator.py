import sys
import codecs
import re
from indic_transliteration import sanscript

def createWordList(headwordfile):
	with open(headwordfile, 'r') as fin:
		result = [x.split(':')[0] for x in fin]
	return result

def pruneByPatterns(hwList, requiredPatterns, prohibitedPatterns):
	for hw in hwList:
		if re.search(requiredPatterns, hw) and not re.search(prohibitedPatterns, hw):
			print(hw)

if __name__ == "__main__":
	requiredPatterns = sys.argv[1]
	prohibitedPatterns = sys.argv[2]
	hwList = createWordList('sanhw1.txt')
	pruneByPatterns(hwList, requiredPatterns, prohibitedPatterns)

