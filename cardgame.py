import pygtk
pygtk.require('2.0')
import os
import gtk
import gtk.glade
import sys
import random

class Board:
    def __init__(self):
        self.gladefile = os.path.split(os.path.realpath(sys.argv[0]))[0]+'/'+'cardgame.glade'
        self.builder = gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.CardGameWnd = self.builder.get_object("CardGameWnd")
        self.CardGameFixed = self.builder.get_object("CardGameFixed")

        self.A1 = self.builder.get_object("A1")
        self.A2 = self.builder.get_object("A2")
        self.A3 = self.builder.get_object("A3")
        self.A4 = self.builder.get_object("A4")
        self.A5 = self.builder.get_object("A5")
        self.A6 = self.builder.get_object("A6")
        self.A7 = self.builder.get_object("A7")
        self.DeckA = self.builder.get_object("DeckA")
        self.DeckNumA = self.builder.get_object("DeckNumA")
        self.B1 = self.builder.get_object("B1")
        self.B2 = self.builder.get_object("B2")
        self.B3 = self.builder.get_object("B3")
        self.B4 = self.builder.get_object("B4")
        self.B5 = self.builder.get_object("B5")
        self.B6 = self.builder.get_object("B6")
        self.B7 = self.builder.get_object("B7")
        self.DeckB = self.builder.get_object("DeckB")
        self.DeckNumB = self.builder.get_object("DeckNumB")
        self.P1 = self.builder.get_object("P1")
        self.P2 = self.builder.get_object("P2")
        self.P3 = self.builder.get_object("P3")
        self.P4 = self.builder.get_object("P4")
        self.P5 = self.builder.get_object("P5")
        self.P6 = self.builder.get_object("P6")
        self.P7 = self.builder.get_object("P7")
        self.PlayerA = self.builder.get_object("PlayerA")
        self.PlayerB = self.builder.get_object("PlayerB")
        self.LifeA = self.builder.get_object("LifeA")
        self.ManaA = self.builder.get_object("ManaA")
        self.LifeB = self.builder.get_object("LifeB")
        self.ManaB = self.builder.get_object("ManaB")
        self.OKABtn = self.builder.get_object("OKABtn")
        self.EndABtn = self.builder.get_object("EndABtn")
        self.OKBBtn = self.builder.get_object("OKBBtn")
        self.EndBBtn = self.builder.get_object("EndBBtn")
        self.A1Btn = self.builder.get_object("A1Btn")
        self.A2Btn = self.builder.get_object("A2Btn")
        self.A3Btn = self.builder.get_object("A3Btn")
        self.A4Btn = self.builder.get_object("A4Btn")
        self.A5Btn = self.builder.get_object("A5Btn")
        self.A6Btn = self.builder.get_object("A6Btn")
        self.A7Btn = self.builder.get_object("A7Btn")
        self.B1Btn = self.builder.get_object("B1Btn")
        self.B2Btn = self.builder.get_object("B2Btn")
        self.B3Btn = self.builder.get_object("B3Btn")
        self.B4Btn = self.builder.get_object("B4Btn")
        self.B5Btn = self.builder.get_object("B5Btn")
        self.B6Btn = self.builder.get_object("B6Btn")
        self.B7Btn = self.builder.get_object("B7Btn")
        self.P1Btn = self.builder.get_object("P1Btn")
        self.P2Btn = self.builder.get_object("P2Btn")
        self.P3Btn = self.builder.get_object("P3Btn")
        self.P4Btn = self.builder.get_object("P4Btn")
        self.P5Btn = self.builder.get_object("P5Btn")
        self.P6Btn = self.builder.get_object("P6Btn")
        self.P7Btn = self.builder.get_object("P7Btn")
        self.RestLife1 = self.builder.get_object("RestLife1")
        self.RestLife2 = self.builder.get_object("RestLife2")
        self.RestLife3 = self.builder.get_object("RestLife3")
        self.RestLife4 = self.builder.get_object("RestLife4")
        self.RestLife5 = self.builder.get_object("RestLife5")
        self.RestLife6 = self.builder.get_object("RestLife6")
        self.RestLife7 = self.builder.get_object("RestLife7")
        self.Side1 = self.builder.get_object("Side1")
        self.Side2 = self.builder.get_object("Side2")
        self.Side3 = self.builder.get_object("Side3")
        self.Side4 = self.builder.get_object("Side4")
        self.Side5 = self.builder.get_object("Side5")
        self.Side6 = self.builder.get_object("Side6")
        self.Side7 = self.builder.get_object("Side7")

        self.ABtn = [self.A1Btn,self.A2Btn,self.A3Btn,self.A4Btn,self.A5Btn,self.A6Btn,self.A7Btn]
        self.BBtn = [self.B1Btn,self.B2Btn,self.B3Btn,self.B4Btn,self.B5Btn,self.B6Btn,self.B7Btn]
        self.PBtn = [self.P1Btn,self.P2Btn,self.P3Btn,self.P4Btn,self.P5Btn,self.P6Btn,self.P7Btn]
        self.APic = [self.A1,self.A2,self.A3,self.A4,self.A5,self.A6,self.A7]
        self.BPic = [self.B1,self.B2,self.B3,self.B4,self.B5,self.B6,self.B7]
        self.PPic = [self.P1,self.P2,self.P3,self.P4,self.P5,self.P6,self.P7]
        self.RestLife = [self.RestLife1,self.RestLife2,self.RestLife3,self.RestLife4,self.RestLife5,
                         self.RestLife6,self.RestLife7]
        self.Side = [self.Side1,self.Side2,self.Side3,self.Side4,self.Side5,self.Side6,self.Side7]

        self.AHand1=self.AHand2=self.AHand3=self.AHand4=self.AHand5=self.AHand6=self.AHand7=None
        self.BHand1=self.BHand2=self.BHand3=self.BHand4=self.BHand5=self.BHand6=self.BHand7=None
        self.PCard1=self.PCard2=self.PCard3=self.PCard4=self.PCard5=self.PCard6=self.PCard7=None
        self.RL1 = self.RL2 = self.RL3 = self.RL4 = self.RL5 = self.RL6 = self.RL7 = None
        self.AHand = [self.AHand1,self.AHand2,self.AHand3,self.AHand4,self.AHand5,self.AHand6,self.AHand7]
        self.BHand = [self.BHand1,self.BHand2,self.BHand3,self.BHand4,self.BHand5,self.BHand6,self.BHand7]
        self.PCard = [self.PCard1,self.PCard2,self.PCard3,self.PCard4,self.PCard5,self.PCard6,self.PCard7]
        self.RL = [self.RL1,self.RL2,self.RL3,self.RL4,self.RL5,self.RL6,self.RL7]

        self.ADeck = [Snake,Snake,Crab,Owl,Turtle,Draw2Cards,Draw2Cards,Wolf,AllBack,Ape,Ape,Bear,GunShot,Rhino,
                      Rhino,Tiger,Tiger,Hippo,Hippo,Lion,Elephant,Rex,Fire,Fire,RestForBattle]
        self.BDeck = [Snake,Snake,Crab,Owl,AllBack,Turtle,Draw2Cards,Wolf,Wolf,Ape,Ape,Bear,Bear,Rhino,
                      Rhino,Tiger,Tiger,Hippo,Hippo,Lion,Elephant,Rex,GunShot,MindControl,RestForBattle]
        self.ADeckNum = len(self.ADeck)
        self.BDeckNum = len(self.BDeck)
        self.DeckNumA.set_text(str(self.ADeckNum) + " Cards")
        self.DeckNumB.set_text(str(self.BDeckNum) + " Cards")
        random.shuffle(self.ADeck)
        random.shuffle(self.BDeck)
        self.ALife = self.BLife = 20
        self.AMana = 4
        self.BMana = 2
        self.CurrentPlayer = "A"
        self.LifeA.set_text(str(self.ALife))
        self.LifeB.set_text(str(self.BLife))
        self.ManaA.set_text(str(self.AMana))
        self.ManaB.set_text(str(self.BMana))

        self.A1.set_from_file("desk.png")
        self.A2.set_from_file("desk.png")
        self.A3.set_from_file("desk.png")
        self.A4.set_from_file("desk.png")
        self.A5.set_from_file("desk.png")
        self.A6.set_from_file("desk.png")
        self.A7.set_from_file("desk.png")
        self.B1.set_from_file("desk.png")
        self.B2.set_from_file("desk.png")
        self.B3.set_from_file("desk.png")
        self.B4.set_from_file("desk.png")
        self.B5.set_from_file("desk.png")
        self.B6.set_from_file("desk.png")
        self.B7.set_from_file("desk.png")
        self.DeckA.set_from_file("back.png")
        self.DeckB.set_from_file("back.png")
        self.P1.set_from_file("desk.png")
        self.P2.set_from_file("desk.png")
        self.P3.set_from_file("desk.png")
        self.P4.set_from_file("desk.png")
        self.P5.set_from_file("desk.png")
        self.P6.set_from_file("desk.png")
        self.P7.set_from_file("desk.png")
        self.PlayerA.set_from_file("playera.png")
        self.PlayerB.set_from_file("playerb.png")
        self.OKABtn.set_sensitive(True)
        self.EndABtn.set_sensitive(True)
        self.OKBBtn.set_sensitive(False)
        self.EndBBtn.set_sensitive(False)
        self.A1Btn.set_sensitive(False)
        self.A2Btn.set_sensitive(False)
        self.A3Btn.set_sensitive(False)
        self.A4Btn.set_sensitive(False)
        self.A5Btn.set_sensitive(False)
        self.A6Btn.set_sensitive(False)
        self.A7Btn.set_sensitive(False)
        self.B1Btn.set_sensitive(False)
        self.B2Btn.set_sensitive(False)
        self.B3Btn.set_sensitive(False)
        self.B4Btn.set_sensitive(False)
        self.B5Btn.set_sensitive(False)
        self.B6Btn.set_sensitive(False)
        self.B7Btn.set_sensitive(False)
        self.RestLife1.set_text("")
        self.RestLife2.set_text("")
        self.RestLife3.set_text("")
        self.RestLife4.set_text("")
        self.RestLife5.set_text("")
        self.RestLife6.set_text("")
        self.RestLife7.set_text("")
        self.Side1.set_text("")
        self.Side2.set_text("")
        self.Side3.set_text("")
        self.Side4.set_text("")
        self.Side5.set_text("")
        self.Side6.set_text("")
        self.Side7.set_text("")

        self.DrawCardA()
        self.DrawCardA()
        self.DrawCardA()
        self.DrawCardA()
        self.DrawCardB()
        self.DrawCardB()
        self.DrawCardB()
        self.CardGameWnd.show()

    def DrawCardA(self):
        for i in range(7):
            if self.AHand[i] == None and self.ADeckNum > 0:
                self.AHand[i] = self.ADeck[-1]
                self.ADeck.pop()
                self.APic[i].set_from_file(self.AHand[i].pic)
                self.ABtn[i].set_sensitive(True)
                self.ADeckNum -= 1
                self.DeckNumA.set_text(str(self.ADeckNum) + " Cards")
                break

    def DrawCardB(self):
        for i in range(7):
            if self.BHand[i] == None and self.BDeckNum > 0:
                self.BHand[i] = self.BDeck[-1]
                self.BDeck.pop()
                self.BPic[i].set_from_file(self.BHand[i].pic)
                self.BBtn[i].set_sensitive(True)
                self.BDeckNum -= 1
                self.DeckNumB.set_text(str(self.BDeckNum) + " Cards")
                break

    def AHand_destroy(self,number):
        self.AHand[number] = None
        self.APic[number].set_from_file("desk.png")
        self.ABtn[number].set_sensitive(False)

    def BHand_destroy(self,number):
        self.BHand[number] = None
        self.BPic[number].set_from_file("desk.png")
        self.BBtn[number].set_sensitive(False)

    def PCard_destroy(self,number):
        self.RL[number] = None
        self.RestLife[number].set_text("")
        self.Side[number].set_text("")
        self.PCard[number] = None
        self.PPic[number].set_from_file("desk.png")

    def on_OKABtn_clicked(self, widget):
        for i in range(7):
            if self.ABtn[i].get_active():
                for j in range(7):
                    if self.PBtn[j].get_active():
                        if self.AMana >= self.AHand[i].mana:
                            self.AMana -= self.AHand[i].mana
                            self.ManaA.set_text(str(self.AMana))
                            if str(self.AHand[i].__class__) == "__main__.SpellCards":
                                self.AHand[i].method(main)
                                self.AHand_destroy(i)
                            else:
                                if self.PCard[j] == None:
                                    self.PCard[j] = self.AHand[i]
                                    self.PPic[j].set_from_file(self.AHand[i].pic)
                                    self.RL[j] = self.AHand[i].life
                                    self.RestLife[j].set_text(str(self.RL[j]))
                                    self.Side[j].set_text("A")
                                    self.AHand_destroy(i)
                                elif self.Side[j].get_text() == "A":
                                    r = self.PCard[j]
                                    self.PCard[j] = self.AHand[i]
                                    self.PPic[j].set_from_file(self.AHand[i].pic)
                                    self.RL[j] = self.AHand[i].life
                                    self.RestLife[j].set_text(str(self.RL[j]))
                                    self.AHand[i] = r
                                    self.APic[i].set_from_file(self.AHand[i].pic)
                                else:
                                    rla = self.AHand[i].life - self.PCard[j].attack
                                    rlb = self.RL[j] - self.AHand[i].attack
                                    if rlb > 0:
                                        self.RL[j] = rlb
                                        self.RestLife[j].set_text(str(rlb))
                                        if rla <= 0:
                                            self.AHand_destroy(i)
                                    else:
                                        if rla > 0:
                                            self.PCard[j] = self.AHand[i]
                                            self.PPic[j].set_from_file(self.AHand[i].pic)
                                            self.RL[j] = rla
                                            self.RestLife[j].set_text(str(rla))
                                            self.Side[j].set_text("A")
                                            self.AHand_destroy(i)
                                        else:
                                            self.PCard_destroy(j)
                                            self.AHand_destroy(i)

    def on_OKBBtn_clicked(self, widget):
        for i in range(7):
            if self.BBtn[i].get_active():
                for j in range(7):
                    if self.PBtn[j].get_active():
                        if self.BMana >= self.BHand[i].mana:
                            self.BMana -= self.BHand[i].mana
                            self.ManaB.set_text(str(self.BMana))
                            if str(self.BHand[i].__class__) == "__main__.SpellCards":
                                self.BHand[i].method(main)
                                self.BHand_destroy(i)
                            else:
                                if self.PCard[j] == None:
                                    self.PCard[j] = self.BHand[i]
                                    self.PPic[j].set_from_file(self.BHand[i].pic)
                                    self.RL[j] = self.BHand[i].life
                                    self.RestLife[j].set_text(str(self.RL[j]))
                                    self.Side[j].set_text("B")
                                    self.BHand_destroy(i)
                                elif self.Side[j].get_text() == "B":
                                    r = self.PCard[j]
                                    self.PCard[j] = self.BHand[i]
                                    self.PPic[j].set_from_file(self.BHand[i].pic)
                                    self.RL[j] = self.BHand[i].life
                                    self.RestLife[j].set_text(str(self.RL[j]))
                                    self.BHand[i] = r
                                    self.BPic[i].set_from_file(self.BHand[i].pic)
                                else:
                                    rlb = self.BHand[i].life - self.PCard[j].attack
                                    rla = self.RL[j] - self.BHand[i].attack
                                    if rla > 0:
                                        self.RL[j] = rla
                                        self.RestLife[j].set_text(str(rla))
                                        if rlb <= 0:
                                            self.BHand_destroy(i)
                                    else:
                                        if rlb > 0:
                                            self.PCard[j] = self.BHand[i]
                                            self.PPic[j].set_from_file(self.BHand[i].pic)
                                            self.RL[j] = rlb
                                            self.RestLife[j].set_text(str(rlb))
                                            self.Side[j].set_text("B")
                                            self.BHand_destroy(i)
                                        else:
                                            self.PCard_destroy(j)
                                            self.BHand_destroy(i)

    def on_EndABtn_clicked(self,widget):
        self.BMana += 4
        if self.Side1.get_text() == "B":
            self.BMana += 1
        if self.Side7.get_text() == "B":
            self.BMana += 1
        self.ManaB.set_text(str(self.BMana))

        for i in range(1,6):
            if self.Side[i].get_text() == "B":
                self.ALife -= self.PCard[i].attack
                self.LifeA.set_text(str(self.ALife))
        if self.ALife <= 0:
            self.PlayerA.set_from_file("playeradefeated.png")
        elif self.BDeckNum <= 0:
            self.PlayerB.set_from_file("playerbdefeated.png")

        self.DrawCardB()
        self.CurrentPlayer = "B"
        self.OKABtn.set_sensitive(False)
        self.EndABtn.set_sensitive(False)
        self.OKBBtn.set_sensitive(True)
        self.EndBBtn.set_sensitive(True)

    def on_EndBBtn_clicked(self,widget):
        self.AMana += 4
        if self.Side1.get_text() == "A":
            self.AMana += 1
        if self.Side7.get_text() == "A":
            self.AMana += 1
        self.ManaA.set_text(str(self.AMana))

        for i in range(1,6):
            if self.Side[i].get_text() == "A":
                self.BLife -= self.PCard[i].attack
                self.LifeB.set_text(str(self.BLife))
        if self.BLife <= 0:
            self.PlayerB.set_from_file("playerbdefeated.png")
        elif self.ADeckNum <= 0:
            self.PlayerA.set_from_file("playeradefeated.png")

        self.DrawCardA()
        self.CurrentPlayer = "A"
        self.OKBBtn.set_sensitive(False)
        self.EndBBtn.set_sensitive(False)
        self.OKABtn.set_sensitive(True)
        self.EndABtn.set_sensitive(True)

    def fire(self):
        if self.CurrentPlayer == "A":
            for i in range(7):
                if self.Side[i].get_text() == "B":
                    self.RL[i] -= 2
                    self.RestLife[i].set_text(str(self.RL[i]))
                    if self.RL[i] <= 0:
                        self.PCard_destroy(i)
        else:
            for i in range(7):
                if self.Side[i].get_text() == "A":
                    self.RL[i] -= 2
                    self.RestLife[i].set_text(str(self.RL[i]))
                    if self.RL[i] <= 0:
                        self.PCard_destroy(i)

    def mindcontrol(self):
        for i in range(7):
            if self.PBtn[i].get_active():
                if self.CurrentPlayer == "A":
                    self.Side[i].set_text("A")
                else:
                    self.Side[i].set_text("B")

    def draw2cards(self):
        if self.CurrentPlayer == "A":
            self.DrawCardA()
            self.DrawCardA()
        else:
            self.DrawCardB()
            self.DrawCardB()

    def restforbattle(self):
        if self.CurrentPlayer == "A":
            for i in range(7):
                if self.PBtn[i].get_active() and self.Side[i].get_text() == "A":
                    for j in range(7):
                        if self.AHand[j] == None:
                            self.AHand[j] = self.PCard[i]
                            self.APic[j].set_from_file(self.PCard[i].pic)
                            self.ABtn[j].set_sensitive(True)
                            self.PCard_destroy(i)
                            self.AMana += 3
                            self.ManaA.set_text(str(self.AMana))
                            break
        else:
            for i in range(7):
                if self.PBtn[i].get_active() and self.Side[i].get_text() == "B":
                    for j in range(7):
                        if self.BHand[j] == None:
                            self.BHand[j] = self.PCard[i]
                            self.BPic[j].set_from_file(self.PCard[i].pic)
                            self.BBtn[j].set_sensitive(True)
                            self.PCard_destroy(i)
                            self.BMana += 3
                            self.ManaB.set_text(str(self.BMana))
                            break

    def gunshot(self):
        for i in range(7):
            if self.PBtn[i].get_active() and self.PCard[i] != None:
                self.PCard_destroy(i)
                if i > 0:
                    self.PCard_destroy(i-1)
                if i < 6:
                    self.PCard_destroy(i+1)

    def allback(self):
        for i in range(7):
            if self.Side[i].get_text() == "A":
                for j in range(7):
                        if self.AHand[j] == None:
                            self.AHand[j] = self.PCard[i]
                            self.APic[j].set_from_file(self.PCard[i].pic)
                            self.ABtn[j].set_sensitive(True)
                            self.PCard_destroy(i)
                            break
            elif self.Side[i].get_text() == "B":
                for j in range(7):
                        if self.BHand[j] == None:
                            self.BHand[j] = self.PCard[i]
                            self.BPic[j].set_from_file(self.PCard[i].pic)
                            self.BBtn[j].set_sensitive(True)
                            self.PCard_destroy(i)
                            break

class MinionCards:
    def __init__(self, attack, life, mana, pic):
        self.attack = attack
        self.life = life
        self.mana = mana
        self.pic = pic

Snake = MinionCards(2,1,1,"snake.png")
Crab = MinionCards(1,2,1,"crab.png")
Owl = MinionCards(3,2,2,"owl.png")
Turtle = MinionCards(2,3,2,"turtle.png")
Wolf = MinionCards(4,3,3,"wolf.png")
Ape = MinionCards(3,4,3,"ape.png")
Bear = MinionCards(5,4,4,"bear.png")
Rhino = MinionCards(4,5,4,"rhino.png")
Tiger = MinionCards(6,5,5,"tiger.png")
Hippo = MinionCards(5,6,5,"hippo.png")
Lion = MinionCards(7,6,6,"lion.png")
Elephant = MinionCards(6,7,6,"elephant.png")
Rex = MinionCards(8,8,7,"rex.png")

class SpellCards:
    def __init__(self, mana, pic, method):
        self.mana = mana
        self.pic = pic
        self.method = method

Fire = SpellCards(3,"fire.png",Board.fire)
MindControl = SpellCards(8,"mindcontrol.png",Board.mindcontrol)
Draw2Cards = SpellCards(3,"draw2cards.png",Board.draw2cards)
RestForBattle = SpellCards(0,"restforbattle.png",Board.restforbattle)
GunShot = SpellCards(5,"gunshot.png",Board.gunshot)
AllBack = SpellCards(4,"allback.png",Board.allback)


if __name__ == "__main__":
    main = Board()
    gtk.main()

