import networkx as nx
import argparse

parser = argparse.ArgumentParser(description="Creates a Flow Graph for a Program in C/Java")
parser.add_argument('--fileName', required=True, help="The name of the file containing the program to analyze")
args = parser.parse_args()
print args.fileName

programFile = open(args.fileName, 'r')
outputFile = open("commentedProgram.txt", 'w')
controlFlowGraph = nx.Graph()

for line in programFile:
	if "if" in line:
		

