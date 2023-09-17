from database.connectDB import get_connection

class model_dropdown:

    @staticmethod
    def get_data():
        connection = get_connection()
        with connection.cursor()as cursor:
            SQL_SELECT = "SELECT left(co_ubigeo,2)as co_ubigeo, de_ubigeo FROM Flask_Ubigeo WHERE right(co_ubigeo," \
                         "4)='0000' "
            cursor.execute(SQL_SELECT)
            result = cursor.fetchall()
            data=[]
            for row in result:
                model_department =model_dropdown()
                model_department.co_ubigeo= row[0]
                model_department.de_ubigeo = row[1]

                data.append(model_department)
        return data

    @staticmethod
    def get_datacity(id_departamento):
        connection = get_connection()
        with connection.cursor() as cursor:
            SQL_SELECTCITY = "select co_ubigeo as id_city,de_ubigeo as city FROM Flask_Ubigeo where right(co_ubigeo," \
                             "2)='00' and  right(co_ubigeo,4)<>'0000' and LEFT(co_ubigeo,2)=%s"

            values =( id_departamento,)
            cursor.execute(SQL_SELECTCITY, values)
            result = cursor.fetchall()
            data = []
            for row in result:
                model_city = model_dropdown()
                model_city.id_city = row[0]
                model_city.city = row[1]

                data.append(model_city)
        return data