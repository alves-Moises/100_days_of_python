#simple function
# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the wather nice today?")
# greet()

#function that aloows fow input

def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"What is it like in {location}")

greet_with_name("Angela", "Nowhere")
greet_with_name("Nowhere", "Angela")
greet_with_name(location="Nowhere", name="Angela")
