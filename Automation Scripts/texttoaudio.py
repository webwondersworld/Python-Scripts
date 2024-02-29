import PyPDF2
import pyttsx3

pdfreader = PyPDF2.PdfReader(open('story.pdf', 'rb'))
speaker = pyttsx3.init()
output_text = ''
for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    cleaned_text = text.strip().replace('\n', ' ')
    print(f"Cleaning Page {page_num}")
    output_text += cleaned_text
    print(f"Appended Page {page_num} to Output")

print("Conversion to Audio has started!")
speaker.save_to_file(output_text, 'story.mp3')
speaker.runAndWait()
print("Conversion Completed! Please hear it.")
speaker.stop()
