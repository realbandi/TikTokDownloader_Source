import yt_dlp
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
    tiktok_video_url = "https://www.tiktok.com/@sehamfc/video/7245301396969377030"
    extracted_info = extract_tiktok_video_info(tiktok_video_url)

    if extracted_info:
        with open("tiktok_video_info.json", "w") as json_file:
            json.dump(extracted_info, json_file, indent=4)
        print("Information saved as tiktok_video_info.json")

        video_url = extracted_info.get('url', None)
        if video_url:
            print("Extracted Video URL:", video_url)
        else:
            print("Video URL extraction failed.")
    else:
        print("Video information extraction failed.")
