import networkx as nx
import argparse

parser = argparse.ArgumentParser(description="Creates a Flow Graph for a Program in C/Java")
parser.add_argument('--fileName', required=True, help="The name of the file containing the program to analyze")
args = parser.parse_args()
print args.fileName

programFile = open(args.fileName, 'r')
outputFile = open("commentedProgram.txt", 'w')
controlFlowGraph = nx.Graph()
counter = 1


createCFG(self, programContent):
    tokens = programContent.split()
    for index, token in enumerate(tokens):
        if (token == "if"):
        	counter += 1
        	[ifString, elseString] = getIfBlockString(tokens[index:])
        	createCFG(ifString)
        	createCFG(elseString)

getIfBlockString(self, tokens):
	afterIf = True
	afterElse = False
	withinBlock = True
	counter = 0

	parentheses = 0
	ifString = ""
	elseString = ""
    for token in tokens:
    	if(token = '{'): 
    		withinBlock = True
    		parentheses += 1
    		continue
    	if(token = '}'):
    		parentheses -= 1
    		continue
        if(withinBlock = True && parentheses != 0 && (token != '{' || token != '}')):
        	if(afterIf): ifString += token
        	if(afterElse): elseString += token
        	continue
        if(withinBlock = True && parentheses == 0): 
        	withinBlock == False
        	afterIf = False
        	continue
        if(withinBlock == False && afterIf = False && afterElse == False):
        	counter += 1
        	if(counter == 1 && token != "else"): break;
            else: afterElse = True
        	continue
    return [ifString, elseString]




"""categorizeLine(self, line):
    if "if" in line:
    	counter += 1
    	writeToOutputFile()
    	controlFlowGraph.addNode(counter)

handleIfStatement(self):

writeToOutputFile(self):
    outputStr = str(counter) + "\t" + str(line)
    outputFile.write(outputStr)

for line in programFile:
    outputStr = str(counter) + "\t" + str(line)
    outputFile.write(outputStr)
    if "if" in line:"""

    
		

