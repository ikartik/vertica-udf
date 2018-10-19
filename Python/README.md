#### roundoff ####

    Q : What it does ?
    A : Beautifully rounds off the input as per your requirement.

    Q : How it works ?
    A : Takes two parameters as input like one is float number to be rounded off and other an integer number that denotes the number of decimal you want.

    Q : Why would you need it ?
    A : Well to be honest, I built it when I upgraded to Vertica v9.X. Its weird that the result of the built-in round method returns an ugly trail of zeroes. (No offence Vertica Devs)

    Q : Why it is fast ?
    A : No external libraries required, using python's inbuilt round method.
