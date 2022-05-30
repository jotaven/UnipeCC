
def morse(texto):
    traducao = ''
    dicionarioMorse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U':'..-', 'V':'...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/', '!': '-.-.--', '?': '..--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ',': '--..--'}

    for c in texto:
        if c in dicionarioMorse:
            #print(dicionarioMorse[c], end=' ')
            traducao += dicionarioMorse[c] + ' '

        else:
            #print(c, end=' ')
            traducao += c+' '
    return traducao

def binario(texto):
    
    return traducao
        
texto = str(input('Digite o que você quer traduzir: ')).upper()
opção = int(input('1. Morse\n2. Binário\nsua opção: '))
if opção == 1:
    traducao = morse(texto)
elif opção == 2:
    traducao = binario(texto)

print(traducao)
