# Write a program that tries to import a non-existent module and handles the ModuleNotFoundError gracefully.
# Suggest a fallback mechanism.
try:
    import reverse
    print("Module loaded.")
except ModuleNotFoundError:
        print("Module Not Found.")
        print("using default mode instead...")

    