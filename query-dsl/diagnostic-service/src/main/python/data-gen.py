'''
Generated by ChatGPT
Prompt:: ./prompt.txt
'''

import json
import random
from datetime import datetime

# Function to generate random date within a range
def random_date(start, end):
    return start + (end - start) * random.random()

# Function to generate patient diagnosis data
def generate_patient_diagnosis_data(num_entries):
    patient_diagnosis_data = []

    # ICD-10 diagnosis codes
    diagnosis_codes = ['J00', 'J09', 'J10', 'J11', 'J20', 'J12', 'J13', 'J14', 'J15', 'J16', 'J17', 'J18',
                       'H66', 'N39', 'K29', 'A09', 'J30', 'J01', 'J02', 'J03']

    # List of Swedish cities
    cities = ['Stockholm', 'Gothenburg', 'Malmö', 'Uppsala', 'Västerås', 'Örebro', 'Linköping', 'Helsingborg',
              'Jönköping', 'Norrköping', 'Lund', 'Umeå', 'Gävle', 'Borås', 'Södertälje', 'Eskilstuna', 'Halmstad']

    for _ in range(num_entries):
        # Randomly select attributes for patient diagnosis
        diagnosis_code = random.choice(diagnosis_codes)
        birth_year = random.randint(1940, 2010)
        registration_year = random.randint(birth_year, datetime.now().year)
        registration_date = random_date(datetime(birth_year, 1, 1), datetime(registration_year, 12, 31)).strftime("%Y-%m-%d")
        age_at_diagnose = registration_year - birth_year
        city_of_residence = random.choice(cities)
        gender = random.choice(['M', 'F'])
        married = random.choice([True, False])

        # Construct patient diagnosis record
        patient_record = {
            'diagnosis_code': diagnosis_code,
            'registration_date': registration_date,
            'age_at_diagnose': age_at_diagnose,
            'birth_year': birth_year,
            'city_of_residence': city_of_residence,
            'gender': gender,
            'married': married
        }
        patient_diagnosis_data.append(patient_record)

    return patient_diagnosis_data

# Function to generate demographic data
def generate_demographic_data(cities):
    demographic_data = []

    for city in cities:
        total_population = random.randint(50000, 500000)  # Random population for each city
        city_data = {
            'city': city,
            'total_population': total_population
        }
        demographic_data.append(city_data)

    return demographic_data

# Main function
def main():
    # Configuration
    num_patient_entries = 100
    cities = ['Stockholm', 'Gothenburg', 'Malmö', 'Uppsala', 'Västerås', 'Örebro', 'Linköping', 'Helsingborg',
              'Jönköping', 'Norrköping', 'Lund', 'Umeå', 'Gävle', 'Borås', 'Södertälje', 'Eskilstuna', 'Halmstad']

    # Generate data
    patient_diagnosis_data = generate_patient_diagnosis_data(num_patient_entries)
    demographic_data = generate_demographic_data(cities)

    # Save patient diagnosis data to JSON file
    with open('patient_diagnosis_data.json', 'w') as f:
        json.dump(patient_diagnosis_data, f, indent=4)

    # Save demographic data to JSON file
    with open('demographic_data.json', 'w') as f:
        json.dump(demographic_data, f, indent=4)

if __name__ == "__main__":
    main()