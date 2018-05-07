import work_package
import json

def test():
    print('in txt file')
    services = work_package.api_calls.get_services()
    for service in services:
        if service['clientId'] == 1:
            print(json.dumps(service, indent=4))
            
if __name__ == '__main__':
    test()
