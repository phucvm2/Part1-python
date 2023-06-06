import json
import getpass
from napalm import get_network_driver

print ("Insert the Username and Password to login the switch pls:")
username = input ("Username: ")
password=getpass.getpass(prompt='Password: ')

devicelist = ['10.0.82.52',
              '10.0.82.53'
           ]

for devices in devicelist:
    print ("Connect to " + str(devices))
    driver = get_network_driver('ios')
    switch = driver(devices, username, password)
    switch.open()

    print ('Accessing' + str(devices))
    switch.load_merge_candidate(filename='config_vlan.cfg')
    print(switch.compare_config())
    try:
        choice = raw_input ("\nWould you like to commit these changes? [y/N]: ")
    except NameError:
        choice = input ("\nWould you like to commit these changes? [y/N]: ")
    if choice == "y":
       print("Committing......")
       switch.commit_config()
    else:
        print("Discarding.....")
        switch.discard_config()
    switch.close()
    print("Done.")
