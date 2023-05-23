# Vi kan lagre dokumentasjonen i en datastruktur vha. ordboeker

import xml.etree.ElementTree as ET

file = 'i2e_markup.xml'

tree = ET.parse(file)

root = tree.getroot()

def get_questions(root):
    questions = {}                                                              
                                                      
    for node in root.findall(".//Questionnaire/Routing/Nodes/"):                 
        if node.tag in ["Single", "Multi", "Open", "Grid"]:

            name = node.find("Name").text
            text_node = node.find('.//Text')
            text = text_node.text if text_node is not None else None

            # Retrieve answer alternatives
            alternatives = []
            for answer in node.findall('.//Answer'):
                value = answer.attrib['Precode']            # f.eks. "1"
                label = answer.find('.//Text').text         # f.eks. "Mann"
                alternatives.append((value, label))

            # Add to questions dictionary
            questions[name] = {
                'text': text,
                'alternatives': alternatives
            }

    return questions

questions = get_questions(root)


# Function for printing information about specific question
def print_question_info(name, questions):
    question = questions.get(name)
    if question is not None:
        print(f"Spørsmål: {question['text']}")
        print("Svaralternativer:")
        for value, label in question['alternatives']:
            print(f"  {value} - {label}")

# Call function to print information about specific question
print_question_info('background_gender', questions)
