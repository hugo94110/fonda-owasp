## Lancement

```
cp .env.example .env
docker composeup --build
```

Aller à `http://localhost:8000`

## Variables d'environement

```
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_DB
```

## Sécurité

### 1. Sur quoi travaille-t-on ?

On travaille sur une application de transfert/partage de fichiers en ligne avec la possibilité de s'inscrire, se connecter, déposer des fichiers, les télécharger, les partager par lien et les supprimer.

### 2. Qu'est-ce qui peut mal tourner ?

**Surfaces d'entrée**

| Surface     | App                                             |
| ----------- | ----------------------------------------------- |
| Formulaires | Inscription, connexion                          |
| URL         | `/files/{id}`, `/share/{jeton}`                 |
| Cookies     | Cookie de session                               |
| Fichiers    | Upload de fichiers                              |
| API         | Liste des fichiers, création de lien, `/health` |
| Dépendances | `requirements.txt`, images Docker               |

**Les dangers possible**

- **Accès au fichier d'un autre** en changeant l'ID dans l'URL
- **Upload d'un fichier piégé**
- **Lien de partage deviné** ou valable pour toujours
- **Vol de compte** (mdp bruteforce, cookie stole)
- **Disque rempli** par des fichiers très volumineux

### 3. Que fait-on contre ça ?

- Vérifier que le fichier appartient à l'utilisateur connecté
- Renommer les fichiers avec un nom aléatoire, n'autoriser que certaines extensions
- Jeton aléatoire long avec une date d'expiration
- Mots de passe hachés, limite de tentatives, cookies `HttpOnly`
- Taille maximale par fichier et quota par utilisateur

### 4. Avons-nous bien fait ?

Toutes les menaces seront testés et corrigés au fur et à mesure.

## Utilisation de l'IA

Utilisation de claude code pour expliquer la structure à mettre en place ainsi que les subtilitées sur les commandes à utiliser pour lancer et configurer le projet.
