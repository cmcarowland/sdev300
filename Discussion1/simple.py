artists:list = []
yourName = input("What is your name?")
print("Enter your favorite artists:")
while True:
    if len(artist := input()) == 0:
        break
    artists.append(artist)
print("Your favorite artists are:")
for art in artists:
    print(f'{art}')