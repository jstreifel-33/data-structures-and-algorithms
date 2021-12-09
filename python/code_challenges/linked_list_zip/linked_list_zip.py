def linked_list_zip(list_1, list_2):
    node_list_1 = list_1.head
    node_list_2 = list_2.head
    while node_list_1 and node_list_2:
        #do first swap
        placeholder = node_list_1.next
        node_list_1.next = node_list_2
        node_list_1 = placeholder

        #do second swap
        placeholder = node_list_2.next
        node_list_2.next = node_list_1
        node_list_2 = placeholder
    return list_1
