items = ["apple", "banana", "orange", "apple", "mango", "banana"]

unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicate item: ", item)
        # break sirf apple aye ga lakin agr issy hata dy to banana bhi aye ga apple k saat q k break aik baar element dhoond leny pe loop break ker deta hai
    unique_items.add(item)