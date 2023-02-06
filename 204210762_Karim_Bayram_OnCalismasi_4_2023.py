class Rectangle:
    def __init__(self,Height,Width):
        self.Height=Height;
        self.Width=Width;
    def drawRect(self):
        print('#'*self.Width)
        for i in range(self.Height-2):
            print('#'+' '*(self.Width-2)+'#');
        print('#'*self.Width)
    def isSquare(self):
        x=True if self.Width==self.Height else False;
        return x;
    def setHeight(self,newHeight):
        self.Height=newHeight
    def setWidth(self,newWidth):
        self.Width=newWidth
    def getHeight(self):
        return self.Height;
    def getWidth(self):
        return self.Width;
Rec1=Rectangle(12, 36);
Rec1.drawRect();
print(Rec1.isSquare());
print(Rec1.getHeight());
print(Rec1.getWidth());