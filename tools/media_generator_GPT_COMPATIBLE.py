# =============================================
# ABL-Compatible Media Generator (Streamlit Secret API Key Version)
# Filename: media_generator_GPT_COMPATIBLE.py
# =============================================

import os
import json
import requests
from io import BytesIO
from pathlib import Path
from PIL import Image
from gtts import gTTS
from openai import OpenAI
import streamlit as st

# === Constants ===
LESSON_ID = "lesson_01_intro_to_pipefitting"
BASE_PATH = Path.home() / "Dropbox" / "EI_Cloud" / "ABL_Rev2_6_1_25" / "lessons" / LESSON_ID
MANIFEST_PATH = BASE_PATH / "lesson_01_manifest.json"
IMAGE_DIR = BASE_PATH / "images"
AUDIO_DIR = BASE_PATH / "audio"
FORCE_REGEN = True

os.makedirs(IMAGE_DIR, exist_ok=True)
os.makedirs(AUDIO_DIR, exist_ok=True)

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# === Functions ===
def build_prompt(text):
    return (
        f"{text} Show a pipefitting environment with OSHA-compliant PPE: hard hat, safety glasses, gloves, "
        f"steel-toe boots, high-vis vest. Flat vector art only. No embedded text."
    )

def generate_image(prompt, output_path):
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1
        )
        image_url = response.data[0].url
        img_data = requests.get(image_url)
        img = Image.open(BytesIO(img_data.content)).convert("RGB")
        img = img.resize((1280, 720), Image.Resampling.LANCZOS)
        img.save(output_path)
        print(f"🖼️ Image saved: {output_path.name}")
    except Exception as e:
        print(f"❌ Image generation failed for {output_path.name}: {e}")

def generate_audio(text, lang_code, output_path):
    try:
        tts = gTTS(text=text, lang=lang_code)
        tts.save(output_path)
        print(f"🔊 Audio saved: {output_path.name}")
    except Exception as e:
        print(f"❌ Audio generation failed for {output_path.name}: {e}")

# === Main ===
def run():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    translations = manifest.get("translations", {})
    segments = manifest.get("segments", [])

    for seg in segments:
        seg_id = seg["id"]
        if not seg_id.startswith("seg_"):
            continue

        en_text = translations.get("en", {}).get(seg_id)
        es_text = translations.get("es", {}).get(seg_id)

        if not en_text:
            print(f"⚠️ No English text for {seg_id}")
            continue

        audio_path_en = AUDIO_DIR / f"{seg_id}_en.mp3"
        audio_path_es = AUDIO_DIR / f"{seg_id}_es.mp3"
        image_path = IMAGE_DIR / f"{seg_id}.png"

        if FORCE_REGEN or not audio_path_en.exists():
            generate_audio(en_text, "en", audio_path_en)
        if FORCE_REGEN and es_text:
            generate_audio(es_text, "es", audio_path_es)
        if FORCE_REGEN or not image_path.exists():
            generate_image(build_prompt(en_text), image_path)

if __name__ == "__main__":
    run()
