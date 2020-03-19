# Check salary in percentage

package = 1000000


print("Percentage         Package          Increased Amount                 Total Amount")
print("-" * 100)

for i in range(10,101):
	result = (i/100) * package
	total_package = result + package
	re = round(result, 2)
	print("  %s               %s          %s                %s " % (i, package, re, total_package))
	print() 


