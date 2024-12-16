import pandas

# Import csv into dataframe, extract dimensions and remove Box Dimensions string from dataframe
df = pandas.read_csv("list_of_presents.csv")
df[['Length', 'Width', 'Height']] = df['Box Dimensions'].str.extract('(\d{1,2})x(\d{1,2})x(\d{1,2})').astype(int)
del df['Box Dimensions']

# Sort dimensions, converting df from a dataframe to a series
df = df.apply(sorted, axis=1)

# Calculate wrapping paper per box
wrapping_paper = df.apply(lambda x: (2 * (x[0] * x[1] + x[1] * x[2] + x[2] * x[0])) + (x[0] * x[1]))

# Calculate ribbon per box
ribbon = df.apply(lambda x: (2 * (x[0] + x[1])) + (x[0] * x[1] * x[2]))

# Sum wrapping paper and ribbon
wrapping_paper_total = wrapping_paper.sum()
ribbon_total = ribbon.sum()

# Print results
print(f"The total wrapping paper needed is: {wrapping_paper_total}")
print(f"The total ribbon needed is: {ribbon_total}")
