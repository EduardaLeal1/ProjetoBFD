aluno = input ("Digite seu nome: ")
nota1 = float (input("Digite a primeria nota do aluno: "))
nota2 = float (input("Digite a segunda nota do aluno: "))
media = (nota1 + nota2)/2


if media < 7 and media > 4:
    print (f"A média do aluno {aluno} é: {media}, ele está em recuperação.")

elif media >= 7:
    print (f"A média do aluno {aluno} é: {media}, ele está aprovado!")

else:
   print (f"A média do aluno {aluno} é: {media}, ele está reprovado!") 
