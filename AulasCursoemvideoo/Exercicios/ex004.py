c = input('\033[97mDigite algo: \033[m')                    # recebendo algo
print(type(c))                                              # escrevendo o tipo de algo
print("{} é alfanumérico: {}".format(c, c.isalnum()))        # dizendo se algo é alfanumérico
print("{} é numérico: {}".format(c, c.isnumeric()))          # dizendo se algo é numérico
print("{} é escrita: {}".format(c, c.isalpha()))             # dizendo se algo é alpha
print("{} está em maiuscula: {}".format(c, c.isupper()))     # dizendo se algo é maiúsculo
print("{} é um espaço: {}".format(c, c.isspace()))           # dizendo se algo é apenas espaços
