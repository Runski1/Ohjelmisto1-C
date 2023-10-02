from rich.console import Console

console = Console(highlight=False)

console.print("Test print")
console.print("[green]Test print (green)")
console.print("[bold]Test print (bold)")
console.print("[bold underline]Test print (bold underline)")

input()
'''from rich.console import Console

console = Console()
console.print("Hello",style= 'Blue')'''

'''speed = 0.08  # kirjoitusnopeus
min_speed = 0.04  # Alin  kirjoitus nopeus
max_speed = 0.1   # Ylin kirjoitus nopeus
for letter in intro_text:
    sys.stdout.write(letter)
    sys.stdout.flush()  # Päivitä näyttö
    time.sleep(speed)  # Käytä muuttujan "nopeus" arvoa odotusaikana
    # Muuta nopeutta satunnaisesti
    speed += random.uniform(-0.01, 0.01)  # Lisää tai vähennä nopeutta pienellä satunnaisella määrällä
    speed = max(min_speed, min(speed, max_speed))  # rajoittaa nopeutta ettei ohjelma kaadu;DD
    # Lopuksi, jätä kursori paikalleen
sys.stdout.write('\n')
'''