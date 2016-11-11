# Program to convert kilometers into miles

# change this value for a different result
kilometers = float(input('Enter kilometers: '))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('{0} kilometers is equal to {1} miles'.format(kilometers,miles))
