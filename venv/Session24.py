"""
    Linear Regression

    Data: is known to us before hand
    Hence, Supervised Learning
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 5, 4, 5]

    Equation of Regression Line
    Y = b0 + b1X

    Primary Objective : To Find Slope of Line i.e. b1 !!

    Mean of X : MX | 3
    Mean of Y : MY | 4

    Step 1:
    -------------------------------------------------
    X   Y   X-MX    Y-MY    Sq(X-MX)    (X-MX)(Y-MY)
    -------------------------------------------------
    1   2   -2      -2      4           4
    2   4   -1       0      1           0
    3   5    0       1      0           0
    4   4    1       0      1           0
    5   5    2       1      4           2
    -------------------------------------------------

    Step 2:
    -------
    Sum of Sq(X-MX)     :   10
    Sum of (X-MX)(Y-MY) :   6

    b1 is slope of line
    b1 = [Sum of (X-MX)(Y-MY)] / [Sum of Sq(X-MX)]
    b1 = 6/10
    b1 = 0.6

    Step 3:
    -------

    Equation of Line
    ================
    Y = b0 + (0.6)X

    Put the mean value of x and y in equation to find b0
    4 = b0 + (0.6) * 3
    bo = 2.2

    ======================
    Final Equation of Line
    ======================
    Y = 2.2 + (0.6)X
    ======================

    Step 4:

    Calculate Errors !!
    Check for errors if they are more or less !!
    if errors are less we are good to go else we have to optimize our data or any other part of program

    1. MSE
    2. R2
    3. Variance

    Lets find MSE
    Substitute original value of x and compute y with equation of line

    Y = 2.2 + (0.6)X
    Y' will be predicted output based on equation of line

    -------------------------------------------------
    X   Y    Y'     Y-MY    Sq(Y-MY)  Y'-MY  Sq(Y'-MY)
    -------------------------------------------------
    1   2   2.8     -2      4         -1.2      1.44
    2   4   3.4      0      0         -0.6      0.36
    3   5   4        1      1            0      0
    4   4   4.6      0      0          0.6      0.36
    5   5   5.2      1      1          1.2      1.44
    -------------------------------------------------

    MSE = [Sum of Sq(Y'-MY)] / [Sum of Sq(Y-MY)]
    MSE = 3.6/6
    MSE = 0.6

    if MSE is 0 it means Regression Line is PERFECT
    MSE should be nearly 0 so as our predictions can go better

"""