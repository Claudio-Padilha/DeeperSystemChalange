import json

def generate_obj(projects):
    print
    ret_managers = {}
    ret_watchers = {}

    for project in projects:
        for manager in project['managers']:
            if manager not in ret_managers:
                ret_managers[manager] = []
            
            ret_managers[manager].append({"name": project['name'], "priority": project['priority']})
            
        for watcher in project['watchers']:
            if watcher not in ret_watchers:
                ret_watchers[watcher] = []
            
            ret_watchers[watcher].append({"name": project['name'], "priority": project['priority']})

    for manager in ret_managers:
        ret_managers[manager] = sorted(ret_managers[manager], key=lambda x: x['priority'], reverse=True)

    for watcher in ret_watchers:
        ret_watchers[watcher] = sorted(ret_watchers[watcher], key=lambda x: x['priority'], reverse=True)
    
    return ret_managers, ret_watchers

if __name__ == "__main__":
    f = open('source_file_2.json',)

    projects = json.load(f)

    managers, watchers = generate_obj(projects)

    print(managers)

    for manager in managers:
        for i in range(len(managers[manager])):
            managers[manager][i] = managers[manager][i]['name']

    for watcher in watchers:
        for i in range(len(watchers[watcher])):
            watchers[watcher][i] = watchers[watcher][i]['name']
        
    manager_json = json.dumps(managers)
    watcher_json = json.dumps(watchers)

    with open('managers.json', 'w') as f:
        json.dump(manager_json, f, indent=2)

    with open('watchers.json', 'w') as f:
        json.dump(watcher_json, f, indent=2)
    
    