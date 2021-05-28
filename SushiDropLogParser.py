#!/usr/bin/env python

# SUSHI DROP LOG PARSER

import argparse

def extractor(InputFile,OutputFile):
	translation_table = dict.fromkeys(map(ord, ',"'), None)
	with open(InputFile, 'r') as f:
		for i, line in enumerate(f):
			with open(OutputFile, 'a') as out:
				parsed = line.split(" ")
				topic = parsed[11].translate(translation_table)
				data = parsed[13].translate(translation_table)
				seq = parsed[14]
				out.write(topic+','+data+','+seq+'\n')
				

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('InputFile', help='Full path for input file')
	parser.add_argument('OutputFile', help='Full path for output file')
	args = parser.parse_args()
	extractor(args.InputFile,args.OutputFile)