
##########
# Total number of questions: #
# len(pages) * (len(pages)-1) + len(source_elements_across_all_pags) #
##########


import pandas as pd
from pprint import pprint

# Placeholder data
pages = [
    {
        'id': 1,
        'name': 'Home',
        'elements': [
            'SHAEDS',
            'Classics',
            'See all',
            'More details',
            'FW2023',
        ],
    },
    {
        'id': 2,
        'name': 'Classics',
        'elements': [
            'Home',
            'Classics',
            '649 - Original',
            'More details',
            '$261.00',
        ],
    },
    {
        'id': 3,
        'name': 'Details',
        'elements': [
            'Classics',
            '649 - Original',
            '$261.00',
            'Persol',
            'To Shopping Bag',
        ],
    },
    {
        'id': 4,
        'name': 'Photos',
        'elements': [
            'Photo',
            'Dots',
        ],
    },
    {
        'id': 5,
        'name': 'Shopping Bag',
        'elements': [
            'Details',
            'Shopping Bag',
            'Delivery Location',
            'VISA Classic',
            'To Checkout',
        ],
    },
]

# Data container
questions = {
    'source_element_selection': [],
    'target_page_selection': [],
}

# Source element selection
for target_page in pages:
    for source_page in pages:
        if source_page != target_page:
            question = {
                'text': 'Which element links to this target page?',
                'source_page': source_page['name'],
                'target_page': target_page['name'],
                'options': source_page['elements'] + ['None']
            }
            questions['source_element_selection'].append(question)

# Target page selection
for source_page in pages:
    for source_element in source_page['elements']:
        question = {
            'text': 'Which page does this element link to?',
            'source_page': source_page['name'],
            'source_element': source_element,
            'options': [page['name'] for page in pages if page != source_page] + ['None']
        }
        questions['target_page_selection'].append(question)


# Questions
pprint(questions)

# Total number of questions
source_selection_count = len(questions['source_element_selection'])
target_selection_count = len(questions['target_page_selection'])
total_count = source_selection_count + target_selection_count
print(f'Source element selection questions count: {source_selection_count}')
print(f'Target page selection questions count: {target_selection_count}')
print(f'Total questions count: {total_count}')

# DataFrame
source_selection_questions = questions['source_element_selection'].copy()
for i in range(len(source_selection_questions)):
    source_selection_questions[i]['type'] = 'source_selection'
target_selection_questions = questions['target_page_selection'].copy()
for i in range(len(target_selection_questions)):
    target_selection_questions[i]['type'] = 'target_selection'
df = pd.DataFrame(source_selection_questions + target_selection_questions)
print(df)