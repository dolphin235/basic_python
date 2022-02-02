
import csv

def list_to_csv(listitem, output_path):
    with open(output_path, 'w') as f:
        write = csv.writer(f)
        write.writerow(listitem)

