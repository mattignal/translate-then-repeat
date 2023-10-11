"""module to select amazon polly voice"""
import numpy as np


def select_voice(language, gender):
    voices = {
        'Arabic': {
            'Male': ['Zayd'],
            'Female': ['Zeina']
        },
        'Arabic (Gulf)': {
            'Male': ['Zayd'],
            'Female': ['Hala']
        },
        'Dutch (Belgian)': {
            'Male': [],
            'Female': ['Lisa']
        },
        'Catalan': {
            'Male': [],
            'Female': ['Arlet']
        },
        'Chinese (Cantonese)': {
            'Male': [],
            'Female': ['Hiujin']
        },
        'Chinese (Mandarin)': {
            'Male': [],
            'Female': ['Zhiyu']
        },
        'Danish': {
            'Male': ['Mads'],
            'Female': ['Sofie', 'Naja']
        },
        'Dutch': {
            'Male': ['Ruben'],
            'Female': ['Lotte', 'Laura']
        },
        'English (Australian)': {
            'Male': ['Russell'],
            'Female': ['Olivia', 'Nicole']
        },
        'English (British)': {
            'Male': ['Brian', 'Arthur'],
            'Female': ['Amy', 'Emma']
        },
        'English (Indian)': {
            'Male': [],
            'Female': ['Raveena', 'Kajal', 'Aditi']
        },
        'English (Ireland)': {
            'Male': [],
            'Female': ['Niamh']
        },
        'English (New Zealand)': {
            'Male': [],
            'Female': ['Aria']
        },
        'English (South African)': {
            'Male': [],
            'Female': ['Ayanda']
        },
        'English': {
            'Male': ['Matthew', 'Gregory', 'Joey', 'Justin', 'Kevin',
                     'Stephen'],
            'Female': ['Joanna', 'Danielle', 'Ivy', 'Kendra', 'Kimberly',
                       'Salli', 'Ruth']
        },
        'English (Welsh)': {
            'Male': ['Geraint'],
            'Female': []
        },
        'Finnish': {
            'Male': [],
            'Female': ['Suvi']
        },
        'French': {
            'Male': ['Rémi', 'Mathieu'],
            'Female': ['Léa', 'Céline']
        },
        'French (Belgian)': {
            'Male': [],
            'Female': ['Isabelle']
        },
        'French (Canadian)': {
            'Male': ['Liam'],
            'Female': ['Gabrielle', 'Chantal']
        },
        'German': {
            'Male': ['Hans', 'Daniel'],
            'Female': ['Vicki', 'Marlene']
        },
        'German (Austrian)': {
            'Male': [],
            'Female': ['Hannah']
        },
        'Hindi': {
            'Male': [],
            'Female': ['Kajal', 'Aditi']
        },
        'Icelandic': {
            'Male': ['Karl'],
            'Female': ['Dóra']
        },
        'Italian': {
            'Male': ['Giorgio', 'Adriano'],
            'Female': ['Bianca', 'Carla']
        },
        'Japanese': {
            'Male': ['Takumi'],
            'Female': ['Mizuki', 'Kazuha', 'Tomoko']
        },
        'Korean': {
            'Male': [],
            'Female': ['Seoyeon']
        },
        'Norwegian': {
            'Male': [],
            'Female': ['Liv', 'Ida']
        },
        'Polish': {
            'Male': ['Jacek', 'Jan'],
            'Female': ['Ewa', 'Maja', 'Ola']
        },
        'Portuguese': {
            'Male': ['Ricardo', 'Thiago'],
            'Female': ['Camila', 'Vitória']
        },
        'Portuguese (European)': {
            'Male': ['Cristiano'],
            'Female': ['Inês']
        },
        'Romanian': {
            'Male': [],
            'Female': ['Carmen']
        },
        'Russian': {
            'Male': ['Maxim'],
            'Female': ['Tatyana']
        },
        'Spanish': {
            'Male': ['Pedro'],
            'Female': ['Mia']
        },
        'Spanish (European)': {
            'Male': ['Enrique', 'Sergio'],
            'Female': ['Lucia', 'Conchita']
        },
        'Spanish (Mexican)': {
            'Male': ['Andrés'],
            'Female': ['Mia']
        },
        'Spanish (US)': {
            'Male': ['Miguel', 'Pedro'],
            'Female': ['Penélope', 'Lupe']
        },
        'Swedish': {
            'Male': [],
            'Female': ['Astrid', 'Elin']
        },
        'Turkish': {
            'Male': [],
            'Female': ['Filiz']
        },
        'Welsh': {
            'Male': [],
            'Female': ['Gwyneth']
        }
    }

    if gender not in ["Male", "Female"]:
        gender = np.random.choice(['Male', 'Female'])
    if gender == 'Male':
        other_gender = 'Female'
    elif gender == 'Female':
        other_gender = 'Male'
    else:
        other_gender = "Male"

    try:
        return voices[language][gender][0]
    except KeyError:
        return voices[language][other_gender][0]
