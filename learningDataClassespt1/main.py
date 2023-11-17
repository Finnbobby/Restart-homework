from Inventorylibrary import ItemOrigin, InventoryItem

def main():
    item_origin = ItemOrigin(country = "Ethiopia", production_date = "13/11/2023")
    my_item1 = InventoryItem(name = "Printer", 
                             quantity = 25, 
                             serial_number= "2173FC8921EA3",
                             origin = item_origin)
    my_serailized_object1 = my_item1.__dict__
    print(my_serailized_object1)
    my_item2 = InventoryItem(**my_serailized_object1)
    print(my_item2.__dict__)

if __name__ == "__main__":
    main()
