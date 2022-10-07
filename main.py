"""
R-GAP Exfiltration
This educational project is a POC to test different Air-Gap attack vectors.
(Acoustic, optical, thermal, vibrational, magnetic and electric)
"""

encode_keys = {"0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","/":"-..-.",".":".-.-.-","!":"--..--","?":"..--..","=":"-...-","&":".-...","@":".--.-.","_":"..--.-","kn":"-.--.","sk":"...-.-","ar":".-.-.","bk": "-...-.-"," ": "SPACE"}

decode_keys = {v: k for k, v in encode_keys.items()}

def encode():
    secret = input("Encode : ")
    final_secret = " ".join(encode_keys[x] for x in secret)
    final_secret = final_secret.replace(" SPACE ", "   ")
    print(final_secret)

def decode():
    secret = input("Decode : ")
    secret = secret.replace("   ", " SPACE ").split(" ")
    final_secret = "".join(decode_keys[x] for x in secret)
    print(final_secret)

if __name__ == "__main__":
    encode()
    decode()
