#   **kwargs

def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

'''go revise dictionary methods'''

print_address(street="123 Main St",
              city="Anytown",
              state="CA",
              apartment = "67",
              zip_code="12345")