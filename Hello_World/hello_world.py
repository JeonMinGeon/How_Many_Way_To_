# I mean, How Many Way Are There To Print "Hello, World!"?
# Please... No Matter How it's inefficient and absurd If you see this...
# Add more way to print "Hello, World!" 

## link: https://www.acmicpc.net/problem/2557

# Classic of Classic
print("Hello, World!")

# Using print's sep variable
print("Hello,","World!",sep=" ")
print("Hello","World!",sep=", ")
print("Hell","World!",sep="o, ")
print("Hel","World!",sep="lo, ")
print("He","World!",sep="llo, ")
print("H","World!",sep="ello, ")
print("","World!",sep="Hello, ")
print("Hello","orld!",sep=", W")
print("Hell","orld!",sep="o, W")
print("Hel","orld!",sep="lo, W")
print("He","orld!",sep="llo, W")
print("H","orld!",sep="ello, W")
print("","orld!",sep="Hello, W")
print("Hello","rld!",sep=", Wo")
print("Hell","rld!",sep="o, Wo")
print("Hel","rld!",sep="lo, Wo")
print("He","rld!",sep="llo, Wo")
print("H","rld!",sep="ello, Wo")
print("","rld!",sep="Hello, Wo")
print("Hello","ld!",sep=", Wor")
print("Hell","ld!",sep="o, Wor")
print("Hel","ld!",sep="lo, Wor")
print("He","ld!",sep="llo, Wor")
print("H","ld!",sep="ello, Wor")
print("","ld!",sep="Hello, Wor")
print("Hello","d!",sep=", Worl")
print("Hell","d!",sep="o, Worl")
print("Hel","d!",sep="lo, Worl")
print("He","d!",sep="llo, Worl")
print("H","d!",sep="ello, Worl")
print("","d!",sep="Hello, Worl")
print("Hello","!",sep=", World")
print("Hell","!",sep="o, World")
print("Hel","!",sep="lo, World")
print("He","!",sep="llo, World")
print("H","!",sep="ello, World")
print("","!",sep="Hello, World")
print("Hello","",sep=", World!")
print("Hell","",sep="o, World!")
print("Hel","",sep="lo, World!")
print("He","",sep="llo, World!")
print("H","",sep="ello, World!")
print("","",sep="Hello, World!")



# Using print's end variable
print("Hello, World",end="!\n")
print("Hello, Worl",end="d!\n")
print("Hello, Wor",end="ld!\n")
print("Hello, Wo",end="rld!\n")
print("Hello, W",end="orld!\n")
print("Hello, ",end="World!\n")
print("Hello,",end=" World!\n")
print("Hello",end=", World!\n")
print("Hell",end="o, World!\n")
print("Hel",end="lo, World!\n")
print("He",end="llo, World!\n")
print("H",end="ello, World!\n")
print("",end="Hello, World!\n")



# Using print's sep and end variable
print("Hello,","World",sep=" ",end="!\n")
print("Hello","World",sep=", ",end="!\n")


# Using for
for i in "Hello, World!":
    print(i,end="")