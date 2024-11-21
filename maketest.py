def create_test_file(filename, size_in_mb):
    with open(filename, 'wb') as f:
        f.write(b'\x00' * size_in_mb * 1024 * 1024)

# Hozz létre egy 1 MB méretű fájlt
create_test_file('testfile.bin', 1)