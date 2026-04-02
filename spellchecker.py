import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self._multi = md.MultiDictionary()
        # E' un oggetto MultiDictionary che ha tutti i suoi metodi, ad esempio loadDictionary()



    def handleSentence(self, txtIn, language):

        # 1. Pulizia testo: converte tutto in minuscolo, rimuove simboli e caratteri speciali, e poi
        # divide la frase inserita dall'utente in parole singole
        txtIn = replaceChars(txtIn.lower())
        parole = txtIn.split()

        # 2. Carico il dizionario chiamando loadDictionary() di MultiDictionary
        self._multi.loadDictionary(language)

        # -------------------------
        # USING CONTAINS
        # -------------------------
        print("\nUsing contains")
        start = time.time()
        result = self._multi.searchWord(parole, language)
        # Nota. Usa prima searchWord (di MultiDictionary) che a sua volta usa contains() di Dictionary
        end = time.time()

        for r in result:
            if not r.corretta:
                print(r)
        print("Time elapsed", end - start)

        # -------------------------
        # USING LINEAR SEARCH
        # -------------------------
        print("\nUsing Linear search")
        start = time.time()
        result = self._multi._dizionari[language].searchLinear  # metodo singolo
        # ma dobbiamo applicarlo a tutte le parole
        wrong = []
        for p in parole:
            if not self._multi._dizionari[language].searchLinear(p):
                wrong.append(p)
        end = time.time()

        for w in wrong:
            print(w)
        print("Time elapsed", end - start)

        # -------------------------
        # USING DICHOTOMIC SEARCH
        # -------------------------
        print("\nUsing Dichotomic search")
        start = time.time()
        wrong = []
        for p in parole:
            if not self._multi._dizionari[language].searchDichotomic(p):
                wrong.append(p)
        end = time.time()

        for w in wrong:
            print(w)
        print("Time elapsed", end - start)



    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    # NIENTE spazio qui dentro
    chars = "|*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
