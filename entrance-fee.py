# Path to the Python 2 interpreter
#! /usr/bin/env python2

# The following line declares the encoding for the code.
# This allows us to display the pound currency symbol.

# -*- coding: utf-8 -*-

# Store the admission price as constants
baby_price = 0.99
child_price = 17.25
adult_price = 21.50
senior_price = 19.35


# Store the age limit as constants
baby_age_limit = 3
child_age_limit = 15
adult_age_limit = 60


# Variable to hold the total admission price
total = 0

# Variable to hold the total number of people in the group
# number = 0

# Keep reading ages until the user enters a blank line
visitor = input ("Enter the age of the visitor (0 to exit): ")

while visitor != 0:
	age = int(visitor)

	#Compute the amount based on the age
	if age <= baby_age_limit:
        	total = total + baby_price
		# number = number + 1
    	elif age <= child_age_limit:
		total = total + child_price
		# number = number + 1
	elif age <= adult_age_limit:
	        total = total + adult_price
		# number = number + 1
	else:
	        total = total + senior_price
		# number = number + 1

	# Read the next line from the user
	visitor = input ("Enter the age of the visitor (0 to exit): ")

# Display the final amount
print "The total entrance fee for the group is %.2f" %total

# To display the Pound currency symbol
# print u'The total entrance fee for the group is \u00a3 %.2f' %total

# To display the total number of users in the group along with the admission price.
# print u'There are %d people in the group and their entrance fee is \u00a3 %.2f' %(number, total)
