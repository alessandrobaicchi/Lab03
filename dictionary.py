class Dictionary:
    def __init__(self):
        self._words = []
        # E' una lista di stringhe che contiene tutte le parole del dizionario della lingua selezionata

    def loadDictionary(self,path):
        try:
            with open(path, 'r', encoding="utf-8") as f:
                for line in f:
                    # Rimuovo spazi/newline e mette tutto in minuscolo
                    word = line.strip().lower()
                    if word:    # La variabile word contiene qualcosa? Se TRUE aggiungo a _words
                        self._words.append(word)
        except FileNotFoundError:
            print(f"File {path} non trovato!")

        print("Percorso assoluto:", path)


    # Metodo "di servizio" che serve a stampare le parole di _words
    def printAll(self):
        for w in self._words:
            print(w)


    # Primo metodo di ricerca
    def contains(self,word):
        return word in self._words
        # Se word è nella lista _words restituisce TRUE


    # Secondo metodo di ricerca: lineare
    def searchLinear(self,word):
        for w in self._words:
            if w == word:
                return True
        return False


    # Terzo metodo di ricerca: dicotomica
    # Posso farlo perché la lista _words è ordinata alfabeticamente!
    def searchDichotomic(self,word):
        low = 0
        high = len(self._words)-1
        while low <= high:
            mid = (low + high) // 2     # E' la divisione intera
            if self._words[mid] == word:
                return True
            elif self._words[mid] < word:
                low = mid + 1
            else:
                high = mid - 1
        return False


    # @property
    # def dict(self):
    #     return self._dict


