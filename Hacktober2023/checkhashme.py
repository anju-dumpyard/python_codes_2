import hashlib

def calculate_file_hash(file_path, hash_algorithm='sha256', buffer_size=65536):
    """Calculate hash value of a file using the specified hash algorithm."""
    hasher = hashlib.new(hash_algorithm)
    with open(file_path, 'rb') as file:
        buffer = file.read(buffer_size)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = file.read(buffer_size)
    return hasher.hexdigest()

def check_file_hash(file_path, expected_hash, hash_algorithm='sha256'):
    """Check if the calculated hash matches the expected hash value."""
    calculated_hash = calculate_file_hash(file_path, hash_algorithm)
    return calculated_hash == expected_hash

if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")
    expected_hash = input("Enter the expected hash value: ")
    hash_algorithm = input("Enter the hash algorithm (default is sha256): ").lower() or 'sha256'

    try:
        if check_file_hash(file_path, expected_hash, hash_algorithm):
            print("File integrity verified. The hash matches the expected value.")
        else:
            print("File integrity compromised. The hash does not match the expected value.")
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print("An error occurred:", str(e))
