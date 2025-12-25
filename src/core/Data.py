
import pandas as pd

language_tuple_list = [("English", 0),
                       ("Spanish", 1),
                       ("Portuguese", 2),
                       ("Italian", 3),
                       ("French", 4),
                       ("German", 5),
                       ("Danish", 6),
                       ("Japanese", 7),
                       ("Chinese", 8),
                       ("Hindi", 9),
                       ("Arabic", 10),
                       ("Russian", 11),
                       ]

multi_language_dict = {
    "as": ("como", "como", "come", "comme", "wie", "som", "ように", "一", "जैसा", "كما", "как"),
    "I": ("Yo", "Eu", "Io", "Je", "Ich", "Jeg", "私は", "人", "मैं", "أنا", "Я"),
    "his": ("Su", "Seu", "Il suo", "son", "siene", "Hans", "彼の", "他的", "उसका", "له", "его"),
    "that": ("eso", "isso", "quello", "ce", "das", "at", "それ", "那", "वह", "ذلك", "что"),
    "he": ("él", "ele", "lui", "il", "er", "han", "彼", "他", "वह", "هو", "он"),
    "was": ("era", "Foi", "era", "était", "war", "var", "でした", "是", "था", "كان", "был"),
    "for": ("para", "para", "per", "pour", "für", "til", "ため", "为", "के लिए", "ل", "для"),
    "on": ("en", "em", "su", "sur", "auf", "pay", "に", "在", "पर", "على", "на"),
    "are": ("son", "são", "sono", "sont", "sind", "er", "です", "是", "हैं", "هي", "есть"),
    "with": ("con", "com", "con", "avec", "mit", "med", "と", "与", "के साथ", "مع", "с"),
    "they": ("ellos", "eles", "essi", "ils", "sie", "de", "彼ら", "他们", "वे", "هم", "они"),
    "be": ("ser", "ser", "essere", "être", "sein", "vær", "ある", "是", "होना", "يكون", "быть"),
    "at": ("a", "em", "a", "à", "bei", "ved", "で", "在", "पर", "في", "в"),
    "one": ("uno", "um", "uno", "un", "ein", "en", "一つ", "一", "एक", "واحد", "один"),
    "have": ("tener", "ter", "avere", "avoir", "haben", "ha", "持っている", "有", "है", "لديك", "иметь"),
    "this": ("esto", "isso", "questo", "ceci", "dies", "denne", "これ", "这个", "यह", "هذا", "это"),
    "from": ("de", "de", "da", "de", "von", "fra", "から", "从", "से", "من", "из"),
    "by": ("por", "por", "per", "par", "durch", "ved", "より", "通过", "द्वारा", "بواسطة", "по"),
    "hot": ("caliente", "quente", "caldo", "chaud", "heiß", "varm", "暑い", "热", "गर्म", "حار", "горячо"),
    "word": ("palabra", "palavra", "parola", "mot", "Wort", "ord", "言葉", "词", "शब्द", "كلمة", "слово"),
    "but": ("pero", "mas", "ma", "mais", "aber", "men", "しかし", "但", "लेकिन", "لكن", "но"),
    "what": ("qué", "o que", "cosa", "quoi", "was", "hva", "何", "什么", "क्या", "ماذا", "что"),
    "some": ("algunos", "alguns", "alcuni", "quelques", "einige", "noen", "いくつか", "一些", "कुछ", "بعض", "некоторые"),
    "is": ("es", "é", "è", "est", "ist", "er", "ある", "是", "है", "هو", "является"),
    "it": ("eso", "isso", "esso", "il", "es", "det", "それ", "它", "यह", "هو", "это"),
    "your": ("tu", "seu", "il tuo", "votre", "dein", "din", "あなたの", "你的", "आपका", "لك", "ваш"),
    "or": ("o", "ou", "oppure", "ou", "oder", "eller", "または", "或者", "या", "أو", "или"),
    "had": ("tenía", "teve", "aveva", "avait", "hatte", "hadde", "持っていた", "有", "था", "كان", "имел"),
    "the": ("el", "o", "il", "le", "der", "den", "ザ", "的", "यह", "ال", "этот"),
    "of": ("de", "de", "di", "de", "von", "av", "の", "的", "का", "من", "из")
}

class Data:
    """
    Class for managing and retrieving multi-language data for a quiz application.
    """
    language_tuple_list = language_tuple_list
    multi_language_dict: dict
    word_list: list


    def __init__(self):
        import os
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        output_file = os.path.join(project_root, "data", "multi_language_dict.csv")

        new_data = pd.read_csv(output_file)

        self.word_list = new_data['English'].tolist()
        word_dict = dict(zip(self.word_list, map(tuple, new_data.iloc[:, 1:].values)))
        self.multi_language_dict = word_dict

    def get_data(self):
        """
        Retrieves the multi-language data dictionary.
        """
        return self.multi_language_dict


if __name__ == "__main__":
    """
    Test code for the Data class.
    """
    print(language_tuple_list)
    print(multi_language_dict)

    languages = []
    for lang in language_tuple_list:
        languages.append(lang[0])
    print(languages)

    headers = ["English"] + languages[1:]
    print(headers)

    data = []
    for english_word, translation in multi_language_dict.items():
        row = [english_word] + list(translation)
        data.append(row)

    df = pd.DataFrame(data, columns=headers)



    import os
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    output_file = os.path.join(project_root, "data", "multi_language_dict.csv")

    new_data = pd.read_csv(output_file)

    word_list = new_data['English'].tolist()
    word_dict = dict(zip(word_list, map(tuple, new_data.iloc[:, 1:].values)))

    print(word_dict)
    print(word_list)
    print(new_data)

