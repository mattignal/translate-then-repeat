import os
from create_audio import produce_audio
from order_sentences import create_ordered_sentences


def run_sentences(native_language, target_language, word_or_exp_list,
                  shuffle=True, n=10, SRS=False, verbs=False):
    if n < 3:
        n = 3
    if not os.path.exists('audio'):
        os.makedirs('audio')
    ordered_sentences = create_ordered_sentences(target_language,
                                                 word_or_exp_list, shuffle,
                                                 n, SRS, verbs)
    audio = produce_audio(native_language, target_language, ordered_sentences)

    audio.export(f'audio/{target_language}_{word_or_exp_list[0]}.mp3',
                 format='mp3')


if __name__ == "__main__":
    # You can call your run_sentences function here with appropriate parameters
    # For example:
    native_language = 'English'
    target_language = 'Spanish'
    word_or_exp_list = ['a través de',
                        'ha sido',
                        'por lo que',
                        'así como',
                        'a partir de',
                        'a lo largo',
                        'se trata',
                        'a pesar de',
                        'este tipo de',
                        'a la hora',
                        'en cuanto a',
                        'han sido',
                        'puede ser',
                        'la hora de',
                        'por otro lado',
                        'en los últimos',
                        'medio ambiente',
                        'sin duda',
                        'cada vez más',
                        'lo que se',
                        'por lo tanto',
                        'de la ley',
                        'punto de vista',
                        'se ha',
                        'por parte de',
                        'es decir',
                        'en el ámbito',
                        'tener en cuenta',
                        'a cabo',
                        'se ha convertido en',
                        'desde el punto de vista',
                        'hay que tener en cuenta',
                        'puesta en marcha de',
                        'llevar a cabo',
                        'al fin y al cabo',
                        'desde entonces',
                        "así es",
                        "por último",
                        "Por fin",
                        "De repente",
                        "Al principio",
                        "En ningún lugar",
                        "A propósito",
                        "Ni idea",
                        "En breve",
                        "Más adelante",
                        "Fuera de",
                        "En resumen",
                        "Con cariño",
                        "Bajo el sol",
                        "Hacia atrás",
                        "En casa",
                        "Por desgracia",
                        "Dentro de nada",
                        "Hasta el fin",
                        "En aquel entonces",
                        "A la vez",
                        "De ninguna forma",
                        "Cuesta arriba",
                        "De nuevo",
                        "Fuera de juego",
                        "En vivo",
                        "A fondo",
                        "Cabe mencionar",
                        "En total",
                        "A corto plazo",
                        "A largo plazo",
                        "Con respecto a"]
    n = 5  # number of repetitions of each phrase, keep higher for verbs
    SRS = False  # recommend False for verb practice
    shuffle = True  # shuffle the list?
    verbs = False  # Set to True if all verbs and you want a challenge with
    # different verb tenses

    run_sentences(native_language, target_language, word_or_exp_list,
                  shuffle, n, SRS)
    pass
