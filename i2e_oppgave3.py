# Oppgave 3.1

"""
Jeg finner fire forskjellige typer spørsmål i XML-filen: Single, Multi, Open og Grid.

Single og Multi er begge spørsmålstyper med svaralternativer. 
    Single-spørsmål kan kun ta ett svar, som "Hvilken aldersgruppe tilhører du?".
    Multi-spørsmål tillater derimot flere svar, som "Hvilke av disse aktivitetene har du deltatt på det siste året?". 

Open-spørsmål innebærer en tom tekstboks for input, som "Hva er din e-postadresse?".

Grid-spørsmål innebærer en tabell med svaralternativer, som "Hvor fornøyd er du med følgende tjenester?".
Her skal respondenten huke av for flere verdier i hver rad, og hver rad har sin egen variabel.
"""


# Oppgave 3.2

import xml.etree.ElementTree as ET
import pandas as pd

def get_questions(root):
    questions = {}
    for node in root.findall(".//Questionnaire/Routing/Nodes/"):
        if node.tag in ["Single", "Multi", "Open", "Grid"]:
            name = node.find("Name").text
            text_node = node.find('.//Text')
            text = text_node.text if text_node is not None else None
            alternatives = []
            for answer in node.findall('.//Answer'):
                value = answer.attrib['Precode']
                label = answer.find('.//Text').text
                alternatives.append((value, label))
            questions[name] = {
                'text': text,
                'alternatives': alternatives
            }
    return questions

def print_question_info(name, questions):
    question = questions.get(name)
    if question is not None:
        print(f"Spørsmål: {question['text']}")
        print("Svaralternativer:")
        for value, label in question['alternatives']:
            print(f"  {value} - {label}")

# Parse the XML file and retrieve question information
file = 'i2e_markup.xml'
tree = ET.parse(file)
root = tree.getroot()
questions = get_questions(root)

# Read the Excel file and store it in a DataFrame
df = pd.read_excel('i2e_datasett.xlsx')

# Create a frequency table for a "Single" question
single_question_freq = df['single_binary'].value_counts()

# Print information about the "Single" question
print_question_info('single_binary', questions)
print(single_question_freq)

# Create a frequency table for a "Multi" question
multi_question_freq = df['multi_binary1_1'].value_counts()

# Print information about the "Multi" question
print_question_info('multi_binary1_1', questions)
print(multi_question_freq)

