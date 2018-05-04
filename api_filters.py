import work_package.api_calls

statuses = {'Prepared': 0,
            'Active': 1,
            'Ended': 2,
            'Suspended': 3,
            'Prepared Blocked': 4,
            'Obsolete': 5,
            'Deferred': 6
}

def filter_services_by_status(status):
    services_list = []
    for service in services:
        if service['status'] == status:
            list.append(service['id'])

def get_canceled_services():
    return filter_service_by_status(statuses['Ended'])
