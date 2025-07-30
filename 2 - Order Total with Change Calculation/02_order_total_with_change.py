print("Bem-vindo(a) à padaria!")
print("Se quiser sair, digite: 'sair' ")

debtors = []
options = {'fiado', 'pagar'}

while True:
    name = input("\nOlá, tome seu pão, qual seu nome? ").strip().title()
    
    if name.lower() == 'sair':
        break
        
    if name == "":
        print("Digite um nome válido...")
        continue
  
    # LITTLE LOOP PAYMENT
    while True:
        payment = input("Você irá pagar ou é no fiado? ").strip().lower()
        if payment not in options:
            print("Opção inválida! Digite apenas 'pagar' ou 'fiado'.")
            continue
          
        if payment == 'fiado':
            debtors.append(name)     
            print("\nSeu nome foi adicionado ao caderninho de devedores... Até logo!")
            break
        else:
            print("\nParabéns por optar pagar na hora! Volte sempre!")
            break   
    print("Próximoooo!!!")
    
    
# BOOK OF DEBTORS
print("\n``` CADERDINHO DE DEVEDORES ```")
if not debtors:
    print("Sem devedores hoje") 
else:
    for debtor in debtors:
        print(f"Hoje, {debtor} está devendo!")