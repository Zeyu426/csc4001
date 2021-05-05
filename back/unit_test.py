import pymysql

def get_login(username, password):
    return_data = {
        'status': False,
        'id': 0,
        'role': ""
    }

    # SQL
    conn = pymysql.connect(host = '182.61.17.45', 
                       user = "csc4001",
                       passwd = "123456", 
                       database = "Hospital")
    cur = conn.cursor()

    cur.execute('select id, identity from Account where account = "%s" and password = "%s"'%(username, password))
    result = cur.fetchall()
    if (len(result) == 1):
        return_data['status'] = True
        return_data['id'] = result[0][0]
        return_data['role'] = result[0][1]

    cur.close()
    conn.close()
    return return_data

username = '123456789'
password = '123456789'

return_data = get_login(username, password)
print(return_data)