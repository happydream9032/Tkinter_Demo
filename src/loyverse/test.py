print("making customers.json")
response_customers = requests.get(
    'https://api.loyverse.com/v1.0/customers', headers=headers)

if response_customers.status_code == 200:
    # Request was successful
    customers_data_array = response_customers.json()

    with open("customers.json", "w") as file:
        json.dump(customers_data_array, file)

print("making stores.json")
response_stores = requests.get(
    'https://api.loyverse.com/v1.0/stores', headers=headers)

if response_stores.status_code == 200:
    # Request was successful
    stores_data_array = response_stores.json()

    with open("stores.json", "w") as file:
        json.dump(stores_data_array, file)


print("making discount.json")
response_discounts = requests.get(
    'https://api.loyverse.com/v1.0/discounts', headers=headers)

if response_discounts.status_code == 200:
    # Request was successful
    discounts_data_array = response_discounts.json()
    temp_array = discounts_data_array["discounts"]

    for temp_item in temp_array:
        ids_array = temp_item["stores"]

        temp_array = []
        for ids_item in ids_array:
            response_stores = requests.get(
                f'https://api.loyverse.com/v1.0/stores/{ids_item}', headers=headers)

            stores_data = response_stores.json()
            temp_array.append(stores_data)

        temp_item["stores"] = temp_array

    with open("stores.json", "w") as file:
        json.dump(stores_data_array, file)


print("making employees.json")
response_employes = requests.get(
    'https://api.loyverse.com/v1.0/employees', headers=headers)

if response_employes.status_code == 200:
    # Request was successful
    employes_data_array = response_employes.json()
    temp_array = employes_data_array["employees"]

    for temp_item in temp_array:
        ids_array = temp_item["stores"]

        temp_array = []
        for ids_item in ids_array:
            response_stores = requests.get(
                f'https://api.loyverse.com/v1.0/stores/{ids_item}', headers=headers)

            stores_data = response_stores.json()
            temp_array.append(stores_data)

        temp_item["stores"] = temp_array

    with open("employees.json", "w") as file:
        json.dump(employes_data_array, file)


print("making inventory.json")
response_inventory = requests.get(
    'https://api.loyverse.com/v1.0/inventory', headers=headers)

if response_inventory.status_code == 200:
    # Request was successful
    inventory_data_array = response_inventory.json()

    with open("inventory.json", "w") as file:
        json.dump(inventory_data_array, file)


print("making merchant.json")
response_merchant = requests.get(
    'https://api.loyverse.com/v1.0/merchant', headers=headers)

if response_merchant.status_code == 200:
    # Request was successful
    merchant_data_array = response_merchant.json()

    with open("merchant.json", "w") as file:
        json.dump(merchant_data_array, file)


print("making modifiers.json")
response_modifiers = requests.get(
    'https://api.loyverse.com/v1.0/modifiers', headers=headers)

if response_modifiers.status_code == 200:
    # Request was successful
    modifiers_data_array = response_modifiers.json()
    temp_array = modifiers_data_array["modifiers"]

    for temp_item in temp_array:
        ids_array = temp_item["stores"]

        temp_array = []
        for ids_item in ids_array:
            response_stores = requests.get(
                f'https://api.loyverse.com/v1.0/stores/{ids_item}', headers=headers)

            stores_data = response_stores.json()
            temp_array.append(stores_data)

        temp_item["stores"] = temp_array

    with open("modifiers.json", "w") as file:
        json.dump(modifiers_data_array, file)

print("making payment_types.json")
response_payment_types = requests.get(
    'https://api.loyverse.com/v1.0/payment_types', headers=headers)

if response_payment_types.status_code == 200:
    # Request was successful
    payment_types_data_array = response_payment_types.json()
    temp_array = payment_types_data_array["payment_types"]

    for temp_item in temp_array:
        ids_array = temp_item["stores"]

        temp_array = []
        for ids_item in ids_array:
            response_stores = requests.get(
                f'https://api.loyverse.com/v1.0/stores/{ids_item}', headers=headers)

            stores_data = response_stores.json()
            temp_array.append(stores_data)

        temp_item["stores"] = temp_array

    with open("payment_types.json", "w") as file:
        json.dump(payment_types_data_array, file)


print("making pos_devices.json")
response_pos_devices = requests.get(
    'https://api.loyverse.com/v1.0/pos_devices', headers=headers)

if response_pos_devices.status_code == 200:
    # Request was successful
    pos_devices_data_array = response_pos_devices.json()
    temp_array = pos_devices_data_array["pos_devices"]

    for temp_item in temp_array:
        ids_item = temp_item["store_id"]

        response_stores = requests.get(
            f'https://api.loyverse.com/v1.0/stores/{ids_item}', headers=headers)

        stores_data = response_stores.json()

        temp_item["stores"] = stores_data

    with open("pos_devices.json", "w") as file:
        json.dump(pos_devices_data_array, file)
