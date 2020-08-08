
KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
    ' ': '&',
}


def cifrar(mensage):

    #Se le asignan los llaves al mensaje
    cifrar_mensage = ""
    for llaves in mensage:
        clave = KEYS[llaves]
        cifrar_mensage += clave
    print(cifrar_mensage)

    #Se transforma en el equivalente unicode
    unicode_mensage = []
    for iterar_cifrar_mensage in cifrar_mensage:
        unicode = ord(iterar_cifrar_mensage)
        unicode_mensage.append(unicode)
    print(unicode_mensage)

    #Se binariza el equivalente unicode
    binarizar_unicode = []
    for iterar_unicode_mensage in unicode_mensage:
        binario = format(iterar_unicode_mensage, '0b')
        binarizar_unicode.append(binario)
    print(binarizar_unicode)
    return ' '.join(binarizar_unicode)

def descifrar(mensaje_encriptado):

    division_por_indices = mensaje_encriptado.split()
    print(division_por_indices)

    #Se desbinariza y se convierte en el equivalente unicode
    lista_desbinarizados = []
    for indice_division in range(len(division_por_indices)):
        desbinarizado = int(division_por_indices[indice_division], 2)
        lista_desbinarizados.append(desbinarizado)
    print(lista_desbinarizados)

    #Se devuelve al caracter que corresponde cada numero en unicode
    lista_devolver_uncode = ''
    for indice_lista_desbinarizados in range(len(lista_desbinarizados)):
        quitar_uncode = chr(lista_desbinarizados[indice_lista_desbinarizados])
        lista_devolver_uncode += quitar_uncode
    print(lista_devolver_uncode)

    #Se le asigna la llave a cada valor, para asi formar el mensaje
    descifrar_keys_message = ""
    i = 0
    for letras in lista_devolver_uncode:
        for keys, values in KEYS.items():
            if values == letras:
                descifrar_keys_message += keys
                i =0
    return descifrar_keys_message

def run():

    while True:
        print('-----------------------------------------------------------------------')
        print('                 BIENVENIDO A CRIPTOGRAFIA BINARIA, QUE DESEA HACER?        ')
        print('''\n                     Presione [c] para cifrar mensaje
                     Presione [d] para decifrar mensaje
                     Presione [s] para salir
              ''')
        print('-----------------------------------------------------------------------')
        com = input('Ingrese la opcion que desea: ')
        comando = com.lower()

        if comando == 'c':
            mensage = input('\nEscribe el mensaje: ')
            cifrar_mensaje = cifrar(mensage)
            print('\nCOMANDO ENCRIPTADO')
            print(cifrar_mensaje)

        if comando == 'd':
            mensaje_encriptado = input('Escribe el mensaje encriptado: ')
            descifrar_mensaje =  descifrar(mensaje_encriptado)
            print('\nCOMANDO DESENCRIPTADO')
            print(descifrar_mensaje)

        if comando == 's':
            break


if __name__ == '__main__':
    run()