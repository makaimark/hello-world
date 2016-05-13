import sys

def main():
	if len(sys.argv) == 2:
		name = sys.argv[1]
	else :
		name = "world"
	
	print ( " Hello " + name )

main()

