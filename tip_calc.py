from optparse import OptionParser

parser = OptionParser()
parser.add_option("-m", "--meal", dest="meal", help="cost for a meal",
 type="float")
parser.add_option("-x", "--tax", dest="tax", help="tax %, decimal form",
 type="float")
parser.add_option("-t", "--tip", dest="tip", help="tip for meal + tax",
	default=.15, type="float")

(options, args) = parser.parse_args()

if not options.meal:
	parser.error("You need to enter meal cost!")
if not options.tax:
	parser.error("You need to enter the tax %!") 

tax_value = options.meal * options.tax
meal_with_tax = options.meal + tax_value
tip_value = meal_with_tax * options.tip
total = meal_with_tax + tip_value

print "The base cost of your meal was ${:.2f}".format(options.meal)
print "You need to pay ${:.2f} for tax.".format(tax_value)
print "Tipping at a rate of 15%, you should leave ${:.2f} for a tip.".format(tip_value)
print "The grand total of your meal is ${:.2f}.".format(total)