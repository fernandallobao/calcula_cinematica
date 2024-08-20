# menu
def mostrar_menu():
    print('Informe o que deseja calcula')
    print('1 - Calcular energia potencial.')
    print('2 - Calcular energia cinética.')
    print('3 - Sair do progama.')

def calcular_ep(m, h):
    ep = m*9.8*h
    return ep

def calcular_ec(m, v):
    ec = (m*(v**2))/2
    return ec

