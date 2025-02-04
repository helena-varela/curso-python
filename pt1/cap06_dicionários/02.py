#6.2 – Números favoritos: Use um dicionário para armazenar os números favoritos
#de algumas pessoas. Pense em cinco nomes e use-os como chaves em seu
#dicionário. Pense em um número favorito para cada pessoa e armazene cada um
#como um valor em seu dicionário. Exiba o nome de cada pessoa e seu número
#favorito. Para que seja mais divertido ainda, faça uma enquete com alguns amigos
#e obtenha alguns dados reais para o seu programa.

numeros_favoritos = {'fulano': 20, 
                     'ciclano': 13, 
                     'beltrano': 10, 
                     'maria': 22, 
                     'juliana': 6,
                     }

print('o numero favorito de fulano é ' + str(numeros_favoritos['fulano']))
print('o numero favorito de ciclano é ' + str(numeros_favoritos['ciclano']))
print('o numero favorito de beltrano é ' + str(numeros_favoritos['beltrano']))
print('o numero favorito de maria é ' + str(numeros_favoritos['maria']))
print('o numero favorito de juliana é ' + str(numeros_favoritos['juliana']))