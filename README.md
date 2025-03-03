### 🚀 **User Guide for YouTube Downloader & Video Cutter Scripts**  

These scripts allow you to **download a YouTube video**, **save its description and thumbnail**, and **split the video into segments of a specified duration**.  

---

## 📌 **1. Installing Prerequisites**  
Before getting started, make sure you have the following tools installed on your system:  

### 🔧 **1.1 Install Python**  
If you haven’t already, download and install **Python** from:  
🔗 [https://www.python.org/downloads/](https://www.python.org/downloads/)  
Make sure to check **"Add Python to PATH"** during installation.  

### 🔧 **1.2 Install Python Dependencies**  
Open a terminal (CMD, PowerShell, or Terminal on Linux/macOS) and run:  
```bash
pip install yt-dlp requests
```

### 🔧 **1.3 Install FFmpeg**  
FFmpeg is required for **converting and splitting videos**.  

#### ➤ **Windows**  
1. Download **FFmpeg** from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).  
2. Extract the folder and add **the "bin" folder path** to Windows **PATH** environment variables.  
3. Verify the installation by running:  
   ```bash
   ffmpeg -version
   ```

#### ➤ **Linux/macOS**  
Run the following command:  
```bash
sudo apt install ffmpeg  # For Debian/Ubuntu
brew install ffmpeg      # For macOS
```

---

## 📥 **2. Download a YouTube Video**  
Run the `download_video.py` script to download a high-quality YouTube video.  

```bash
python download_video.py
```
It will prompt you for:  
1️⃣ **The YouTube video URL**  
2️⃣ The video will be downloaded in **MP4 format**.  
3️⃣ A **thumbnail** (`.jpg`) and **description** (`.txt`) will be saved in the same folder.  

✅ **Example output:**  
```
🔗 Enter the YouTube video URL: https://www.youtube.com/watch?v=XXXXXXXXXXX
✅ Download complete: video.mp4
📜 Description saved: video_description.txt
🖼️ Thumbnail downloaded: video_thumbnail.jpg
```

---

## ✂️ **3. Split a Video into Segments**  
After downloading a video, use `cut_video.py` to split it.  

```bash
python cut_video.py
```
It will prompt you for:  
1️⃣ **The video name (e.g., `video.mp4`)**  
2️⃣ **The duration of each segment (e.g., 60 seconds)**  
3️⃣ It will create a **folder containing the video segments**.  

✅ **Example output:**  
```
📂 Enter the video name (including extension): video.mp4
⏳ How many seconds per segment? (e.g., 60 for 1 minute): 60
✂️ Splitting complete! The videos are in the 'video' folder.
```

---

## 📂 **4. Generated File Structure**  
After running the scripts, you will get the following structure:  

```
/youtube-video-tool
│── download_video.py       # Script to download the video
│── cut_video.py            # Script to split the video
│── video.mp4               # Downloaded video
│── video_description.txt   # Video description
│── video_thumbnail.jpg     # Video thumbnail
│── /video                  # Folder containing the segments
│   ├── video-part000.mp4
│   ├── video-part001.mp4
│   ├── video-part002.mp4
│   └── ...
```

---

## 🔥 **5. Bonus: Run Both Scripts in One Command**  
You can combine both scripts into a single command:  
```bash
python download_video.py && python cut_video.py
```
This will **download the video** and then **automatically split it**.

---

### 🎯 **Conclusion**  
✅ **Download any YouTube video in MP4 format**  
✅ **Save the description and thumbnail**  
✅ **Split the video into multiple segments**  

If you want **further automation**, we can create a single script to handle everything at once. Let me know if you're interested! 🚀
