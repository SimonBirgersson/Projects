# Script with functions for analyzing absorbance data for activity assays


from scipy.stats import linregress as linreg


# Function to utilize later for calculation of concentration
def func(data, slope, intercept):
    """calculates the concentration from absorbance "x" using "k" and "m" from linreg."""
    conc = (data - intercept) / slope
    return conc


# function for linreg unit analysis etc.
def calculate(
    std,
    data,
    samplename=0,
    protein_concentration=0,
    dilution=1,
):
    """Input: \n
    Dataframe of std data with column 1 as dependent variable (conc, in mM), and the rest of columns being replicates of absorbance values, ex) column 2 is "abs #1" column 2 is "abs #2".

    Data frame with sample data  in the same fashion minus the first column.

    List of names of each sample, will be rownames in final dataframe

    "Protein_concentration" is optional for adding specific activity to to the dataframe, use unit mg and stock protein concentration

    "dilution" is optional for getting the values for the protein stock, use total dilution factor from measured sample to stock

    Output: \n
    Returns the same dataframe as added in "data" with new columns for concentration, and activity"""

    # calculate average and std for std absorbances
    std["avg abs"] = std.iloc[:, 1:].mean(axis=1)
    std["+/- abs"] = std.iloc[:, 1:].std(axis=1)

    # Fits the data into a linear regression class
    regr = linreg(std.iloc[:, 0], std["avg abs"])

    # calculate mean and stdev for sample data
    data["avg abs"] = data.iloc[:, 1:].mean(axis=1)
    data["+/- abs"] = data.iloc[:, 1:].std(axis=1)

    # Predicts concentrations of sample points
    data[["conc. [mM]", "+/- mM"]] = (
        data[["avg abs", "+/- abs"]]
        .apply(lambda x: func(x, regr.slope, regr.intercept))
        .multiply(dilution, axis="index")
    )

    # multiply by dilution factor
    if dilution == 1:
        pass
    else:
        try:
            data[["conc. [mM]", "+/- mM"]] = data[["conc. [mM]", "+/- mM"]].multiply(
                dilution, axis="index"
            )

        except:
            print("\n Beep! some problem with dilution, maybe too few elements in list")

    # unit conversion to activity
    data[["[nkat/ml]", "+/- nkat/ml"]] = data[["conc. [mM]", "+/- mM"]].apply(
        lambda x: x * 10**3 / 600
    )

    # if protein concentration is in calculate specific activity
    if protein_concentration == 0:
        pass
    elif protein_concentration != 0:
        data[["[nkat/mg]", "+/- nkat/mg"]] = data[["[nkat/ml]", "+/- nkat/ml"]].apply(
            lambda x: x / protein_concentration
        )
        # get absolute values of each stdev
        data[["+/- nkat/mg"]] = data[["+/- nkat/ml"]].apply(lambda x: abs(x))

    # get absolute values of each stdev
    data[["+/- abs", "+/- mM", "+/- nkat/ml"]] = data[
        ["+/- abs", "+/- mM", "+/- nkat/ml"]
    ].apply(lambda x: abs(x))

    # change row names to "samplename"
    if samplename == 0:
        pass
    elif isinstance(samplename, list):
        try:
            data.index = samplename
        except:
            print(
                "\n Beep! sample name doesn't work in calculate, maybe to few row names..."
            )

    # Prints the functions from the linear regression
    print("\nFitted equation is: abs = %.3f * c + %.3f" % (regr.slope, regr.intercept))

    # The coefficient of determination R2: 1 is perfect prediction
    print("\nCoefficient of determination (R2): %.4f" % regr.rvalue**2)

    return data, regr.slope, regr.intercept
