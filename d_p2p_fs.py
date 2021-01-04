from lib_and_protocol import *
from client import Client
from server import Server


class d_p2p_fs:
    peers = ['127.0.0.1']

def main():

    sample_msg = file_access.in_byte()
    while True:
        try:
            print("Establishing Connection...")
            time.sleep(randint(TIME_START,TIME_END))
            for peer in d_p2p_fs.peers:
                try:
                    client = Client(peer)
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass


                # become the server
                try:
                    server = Server(sample_msg)
                except KeyboardInterrupt:
                    sys.exit()
                except:
                    pass

        except KeyboardInterrupt as e:
            sys.exit(0)

if __name__ == "__main__":
    main()
