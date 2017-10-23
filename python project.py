def main():

    # Main game loop
    while True:
       
        
        print_room(current_room)
        print_inventory_items(inventory)

       
        command = menu(current_room["exits"], current_room["items"], inventory)

        execute_command(command)

if __name__ == "__main__":
    main()
