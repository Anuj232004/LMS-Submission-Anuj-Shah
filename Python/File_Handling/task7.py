try:
    # Attempt to open and read a non-existent file
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print("File content:\n", content)

# Specific exception if the file does not exist
except FileNotFoundError:
    print("Error: The file does not exist.")

# Catch all other exceptions
except Exception as e:
    print("An unexpected error occurred:", e)

# Optional: finally block executes no matter what
finally:
    print("File operation attempt complete.")