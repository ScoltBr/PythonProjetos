"""
Estruturas condicionais
if (Se), else, elif
"""

idade = 16

"""
# Estrutura condiiconal if, em Java
if(idade < 18){
    system.out.println("Menor de idade");
}else if(idade == 18) {
    system.out.println("Tem 18 anos deidade");
 }else{
    system.out.println("Maior de idade");
}
"""

if idade < 18: # Se idade menor que 18
    print('Menor de idade')
elif idade == 18: # Se idade for igual a 18
    print("Tem 18 anos")
else: # Caso contrario
    print('Maior de Idade')