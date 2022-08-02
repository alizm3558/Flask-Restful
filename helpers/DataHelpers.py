import os

import mysql.connector

class DataHelpers:
    mydb=mysql.connector.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    passwd=os.environ['MYSQL_PASSWD'],
    database=os.environ['MYSQL_DATABASE']
    )
    mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE deneme (id INT AUTO_INCREMENT PRIMARY KEY, Notlar TEXT)")


    def all_select(self):
        self.mycursor.execute("SELECT * FROM UETDS_ESYA_UN_KODLARI")

        myresult = self.mycursor.fetchall()

        data=[]
        temp_data={}
        for x in myresult:
            temp_data={
        'un_no':x[0],
        'isim':x[1],
        'siniflandirma_kodu':x[2],
        'paketleme_grubu':x[3],

            }
            data.append(temp_data)

        return data


if __name__ == '__main__':
    data_helpers=DataHelpers()
    data_helpers.all_select()