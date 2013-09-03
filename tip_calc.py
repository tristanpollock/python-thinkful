import sys

meal = float(sys.argv[1])
tax = float(sys.argv[2])/100
tip = float(sys.argv[3])/100
tax_value = meal * tax
meal_with_tax = meal + meal * tax
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value

print "The base cost of your meal was ${:.2f}".format(meal)
print "You need to pay ${:.2f} for tax.".format(tax_value)
print "Tipping at a rate of 15%, you should leave ${:.2f} for a tip.".format(tip_value)
print "The grand total of your meal is ${:.2f}.".format(total)
