import pandas as pd

def solution(input_data):
    df = pd.read_csv(input_data)
    list_of_presenets = df['Box Dimensions'].to_list()
    del df

    full_list = []
    combined_wrapping_paper_total = 0
    combined_ribbon_total = 0

    for present in list_of_presenets:
        # Split and get Int values for each boxes dimensions
        dimensions = list(map(int, present.split('x')))
        # Sort Dimensions so that smallest measures are always in positions 0 and 1
        dimensions.sort(reverse=False)
        # Get all individual dimension calculations
        smallest_dimension = dimensions[0]*dimensions[1]
        second_dimension = dimensions[0]*dimensions[2]
        third_dimension = dimensions[2]*dimensions[1]
        # Get Box Volume
        box_volume = dimensions[0]*dimensions[1]*dimensions[2]
        # Calculate Wrapping Paper Required for Box
        wrapping_paper_total = 2*(smallest_dimension+second_dimension+third_dimension)+smallest_dimension
        # Add to Wrapping Paper Catch-All Calculation
        combined_wrapping_paper_total+= wrapping_paper_total
        # Calculate Ribbon Needed for Box
        ribbon_total = smallest_dimension+box_volume
        # Add to Ribbon Catch-All Calculation
        combined_ribbon_total += ribbon_total
        #Append all Results to full list
        full_list.append([dimensions, wrapping_paper_total, ribbon_total])

    print(f'Calculated Wrapping Paper Total: {combined_wrapping_paper_total}')
    print(f'Calculated Ribbon Total: {combined_ribbon_total}')


if __name__ == "__main__":
    solution("list_of_presents.csv")