#### roundoff ####

	What it does ?
		Beautifully rounds off the input as per your requirement.

	How it works ?
		Takes two parameters as input like one is float number to be rounded off and other an integer number that denotes the number of decimal you want.

	Why would you need it ?
		Well to be honest, I build it when I upgraded to Vertica v9.X. Its weird that the result of the built-in round method returns an ugly trail of zeroes. (No offence Vertica Devs)

	Why it is fast ?
		No external libraries required, using python's inbuild round method.
