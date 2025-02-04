import base64
import binascii
import codecs
import itertools

def try_hex_decode(data):
    """ Try to decode Hex """
    try:
        return bytes.fromhex(data).decode("utf-8", errors="ignore")
    except (binascii.Error, ValueError):
        return None

def try_base64_decode(data):
    """ Try to decode Base64 """
    try:
        return base64.b64decode(data).decode("utf-8", errors="ignore")
    except (binascii.Error, ValueError):
        return None

def try_rot13_decode(data):
    """ Try ROT13 decoding """
    return codecs.encode(data, "rot_13")

def xor_decrypt(ciphertext, key):
    """ Decrypt using a repeating XOR key """
    return bytes(c ^ k for c, k in zip(ciphertext, itertools.cycle(key)))

def try_xor_bruteforce(data):
    """ Try all single-byte XOR keys (0-255) """
    raw_bytes = data.encode("latin-1", errors="ignore")
    for key in range(256):
        decrypted = bytes([b ^ key for b in raw_bytes])
        if b"MicroCTF{" in decrypted:
            return decrypted.decode("utf-8", errors="ignore")
    return None

def recursive_decode(data):
    """ Try all decoding methods recursively """
    checked = set()
    
    def decode_step(data):
        if data in checked:  # Prevent infinite loops
            return
        checked.add(data)
        
        print("\n[🔎 Checking:]", data[:50], "...")  # Preview first 50 chars
        
        # If we already see the flag, stop
        if "MicroCTF{" in data:
            print("\n🎉 Found the flag:", data)
            return data
        
        # Try different decodings
        hex_decoded = try_hex_decode(data)
        if hex_decoded and hex_decoded not in checked:
            return decode_step(hex_decoded)

        base64_decoded = try_base64_decode(data)
        if base64_decoded and base64_decoded not in checked:
            return decode_step(base64_decoded)

        rot13_decoded = try_rot13_decode(data)
        if rot13_decoded and rot13_decoded not in checked:
            return decode_step(rot13_decoded)

        xor_decrypted = try_xor_bruteforce(data)
        if xor_decrypted and xor_decrypted not in checked:
            return decode_step(xor_decrypted)
        
        return None

    return decode_step(data)


# Read the flag.txt file and start decryption
with open("flag.txt", "r") as file:
    encrypted_data = file.read().strip()

recursive_decode(encrypted_data)
