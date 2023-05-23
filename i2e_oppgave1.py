import pandas as pd

# Reads the Excel file and store it in a DataFrame
try:
    df = pd.read_excel('C:/I2E/i2e_datasett.xlsx')
    print("Excel file read successfully.")
except Exception as e:
    print(f"An error occurred while reading the Excel file: {e}")


# Oppgave 1.1: Bruk kode til aa identifisere kolonner som inneholder tekst

text_columns = df.select_dtypes(include=['object']).columns                     
print('Solely text-based columns include:', text_columns)


# Oppgave 1.2: Bruk kode til aa identifisere den tekststrengen på tvers av alle tekst-variabler med flest antall tegn

max_length = 0
longest_string = None

for column in text_columns:
    max_string_in_col = df[column].str.len().idxmax()
    max_length_in_col = df[column].str.len().max() 
    
    if max_length_in_col > max_length:
        max_length = max_length_in_col
        longest_string = df.loc[max_string_in_col, column]

print(f"The longest string across all text variables is: '{longest_string}', with a length of {max_length} characters.")


# Oppgave 1.3: Lag en tabell som viser gjennomsnittsverdier for alle numeriske variabler med mer enn 10 observasjoner

numeric_columns = df.select_dtypes(include='number').columns
numeric_columns_over10obs = [col for col in numeric_columns if df[col].count() > 10]

avg_values_table = df[numeric_columns_over10obs].mean()
print("\nAverage values for numeric variables with more than 10 observations:")
print(avg_values_table)

