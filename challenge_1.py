import csv

def generate_box_dimensions(num_boxes, seed=None):
    """
    Generates random box dimensions in the format LxWxH.
    
    :param num_boxes: Number of box dimensions to generate
    :param seed: Seed for reproducibility
    :return: List of box dimensions as strings
    """
    if seed is not None:
        random.seed(seed)
    return [f"{random.randint(1, 10)}x{random.randint(1, 10)}x{random.randint(1, 10)}" for _ in range(num_boxes)]

def save_to_csv(file_path, data):
    """
    Saves a list of data to a CSV file.

    :param file_path: Path to the output CSV file
    :param data: List of data to save
    """
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Box Dimensions"])  # Write header
        writer.writerows([[dim] for dim in data])

if __name__ == "__main__":
    # Generate box dimensions
    box_dimensions = generate_box_dimensions(100, seed=42)
    
    # Save to CSV
    save_to_csv("list_of_presents.csv", box_dimensions)
    print("Box dimensions have been saved to 'list_of_presents.csv'.")
