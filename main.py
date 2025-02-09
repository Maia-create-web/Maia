class EnglishGermanDictionary:
    def __init__(self, word_list):
        self.dictionary = {}
        for item in word_list:
            english, german = item.split('-')
            self.dictionary[english.strip().lower()] = german.strip().lower()
            self.dictionary[german.strip().lower()] = english.strip().lower()

    def translate(self, word):
        return self.dictionary.get(word.lower(), "Not Found")

    def log_to_history(self, word):
        with open("history.txt", "a") as file:
            file.write(word + "\n")

word_list = [
    "area-Bereich", "book-Buch", "business-Geschäft", "case-Fall", "child-Kind", "company-Unternehmen",
    "country-Land", "day-Tag", "eye-Auge", "fact-Tatsache", "family-Familie", "government-Regierung",
    "group-Gruppe", "hand-hand", "home-Zuhause", "job-Job", "life-Leben", "lot-Menge", "man-man",
    "money-Geld", "month-Monat", "mother-Mutter", "Mr-Herr", "night-Nacht", "number-Nummer",
    "part-Teil", "people-Menschen", "place-Ort", "point-Punkt", "problem-problem", "program-Programm",
    "question-Frage", "right-Recht", "room-Zimmer", "school-Schule", "state-Zustand", "story-Geschichte",
    "student-Schüler", "study-Studie", "system-System", "thing-Ding", "time-Zeit", "water-Wasser",
    "way-Weg", "week-Woche", "woman-Frau", "word-Wort", "work-Arbeit", "world-Welt", "year-Jahr"
]

eng_ger_dict = EnglishGermanDictionary(word_list)

while True:
    user_word = input("Enter a word in English or German (or type 'exit' to quit): ").strip().lower()

    if user_word == "exit":
        print("Exiting the program.")
        break

    translation = eng_ger_dict.translate(user_word)
    print(f"Translation: {translation}")

    eng_ger_dict.log_to_history(user_word)
