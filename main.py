"""
R-GAP Exfiltration
This educational project is a POC to test different Air-Gap attack vectors.
(Acoustic, optical, thermal, vibrational, magnetic and electric)
"""

keys = {"0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","/":"-..-.",".":".-.-.-","!":"--..--","?":"..--..","=":"-...-","&":".-...","@":".--.-.","_":"..--.-","kn":"-.--.","sk":"...-.-","ar":".-.-.","bk": "-...-.-"}

def encode():
    secret = input("Encode : ")
    final_secret = ""
    for k in range(len(secret)):
        if secret[k] != " ":
            final_secret += keys[secret[k]] + keys["@"]
        else:
            final_secret += keys["@"] + keys["@"]
    print(final_secret)

def decode(): #unfinished
    secret = input("Decode : ")
    secret = secret.replace(".--.-.","@")
    for k,s in keys.items():
        secret = secret.replace(s,k)
    print(secret)

if __name__ == "__main__":
    encode()
    decode()
