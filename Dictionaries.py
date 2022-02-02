price_list = {
    "CPU" : "26,000",
    "GPU" : "43,000",
    "RAM" : "8,000",
    "SSD" : "21,000",
    "CASE":"8,000",
    "BOARD":"25,000"
}

# A dictionary is defined with name of the dictionary = curly braces. The elemets are stored in a key:value pair format

print(price_list.get("HDD","Enter a valid key"))   #We can get the value by entering the key using the get function.