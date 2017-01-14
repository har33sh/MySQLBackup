import json
from  logger import write_sql

def main():
    config_file=json.load(open("config.json"))
    databases= config_file.keys()
    print databases
    for dbs in databases:
        host=config_file[dbs]["host"]
        user=config_file[dbs]["user"]
        passwd=config_file[dbs]["passwd"]
        db=config_file[dbs]["database"]
        tables = config_file[dbs]["tables"]
        print dbs +" Starting to Backup"
        write_sql(dbs,host,user,passwd,db,tables)
        print dbs +" Backup done"

if __name__ == "__main__":
    main()
