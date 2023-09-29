from user_called_functions import *
# Tuodaan käyttäjän kutsuttavat funktiot ajoa varten, ne on kirjoitettu eri fileen selkeyden takia.
commands_without_parameter = ["search", "hire", "help", "exit"]
# Koska osa funktioista kutsutaan parametrin kanssa, tämä väistää errorin käytettäessä listattuja funktioita


def user_input_processor(input_string):
    # Tämä funktio käsittelee käyttäjäsyötteen:
    # splittaa välilyönnistä listaksi
    input_as_list = input_string.split()
    # etsii listan ensimmäistä alkiota vastaavaa arvoa command_dictionarysta (kts user_called_functions.py)
    selected_function = command_dictionary[input_as_list[0]]
    # Jos käyttäjä ei antanut parametria:
    if len(input_as_list) < 2 and input_as_list[0] in commands_without_parameter:
        selected_function()
        # Kutsuu funktion ilman parametria
    elif len(input_as_list) == 2:
        selected_function(input_as_list[1])
        # kutsuu funktion käyttäen listan toista alkiota parametrina
    else:
        print("Bad parameters.")
        # Todennäköisesti parametri puuttuu tai niitä on annettu kaksi
# while True:
    # Tämä loop on turha lopussa, toimii testauksen ajolooppina
#    user_input_processor(input("[ENTER COMMAND]"))
# HUOM!! Jos importatussa pythonfilessä on jotain ajettavaa, se ajetaan automaattisesti importin yhteydessä.
