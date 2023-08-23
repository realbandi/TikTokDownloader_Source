from flask import Flask, render_template, request , redirect
import yt_dlp
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/About')
def About():
   return render_template('About.html')

@app.route('/download', methods = ["POST" , "GET"])
def Downloading():
   url =request.form["url"]
   print("Someone just tried to download", url)
   import json
   def extract_tiktok_video_info(video_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': True,
        'dump_single_json': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        return info_dict

   if __name__ == "__main__":
      tiktok_video_url = url
      extracted_info = extract_tiktok_video_info(tiktok_video_url)

      if extracted_info:
         with open("tiktok_video_info.json", "w") as json_file:
               json.dump(extracted_info, json_file, indent=4)
         print("Information saved as tiktok_video_info.json")

         video_url = extracted_info.get('url', None)
         if video_url:
               Download_link = (video_url)
         else:
               print("Video URL extraction failed.")
      else:
         print("Video information extraction failed.")

      return redirect(Download_link+"&dl=1")

if __name__ == '__main__':
   app.run(port=80, debug=True)
