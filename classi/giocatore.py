from classi.banco import banco


class giocatore:


    def __init__(self,nome,soldi):
        self.__nome = nome
        assert isinstance(soldi,int) > 0 , "non valido"
        self.__soldi = soldi
        self.__carte = []   # CARTE ESTRATTE
        self.__tot_carte = 0
        self.__scommessa = 0


    def set_carte(self, carta):
        self.__carte.append(carta)
        if carta.get_numero() == 1:
            self.__tot_carte += 11
        elif carta.get_numero() == 'J' or carta.get_numero() == 'K' or carta.get_numero() == 'Q':
            self.__tot_carte += 10
        else:
            self.__tot_carte += carta.get_numero()
        if self.__tot_carte > 21:
            for i in self.__carte:
                if i.get_numero() == 1:
                    self.__tot_carte -= 10

    def get_soldi(self):
        return self.__soldi
    
    def get_nome(self):
        return self.__nome

    def get_scommessa(self):
        return self.__scommessa

    def set_soldi(self, soldi):
        self.__soldi = soldi

    def get_carte(self):
        return self.__carte

    def str_carte(self):
        carte = []
        if isinstance(self.get_carte(),list):
            for i in self.get_carte():
                carte.append(str(i))
            return carte
        else:
            return str(self.get_carte())

    def get_totale(self):
        return self.__tot_carte

    def scommetti(self,scommessa):
        if scommessa < self.__soldi:
            self.__soldi -= scommessa
            self.__scommessa = scommessa
        else:
            return False

    def turno_giocatore(self):
        x = 0
        cont = 0
        while x != 3:
            print('1 - Shtatt ferm')
            print('2 - Chiedi carta')
            if cont == 0:
                print('3 - Raddoppia')

            x = input("Scegli la mossa:  ")

            if x == '2':
                banco.distribuisci(self)
                print("-------------------------------------")
                print("Carte:  ",self.str_carte())
                print("Totale:  ",self.get_totale())
                print("Soldi:  ",self.get_soldi())

                if self.__tot_carte == 21:
                    if len(self.get_carte()) == 2:
                        print('BJ')
                    else:
                        print('21')
                elif self.__tot_carte > 21:
                    print('Sballato')
                    break

            elif x == '3' and cont == 0:
                raddoppio = self.__scommessa * 2
                self.__soldi -= self.__scommessa
                banco.distribuisci(self)
                print("-------------------------------------")
                print("Carte:  ",self.str_carte())
                print("Totale:  ",self.get_totale())
                print("Soldi:  ",self.get_soldi())

                if self.__tot_carte == 21:
                    if len(self.get_carte()) == 2:
                        print('BJ')
                    else:
                        print('21')
                elif self.__tot_carte > 21:
                    print('Sballato')
                break
            else:
                break

            cont+=1
