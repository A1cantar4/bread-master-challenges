stock = {
    'frances': 10,
    'integral': 6,
    'doce': 5
}

print("\nOlá, seja bem-vindo(a) a padaria mágica! \nPara sair da padaria, digite: sair")

while True:
    type_of_bread = input("\nQual tipo de pão você quer? ").strip().lower()
    if type_of_bread == "sair":
        print("\nAté depois, volte sempre!")
        break
        
    elif type_of_bread not in stock:
        print("\nNão vendemos esse tipo de pão, escolha entre: \nFrances, Integral e Doce")
        continue
    
    try:
        quantity = int(input(f"\nQuantos pães do tipo {type_of_bread} você deseja? "))
        if quantity <= 0:
            print("Quantidade inválida")
            continue
    except ValueError:
        print("Digite um número válido por favor!")
        continue
     
    if quantity > stock[type_of_bread]:
        print(f"\nNão possuímos essa quantidad de pão {type_of_bread}")
    
    else:
        stock[type_of_bread] -= quantity
        print(f"\nValeu, pedido confirmado!")
        print(f"\nNo sistema informa que possui {stock[type_of_bread]} pães {type_of_bread}")
        print("\nESTOQUE FINAL:", stock)    

print("Saindo da padaria! ")