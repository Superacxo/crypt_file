def encrypt_file(key, file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    encrypted_data = bytearray(data)
    for i in range(len(data)):
        encrypted_data[i] ^= key[i % len(key)]
    with open(file_path + '.encrypted', 'wb') as f:
        f.write(encrypted_data)
        print(file_path, "📁 encrypted :) ")
Key = input("🔑")
file = input("📁_path")
encrypt_file(b'Key',file)
