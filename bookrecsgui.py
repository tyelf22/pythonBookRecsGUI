''' Tyson Elfors
5/29/20
CS-1410
Project 3 - Book Reccomendations GUI
'''

"""I declare that the following source code was written solely by me.
I understand that copying any source code, in whole or in part, constitues cheating,
and that I will receive a zero on this project if I am found in violation of this policy."""

from breezypythongui import EasyFrame
import bookrecs

class FriendRecs(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self['background'] = "#99B898"
        self.friends = self.addButton(text="Friends", row=0, column=0, command=self.friendsBox)
        self.reccomend = self.addButton(text="Recommend", row=0, column=1, command=self.recommendBox)
        self.report = self.addButton(text="Report", row=0, column=3, command=self.startRep)
        

    def friendsBox(self):
        EasyFrame.__init__(self)
        self['background'] = "#FFD300" 
        self.addLabel(text = "Friends", row=0, column=0, columnspan=2, sticky="NSEW")
        self.addLabel(text = "Reader:", row=1, column=0)
        self.friendInput = self.addTextField(text="", row=1, column=1)

        self.addLabel(text = "# of Friends:", row=2, column=0)
        self.numberFriendInput = self.addIntegerField(value=2, row=2, column=1)
        self.outputArea = self.addTextArea("", row=4, column=0, columnspan=2, width=50, height=10)

        self.ok = self.addButton(text="Ok", row=3, column=0, command=self.startFriends)
        self.cancel = self.addButton(text="Cancel", row=3, column=1, command=self.__init__)

    def startFriends(self):
        try:
            friend = self.friendInput.getText()
            numFriends = self.numberFriendInput.getNumber()

            bookrecs.dotProd(friend, numFriends)
            self.outputArea.setText(bookrecs.friends(friend, numFriends))
        except TypeError:
            self.messageBox(title="ERROR", message="Reader not found, try again")
    def recommendBox(self):
        EasyFrame.__init__(self)
        self['background'] = "#355C7D"
        self.addLabel(text = "Recommendations", row=0, column=0, columnspan=2, sticky="NSEW")
        self.addLabel(text = "Reader:", row=1, column=0)
        self.recFriend = self.addTextField(text="", row=1, column=1)

        self.addLabel(text = "# of Friends:", row=2, column=0)
        self.recFriendNum = self.addIntegerField(value=2, row=2, column=1)

        self.recOutputArea = self.addTextArea("", row=4, column=0, columnspan=2, width=50, height=10)

        self.ok = self.addButton(text="Ok", row=3, column=0, command=self.startRecs)
        self.cancel = self.addButton(text="Cancel", row=3, column=1, command=self.__init__)

    def startRecs(self):
        try:
            friend = self.recFriend.getText()
            numFriends = self.recFriendNum.getNumber()

            bookrecs.dotProd(friend, numFriends)
            bookrecs.friends(friend, numFriends)
            self.recOutputArea.setText(bookrecs.recommend(friend, numFriends))

        except TypeError:
            self.messageBox(title="ERROR", message="Reader not found, try again")
    
    def startRep(self):
        self.repOutputArea = self.addTextArea("", row=5, column=0, columnspan=2, width=50, height=15)
        self.repOutputArea['background'] = "#F8B195"
        self.repOutputArea.setText(bookrecs.report())
        
def main():
    FriendRecs().mainloop()

if __name__ == "__main__":
    main()