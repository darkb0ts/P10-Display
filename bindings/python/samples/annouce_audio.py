# from gtts import gTTS
import pygame
# import io

# Function to convert text to audio and play it
def text_to_audio(text):
    # Convert text to speech
    # tts = gTTS(text=text, lang='en')
    
    # # Save the speech to a file-like object
    # fp = io.BytesIO()
    # tts.write_to_fp(fp)
    # fp.seek(0)
    
    # Initialize pygame mixer
    pygame.mixer.init()
    
    # # Load the audio file-like object
    # pygame.mixer.music.load(fp, 'mp3')

    pygame.mixer.music.load("naruto_ringtone_best.mp3", 'mp3')
    
    # Play the audio
    pygame.mixer.music.play()
    
    # Wait until the audio is finished playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Example usage
if __name__ == "__main__":
    # text = "Hello, this is a test of text to audio conversion."
    # text_to_audio(text)
    text_to_audio()
