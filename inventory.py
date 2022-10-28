# Create a program with a list:
# Each item in the list is the quantity of a part for the airplane toy.
# Suppose the optimal number of parts is [ 1000, 1000, 1000, 1000 ]. Can you figure out the following using built-in list functions?

	# Which airplane toy part are we missing the most? Use min() to find the minimum values in each list.
	# Is there an airplane toy part that we are overstocking? Use max() to find the maximum value in each list.
# Codédex

airplane_toys = [898, 732, 543, 878]

a = print(min(airplane_toys))
b = print(max(airplane_toys))
