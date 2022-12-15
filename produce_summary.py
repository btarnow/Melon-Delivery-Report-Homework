def melon_count(day_number, path):
    """This function takes the argument of the day number and path (file name) 
    of the delivery information, and it prints the report.
    """

    print ("DAY", day_number)
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~")

    delivery_log = open(path)

    for line in delivery_log:
        line = line.rstrip()
        words = line.split("|")

        melon_name = words[0]
        count_of_melons = words[1]
        total_cost = words[2]

        print(f"Deliver {count_of_melons} {melon_name}s for total of ${total_cost}")
    
    delivery_log.close()

melon_count(1, "um-deliveries-day-1.txt")
melon_count(2, "um-deliveries-day-2.txt")
melon_count(3, "um-deliveries-day-3.txt")


###This was the provided code. Our task was to make a function to make this code less repetitive!

##ORIGINAL PROVIDED CODE BELOW: 
# #printing out that this is day 1's orders
# print("Day 1")
# #creating a new variable that opens the file with the data for day 1's orders.
# #Note to self-- open() opens files. You need to end with the .close() function like below. 
# the_file = open("um-deliveries-day-1.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-day-2.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-day-3.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()
