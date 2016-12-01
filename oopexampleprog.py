import oopexample

maths = oopexample.Numchange()

def main():

	num = float(input("Please enter a number.\n"))

	added = maths.addfive()

	multip = maths.multiply(added)

	print("The manipulated value is ",multip)
	
main()