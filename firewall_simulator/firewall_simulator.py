'''
1. data structur to store the firewall rules --> Python List
  1.1 individual will be stored a python dictionary (Key:Value pairs)
2. function to add a new rule to the firewall --> add to the previous list in 1
3. function to remove an existing rule from the firewall --> check rule index and remove if valud index
  0,1,2 -> 5 ---> index out of bounds
4. function to simulate the packet filtering operation --> check user i/p against existing rules 
5. main function --> provide a menu for the all the above operations and allow users to give input 
  5.1. allow a user to check all existing firewall rules
'''

firewall_rules = [] 

# add a new firewall rule 
def add_rule(action, src_ip, dst_ip, protocol):
  # add this to the list in line 12 and save each rule as a dictionary object
  firewall_rules.append({'action': action, 'src_ip': src_ip, 'dst_ip': dst_ip, 'protocol': protocol})
  print("Firewall Rule has been successfully added. You can check using Show All Rules...")

# remove a rule 
def remove_rule(rule_index):
  # check if the index is valid: 0 to N-1 where N is size of firewall_rules[]
  if rule_index >= 0 and rule_index < len(firewall_rules):
    firewall_rules.pop(rule_index)
    print("Desired index has been removed from existing Firewall rules")
  else:
    print("Invalid rule index. Please try again. ")



# simulate packet filtering 
def packet_filtering(packet):
  for rule in firewall_rules:
    if (rule['src_ip'] == '*' or rule['src_ip'] == packet['src_ip']) and \
       (rule['dst_ip'] == '*' or rule['dst_ip'] == packet['dst_ip']) and \
       (rule['protocol'] == '*' or rule['protocol'] == packet['protocol']):
      return rule['action']
  return 'DENY'

  

# main function 
def main():
  print("Welcome to the Firewall Simulator Program. Please pick one of the following options")
  while True:
    print("\n 1. Add Rule (press 1)")
    print("2. Remove Rule (press 2)")
    print("3. Simulate Packet Filtering Test (press 3)")
    print("4. Show All Existing Firewall Rules (press 4)")
    print("5. Exit the program (press 5)")
    choice = input("Choose an option between 1 to 5")

    if choice == '1':
      # 4 input from user (src, dest, protocol, action); call function add_rule
      action = input("Enter action (ALLOW/DENY): ")
      src_ip = input("Enter source IP address (or * for any IP): ")
      dst_ip = input("Enter destination IP address (or * for any IP): ")
      protocol = input("Enter protocol TCP/UDP or * for any protocol: ")
      add_rule(action, src_ip, dst_ip, protocol)
    elif choice == '2':
      # index to remove from list; call function to remove the actual content 
      rule_index = int(input("Enter the rule index to remove: "))
      remove_rule(rule_index)
    elif choice == '3':
      # user gives packet to check agains the firewall 
      src_ip = input("Enter source IP: ")
      dst_ip = input("Enter destination IP: ")
      protocol = input("Enter your protocol (TCP/UDP): ")
      packet = {'src_ip': src_ip, 'dst_ip': dst_ip, 'protocol': protocol}
      print("Packet Action: ", packet_filtering(packet))
      
    elif choice == '4':
      # loop over the list and print; when you need both the index and value in each iteration
      for i, rule in enumerate(firewall_rules):
        print(f"{i}: {rule['action']} {rule['src_ip']} -> {rule['dst_ip']} ({rule['protocol']})")
      
    elif choice == '5':
      break
    else:
      print("Invalid choice. Please enter either 1,2,3,4,or 5 ")
  

# calling the main function 
if __name__ == "__main__":
  main()