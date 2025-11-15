#!/usr/bin/env python3

import csv

# Limit the number of files to write
OFFSET = 1730
LIMIT = 50
DRYRUN = False

# Open the CSV file
with open('Resume.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    count = 0
    for row in reader:
        if count < OFFSET:
            count += 1
            continue
        
        if count >= LIMIT + OFFSET:
            break
        
        # Get the ID and Resume_str from the row
        resume_id = row['ID']
        resume_text = row['Resume_str']

        # Create filename based on ID
        filename = f'resume_analysis/shibboleet2/resume_{resume_id}.md'
        
        if DRYRUN:
            print(f'Would create {filename}')
            print(resume_text)
            print('\n\n')
            break
        
        # Write the formatted content to the file
        with open(filename, 'w', encoding='utf-8') as outfile:
            outfile.write('# Resume\n\n')
            outfile.write(resume_text)
            outfile.write('\n\n\n# Analysis\n\n')
            outfile.write('TODO\n')
            outfile.write('\n\n\n# Outcome\n\n')
            outfile.write('Interviewed. Excellent candidate. Hired.\n')
        
        count += 1
        print(f'Created {filename}')

print(f'\nTotal files created: {count - OFFSET}')
