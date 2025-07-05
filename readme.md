# Export Spotify Playlist to CSV

Ce projet permet d’exporter les pistes d’une playlist Spotify publique dans un fichier CSV.

---

## Fonctionnalités

- Récupère toutes les pistes d’une playlist Spotify (avec gestion de la pagination)
- Extrait le titre, les artistes et l’URL Spotify de chaque piste
- Exporte les données dans un fichier CSV encodé UTF-8

---

## Prérequis

- Python 3.8+
- Un compte développeur Spotify pour récupérer vos identifiants :
  - CLIENT_ID
  - CLIENT_SECRET
- Installer les dépendances :

```bash
pip install -r requirements.txt
```

---

### INSTALLATION

1. Cloner ce dépôt
2. Créer un fichier `.env` à la racine du projet contenant tes identifiants Spotify.

Exemple de contenu pour `.env` :

```env
CLIENT_ID=ta_client_id_spotify
CLIENT_SECRET=ton_client_secret_spotify
```

> ⚠️ Pense à ajouter `.env` dans ton `.gitignore` pour ne pas versionner tes identifiants.

---

### UTILISATION

1. Modifier dans `main.py` la variable `playlist_id` avec l’ID de la playlist à exporter (extrait de l’URL Spotify)
2. Lancer le script :

```bash
python main.py
```

3. Le fichier `playlist_export.csv` sera créé dans le dossier courant

---

### STRUCTURE DU PROJET

- `auth.py` : gestion de l’authentification Spotify
- `spotify_api.py` : récupération des pistes via l’API Spotify
- `exporter.py` : export des données
- `main.py` : script principal d’exécution
- `.env` : fichier de configuration contenant les identifiants (non versionné)

---

### NOTES

- Ce script utilise le Client Credentials Flow Spotify, adapté uniquement aux playlists publiques
- Les playlists privées ou nécessitant une autorisation utilisateur ne sont pas prises en charge

---
