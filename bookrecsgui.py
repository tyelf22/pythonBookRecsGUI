from breezypythongui import EasyFrame
import bookrecs

class FriendRecs(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.friends = self.addButton(text="Friends", row=0, column=0, command=self.friendsBox)
        self.reccomend = self.addButton(text="Recommend", row=0, column=1, command=self.recommendBox)
        self.report = self.addButton(text="Report", row=0, column=3)

    def friendsBox(self):
        EasyFrame.__init__(self)
        self.addLabel(text = "Reader:", row=0, column=0)
        self.friendInput = self.addTextField(text="", row=0, column=1)

        self.addLabel(text = "# of Friends:", row=1, column=0)
        self.numberFriendInput = self.addIntegerField(value=2, row=1, column=1)
        self.outputArea = self.addTextArea("", row=3, column=0, columnspan=2, width=50, height=15)

        self.ok = self.addButton(text="Ok", row=2, column=0, command=self.startFriends)
        self.cancel = self.addButton(text="Cancel", row=2, column=1, command=self.__init__)

    def startFriends(self):
        friend = self.friendInput.getText()
        numFriends = self.numberFriendInput.getNumber()

        bookrecs.dotProd(friend, numFriends)
        self.outputArea.setText(bookrecs.friends(friend, numFriends))

    def recommendBox(self):
        EasyFrame.__init__(self)
        self.addLabel(text = "Reader:", row=0, column=0)
        self.recFriend = self.addTextField(text="", row=0, column=1)

        self.addLabel(text = "# of Friends:", row=1, column=0)
        self.recFriendNum = self.addIntegerField(value=2, row=1, column=1)

        self.recOutputArea = self.addTextArea("", row=3, column=0, columnspan=2, width=50, height=15)

        self.ok = self.addButton(text="Ok", row=2, column=0, command=self.startRecs)
        self.cancel = self.addButton(text="Cancel", row=2, column=1, command=self.__init__)

    def startRecs(self):
        friend = self.recFriend.getText()
        numFriends = self.recFriendNum.getNumber()

        bookrecs.dotProd(friend, numFriends)
        bookrecs.friends(friend, numFriends)
        self.recOutputArea.setText(bookrecs.recommend(friend, numFriends))





def main():
    FriendRecs().mainloop()

if __name__ == "__main__":
    main()