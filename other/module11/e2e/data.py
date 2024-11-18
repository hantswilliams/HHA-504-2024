# Function to load ICD-10 from a file
def load_icd10(filepath):
    data = []
    with open(filepath, 'r') as file:
        for line in file:
            # Skip empty lines
            if not line.strip():
                continue
            # Ensure proper splitting
            parts = line.strip().split(' ', 1)  # For space-delimited files
            if len(parts) == 2:  # Only process valid lines
                code, description = parts
                data.append({"code": code, "description": description})
    return data

# Function to load HCPCS which is tab delimited text file 
def load_hcpcs(filepath):
    data = []
    with open(filepath, 'r') as file:
        for line in file:
            # Skip empty lines
            if not line.strip():
                continue
            # Ensure proper splitting
            parts = line.strip().split('\t', 1)  # For tab-delimited files
            if len(parts) == 2:  # Only process valid lines
                code, description = parts
                data.append({"code": code, "description": description})
    return data

# Load ICD-10 data from the text file
ICD10_DATA = load_icd10('data/icd10cm2025.txt')

# Load HCPCS data from the text file
HCPCS_DATA = load_hcpcs('data/hcpcs2025.txt')

## Merge together ICD10_DATA and HCPCS_DATA
MERGED_DATA = ICD10_DATA + HCPCS_DATA