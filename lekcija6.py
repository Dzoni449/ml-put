naslov = input("Naslov: ").strip()
ima_hashtag = "#" in naslov

if ima_hashtag:
    print("Ima hashtag.")

if 10 <= len(naslov) <= 60:
    print("Duzina je OK.") 

if "python" in naslov.lower() and ima_hashtag:
    print("Python klip sa hashtagom.")


if not naslov:
    print("Nisi uneo naslov")