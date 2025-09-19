import math

print("multiplikationstabellen 0-10")
#"yttre loop" för tabellens första faktor
for i in range(0, 11):
    #"inre loop" för tabellens andra faktor
    for j in range(0, 11):
        # Formaterar utskriften så att varje tal tar upp 4 tecken i bredd
        print(f"{i * j:4}", end=" ")
    # Ny rad efter varje tabellrad 
    print()  

