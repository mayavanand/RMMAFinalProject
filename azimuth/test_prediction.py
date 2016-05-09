import numpy as np
import csv
import model_comparison
import testdata
import sys

def main():
	g, cp, pp = testdata.get_test_data("data/testdata.xlsx")
	results = model_comparison.predict(g, cp, pp, model_file=sys.argv[1])
	writer = csv.writer(open(sys.argv[2], "w"))
	#results = model_comparison.predict(g, cp, pp, model_file='saved_models/PAM_nopos.pickle')
	#writer = csv.writer(open("NGGXX.csv", "w"))
	writer.writerow(results)

if __name__ == "__main__": main()
