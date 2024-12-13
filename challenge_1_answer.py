import pandas

df = pandas.read_csv("list_of_presents.csv")

df[['Length', 'Width', 'Height']] = df['Box Dimensions'].str.extract('(\d{1,2})x(\d{1,2})x(\d{1,2})')


df[['Smallest Length', 'Second Smallest Length']] = df.apply(lambda x: pandas.Series(sorted([x['Length'], x['Width'], x['Height']])[:2]), axis=1)

df[['Length', 'Width', 'Height', 'Smallest Length', 'Second Smallest Length']] = df[['Length', 'Width', 'Height', 'Smallest Length', 'Second Smallest Length']].astype(int)

df['Surface Area'] = 2 * ((df['Length'] * df['Width']) + (df['Width'] * df['Height']) + (df['Height'] * df['Length']))
df['Smallest Side'] = df['Smallest Length'] * df['Second Smallest Length']
df['Wrapping Area'] = df['Surface Area'] + (df['Smallest Length'] * df['Second Smallest Length'])


df['Smallest Perimeter'] = 2 * (df['Smallest Length'] + df['Second Smallest Length'])
df['Volume'] = df['Length'] * df['Width'] * df['Height']
df['Ribbon Length'] = df['Smallest Perimeter'] + df['Volume']

sums = df.sum(axis=0, numeric_only=True)

wrapping_area_sum = sums['Wrapping Area']
ribbon_length_sum = sums['Ribbon Length']


print(f"The total wrapping paper needed is: {wrapping_area_sum}")

print(f"The total ribbon needed is: {ribbon_length_sum}")