import work_package
import re

def main():
    services = work_package.api_calls.get_services()
    lines = set()
    for service in services:
        for ip in service['ipRanges']:
            if re.fullmatch(work_package.area_regex.north_c, ip):
                if service['note'] == None:
                    print('Client - ' + str(service['clientId']) + ' -- has no note')
                else:
                    lines.add(service['note'])
    print(lines)

if __name__ == "__main__":
    main()
