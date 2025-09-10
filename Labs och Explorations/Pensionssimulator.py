# Skriver ut ett välkomstmeddelande     

print("Välkommen till denna pensionssimulator!") 

# Ber användaren skriva in sitt namn 

namn = input('Vad heter du i förnamn? ') 

# Ber användaren skriva in sin ålder (int=heltal)     

alder = int(input('Hur gammal är du? ')) 

# Uträkning för att komma fram till hur många år det är kvar till pension     

ar_till_pension = 65 - alder 

# Om personen är yngre än 65 skrivs ett meddelande "Hej (namn). Du går i pension om...år.      

if alder < 65: 

    print(f"Hej {namn.lower()}. Du går i pension om {ar_till_pension} år.") 

# Om personen är 65 år eller äldre får den meddelandet "Du kanske redan är pensionär".  

else: 

    print("Du kanske redan är pensionär?") 
