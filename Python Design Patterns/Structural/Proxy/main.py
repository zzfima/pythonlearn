from proxy import Proxy

if __name__ == '__main__':
    # Instantiate a Proxy
    proxy = Proxy()

    # Make the proxy: Artist produce until Producer is available
    proxy.produce()

    # Change the state to 'occupied'
    proxy.occupied = "Yes"

    # Make the Producer produce
    proxy.produce()
