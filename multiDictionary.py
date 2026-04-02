import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        """
        Costruttore della classe MultiDictionary.

        Inizializza una *mappa* (dict di Python) che conterrà,
        per ogni lingua supportata, il rispettivo oggetto Dictionary.

        Struttura prevista:
            self._dizionari = {
                "Italian": Dictionary(),
                "English": Dictionary(),
                ...
            }

        Nota:
        - Il costruttore NON carica ancora i file dei dizionari.
        - Prepara semplicemente la struttura dati che verrà riempita
          quando lo SpellChecker richiederà una lingua specifica.
        """
        # Dizionario vuoto che mapperà: nome lingua -> oggetto Dictionary
        self._dizionari = {}

    def loadDictionary(self, language):
        """
        Carica il dizionario relativo alla lingua specificata.
        """

        # 1. Se il dizionario è già presente, esco subito
        if language in self._dizionari:
            return

        # 2. Creo un nuovo oggetto Dictionary
        dizionario = d.Dictionary()

        filename = "resources/" + language + ".txt"
        # 3. Carico il file della lingua (es. "Italian.txt")
        dizionario.loadDictionary(filename)

        # 4. Salvo il dizionario nella mappa: lingua -> oggetto Dictionary
        self._dizionari[language] = dizionario


    def printDic(self, language):
        if language in self._dizionari:
            self._dizionari[language].printAll()
        else:
            print("Dizionario non caricato!")


    def searchWord(self, words, language):
        diz = self._dizionari[language]
        results = []

        for w in words:
            rwObj = rw.RichWord(w)
            rwObj.corretta = diz.contains(w)
            results.append(rwObj)

        return results


