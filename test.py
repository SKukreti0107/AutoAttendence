import pymysql
from test_Npcap import get_mac_addresses


conn = pymysql.connect(
    host='localhost',
    user='root',
    password='@Ironman0107#',
    database='hack')
cursor = conn.cursor()


ip_range = "192.168.21.0/24"  
devices = get_mac_addresses(ip_range)
script_mac_addresses = [device['mac'] for device in devices]


matched_students = []
for mac_address in script_mac_addresses:
    
    cursor.execute("SELECT Reg_no, Name FROM students WHERE MAC=%s", (mac_address,))
    result = cursor.fetchone()
    if result:
        reg_no, name = result
        matched_students.append({'name': name, 'registration_number': reg_no})


print("Matched Students:")
for student in matched_students:
    print("Name:", student['name'], "| Registration Number:", student['registration_number'])


conn.close()
