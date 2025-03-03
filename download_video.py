import yt_dlp
import os
import requests

def download_best_quality_video(url, output_path="."):
    try:
        ydl_opts = {
            'format': 'bv*+ba/best',  # Meilleure vidéo + meilleur audio
            'merge_output_format': 'mp4',  # Fusionner en MP4
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',  # Convertir en MP4 si nécessaire
            }]
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get("title", "video")
            description = info.get("description", "Aucune description disponible.")
            thumbnail_url = info.get("thumbnail")  # URL de la couverture

            # Enregistrer la description
            desc_file = os.path.join(output_path, f"{title}_description.txt")
            with open(desc_file, "w", encoding="utf-8") as file:
                file.write(description)

            # Télécharger la photo de couverture
            if thumbnail_url:
                img_data = requests.get(thumbnail_url).content
                thumbnail_file = os.path.join(output_path, f"{title}_thumbnail.jpg")
                with open(thumbnail_file, "wb") as img_file:
                    img_file.write(img_data)
                print(f"🖼️ Miniature téléchargée : {thumbnail_file}")

        print(f"✅ Téléchargement terminé : {title}")
        print(f"📜 Description enregistrée : {desc_file}")

    except Exception as e:
        print(f"❌ Erreur lors du téléchargement : {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    video_url = input("Entrez l'URL de la vidéo YouTube : ")
    download_best_quality_video(video_url)
