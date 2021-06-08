# **NIRAH-TECHNOLOGY - FAB-LAB 3D-PRINTER**

***Rendre accessible l'impression 3D à moindre cout pour tout le monde.***

- On dispose d'un local qui contient une ou plusieurs imprimantes 3D.
- On dispose d'un application web pour le grand public.
- Les utilisateurs du Grand Public se connectent à notre application web.
- Ils se créént un compte gratuit.
- Ils disposent d'une impression offerte
- On leur fait télécharger un logiciel pour qu'ils dessinent les plans de leur objet
- Ils upload sur notre application web le plan de leur objet à imprimer
- Ils planifient leur impression
- Ils configurent leur impression
- Ils choissent comment ils souhaitent récupérer leur impression
- Ils paient s'il ont déja bénéficié de leur 1ere impression gratuite
- Ils sont notifié (mail / SMS) de chaque étape de l'impression.
- Ils peuvent être livré à domicile par drone ou récupérer leur impression sur place.

## **Liste des micro-services**

### **1. Authentification**
Micro-service en charge de l'authentification des utilisateurs pour le control des accès aux API. 

	Session
		-> Creation
		-> Lecture
		-> Modification
		-> Suppression

### **2. Espace Utilisateur**
Micro-service en charge de la consultation et gestion du profil des utilisateurs.

	Utilisateur
		-> Création
		-> Lecture
		-> Modification
		-> Suppression

### **3. Catalogue**
Micro-service en charge de la consultation et gestion du catalogue des différents objets imprimables.

	Objet 3D
		-> Creation
		-> Lecture
		-> Modification
		-> Suppression

### **4. Panier**
Micro-service en charge de la consultation, de la gestion et du traitement des commandes des utilisateurs.

	Commande
		-> Creation
		-> Lecture
		-> Modification
		-> Suppression

### **5. Paiement**
Micro-service en charge du paiement des commande des utilisateurs.

	Paiment
		-> Creation
		-> Lecture
		-> Modification
		-> Suppression


### **6. Planning**
Micro-service en charge de la plannification des impressions des utilisateurs.

	Impression
		-> Creation
		-> Lecture
		-> Modification
		-> Suppression

### **7. Construction**
Micro-service en charge d'informer les utilisateurs de l'état d'impression des objets 3D.

	Impression d'objet 3D
		-> Creation
		-> Lecture
		-> Modification
		-> Suppression

### **8. Livraison**
Micro-service en charge de gérer les livraisons (livraison à domicile (Drone),récupération sur site) des obets imprimés aux utilisateurs.

    Livraison
		-> Creation
		-> Lecture
		-> Modification
		-> Suppression