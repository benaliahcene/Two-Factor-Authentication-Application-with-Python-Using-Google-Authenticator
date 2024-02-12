Il s’agit d’une application fonctionnant sous Windows qui attend qu’on y saisisse dans un champ de validation le 
jeton de huit (8) chiffres générés par l’application Google Authenticator. Si le jeton est valide dans la période de 60 secondes 
donnée, l’accès est confirmé et l’utilisateur reçoit un message « Accès confirmé ! ». Si le jeton ne correspond 
pas, ou encore si la période de 60 secondes est échue, alors l’utilisateur reçoit un message « Accès refusé ! ». 
Après 5 tentatives refusées, l’application serveur se ferme. L’utilisateur doit alors l’ouvrir à nouveau.


Il faut installer les packages suivants: pyotp & qrcode
