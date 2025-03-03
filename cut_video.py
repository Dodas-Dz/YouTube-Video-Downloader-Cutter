import os

# Demander à l'utilisateur le nom de la vidéo
input_video = input("Entrez le nom de la vidéo (avec l'extension, ex: video.mp4) : ")

# Vérifier si le fichier existe
if not os.path.isfile(input_video):
    print("Erreur : le fichier spécifié n'existe pas.")
    exit()

# Extraire le nom de la vidéo sans l'extension
video_name = os.path.splitext(os.path.basename(input_video))[0]

# Demander à l'utilisateur combien de secondes chaque partie doit faire
duration = int(input("Combien de secondes pour chaque segment ? (ex. 60 pour 1 minute) : "))

# Dossier de sortie où les vidéos découpées seront sauvegardées
output_folder = video_name  # Le dossier de sortie porte maintenant le même nom que la vidéo
os.makedirs(output_folder, exist_ok=True)

# Commande FFmpeg pour couper la vidéo en segments de la durée spécifiée par l'utilisateur
command = f'ffmpeg -i "{input_video}" -c copy -map 0 -segment_time {duration} -f segment -reset_timestamps 1 "{output_folder}/{video_name}-part%03d.mp4"'

# Exécution de la commande
os.system(command)

print(f"Découpage terminé ! Les vidéos sont dans le dossier '{output_folder}'.")
