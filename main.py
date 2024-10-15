##### CORES E FORMATAÇÃO NO TERMINAL PYTHON #####

# Base do código de cores
#\033[ Estilo; Cor do texto; Preenchimento m

#Estilos
# 0 - nenhum // 1 - Bold // 4 - Sublinhado // 7 - Negativo
print('\n')

print('ESTILOS')
print('\033[0mSem Estilo\033[m')
print('\033[1mNegrito\033[m')
print('\033[4mSublinhado\033[m')
print('\033[7mNegativo\033[m')
print('\n')

# Cor do Texto 
# 30 - Preto // 31 - Vermelho // 32 - Verde // 33 - Laranja
# 34 - Azul // 35 - Roxo // 36 - Ciano // 37 - Cinza Claro
# 90 - Cinza Escuro // 91 - Vermelho Claro // 92 - Verde Claro
# 93 - Amarelo // 94 - Azul Claro // 95 - Rosa // 96 - Ciano Claro

print('CORES DAS LETRAS')
print(f'\033[30mCor da Letra: Preta\033[m')
print(f'\033[31mCor da Letra: Vermelha\033[m')
print(f'\033[32mCor da Letra: Verde\033[m')
print(f'\033[33mCor da Letra: Laranja\033[m')
print(f'\033[34mCor da Letra: Azul\033[m')
print(f'\033[35mCor da Letra: Roxa\033[m')
print(f'\033[36mCor da Letra: Ciano\033[m')
print(f'\033[37mCor da Letra: Cinza Claro\033[m')
print(f'\033[90mCor da Letra: Cinza Escuro\033[m')
print(f'\033[91mCor da Letra: Vermelho Claro\033[m')
print(f'\033[92mCor da Letra: Verde Claro\033[m')
print(f'\033[93mCor da Letra: Amarelo\033[m')
print(f'\033[94mCor da Letra: Azul Claro\033[m')
print(f'\033[95mCor da Letra: Rosa\033[m')
print(f'\033[96mCor da Letra: Ciano Claro\033[m')
print('\n')

# Preenchimeto
# 40 - Branco // 41 - Vermelho // 42 - Verde 
# 43 - Amarelo // 44 - Azul // 45 - Roxo
# 46 - Azul Claro // 47 - Cinza

print('PREENCHIMENTOS')
print(f'\033[40mPreenchimento Branco\033[m')
print(f'\033[41mPreenchimento Vermelho\033[m')
print(f'\033[42mPreenchimento Verde\033[m')
print(f'\033[43mPreenchimento Amarelo\033[m')
print(f'\033[44mPreenchimento Azul\033[m')
print(f'\033[45mPreenchimento Roxo\033[m')
print(f'\033[46mPreenchimento Azul Claro\033[m')
print(f'\033[47mPreenchimento Cinza\033[m')
print('\n')

# Outros Exemplos
print('OUTROS EXEMPLOS')
print(f'\033[4;43mTexto sublinhado com preenchimento em Amarelo\033[m')
print(f'\033[1;31;44mTexto em negrito com a letra vermelha e preenchimento azul\033[m')
print(f'\033[7;95mTexto em negativo com a letra rosa\033[m')
print(f'\033[7;42mTexto em negativo com o preenchimento verde\033[m')
print('\n')

# Formatação 

string = 'Envelheci dez anos ou mais neste último mês.'
print('String sem formatação')
print(string)
print('\n')

# A Direita
print('# String justificada a direita #')
print(string.rjust(70))
print('\n')
print('# String justificada a direita e preenchida com o carater * #')
print(string.rjust(70, "*"))
print('\n')

# A Esquerda
print('# String justificada a esquerda #')
print(string.ljust(70))
print('\n')
print('# String justificada a esquerda e preenchida com o carater * #')
print(string.ljust(70, "*"))
print('\n')

# Centralizada

print('# String centralizada #')
print(string.center(70))
print('\n')
print('# String centralizada e preenchida com o carater * #')
print(string.center(70, "*"))
