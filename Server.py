import pyotp
import qrcode
import time

def main():
    
    

    # Créer un objet GoogleAuthenticator avec la clé secrète
    ga = pyotp.TOTP('base32secret3232')

    # Générer l'URI de provisionnement pour le QR code
    provisioning_uri = ga.provisioning_uri(name="TP_Securité_informatique")

    # Générer le QR code avec l'URI de provisionnement
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(provisioning_uri)
    qr.make(fit=True)

    # Afficher le QR code à l'utilisateur
    img = qr.make_image(fill='black', back_color='white')
    img.show()

    attempts = 0
    last_valid_token = None
    while attempts < 5:
        # Saisir le jeton OTP côté client
        start_time = time.time()
        user_input = None
        user_input = input("Entrez le jeton OTP de Google Authenticator (ou entrez n'importe quelle lettre pour quitter) : ")
        
                         
           # Si l'utilisateur entre une lettre ou un caractère non numérique, quitter la boucle
        if not user_input.isdigit():
            break

        # Valider le jeton saisi
        if time.time() - start_time > 30:
                last_valid_token = ga.now()
                    # Si aucun jeton a été entré aprés les 30 secondes, afficher le dernier jeton valide
                print("Accès refusé !")    
                print("30 secondes écoulées. Dernier jeton valide :", last_valid_token)
        else:
    # Valider le jeton saisi
                if ga.verify(user_input):
                 print("Accès confirmé !")
                 #  print(time.time() - start_time)
                else:
                  attempts += 1
                  print("Accès refusé !")
                  # print(time.time() - start_time)
                  last_valid_token = ga.now()


    # Si 5 tentatives refusées, fermer l'application
        if attempts == 5:
            print("Trop de tentatives refusées. L'application se ferme.")
            return


                
            
        

if __name__ == "__main__":
    main()
