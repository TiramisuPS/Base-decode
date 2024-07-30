import base64
import sys
import os

def decode_base64(data):
    try:
        return base64.b64decode(data).decode('utf-8')
    except Exception:
        return None

def decode_base32(data):
    try:
        return base64.b32decode(data).decode('utf-8')
    except Exception:
        return None

def decode_base16(data):
    try:
        return base64.b16decode(data).decode('utf-8')
    except Exception:
        return None

def decode_base85(data):
    try:
        return base64.a85decode(data).decode('utf-8')
    except Exception:
        return None

def auto_decode(data):
    decoders = [decode_base64, decode_base32, decode_base16, decode_base85]
    decoded = data
    while True:
        decoded_again = None
        for decoder in decoders:
            result = decoder(decoded)
            if result is not None:
                decoded_again = result
                break
        if decoded_again is None or decoded_again == decoded:
            break
        decoded = decoded_again
    return decoded

def main():
    if len(sys.argv) < 3:
        print("使用方法: python base.py -m '密文' 或 python base.py -r 1.txt")
        sys.exit(1)

    if sys.argv[1] == '-m':
        ciphertext = sys.argv[2]
        decoded_text = auto_decode(ciphertext)
        print("最终解码结果:", decoded_text)
    elif sys.argv[1] == '-r':
        filename = sys.argv[2]
        if not os.path.isfile(filename):
            print("文件不存在")
            sys.exit(1)
        with open(filename, 'r') as file:
            ciphertext = file.read().strip()
            decoded_text = auto_decode(ciphertext)
            print("最终解码结果:", decoded_text)
    else:
        print("无效的选项")
        sys.exit(1)

if __name__ == "__main__":
    main()
