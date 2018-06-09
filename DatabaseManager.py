import psycopg2
import DBConnection

def DeleteData():
    conn = psycopg2.connect(**DBConnection.Credentials.DB_PARAMS)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM RankingFIFA')
    conn.commit()
    cursor.close()
    conn.close()

def InsertData(ranking,
        countryName,
        flagLink,
        abbreviation,
        currentPoints,
        rawPoints,
        previousPoints,
        positionDifference,
        positionMovement,
        averagePoints,
        confederation):
    conn = psycopg2.connect(**DBConnection.Credentials.DB_PARAMS)
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO RankingFIFA (ranking, countryName, flagLink, abbreviation, '
                       'currentPoints, rawPoints, previousPoints, positionDiff, positionMovement,'
                       'averagePoints, confederation) '
                       'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (ranking,
                        countryName,
                        flagLink,
                        abbreviation,
                        currentPoints,
                        rawPoints,
                        previousPoints,
                        positionDifference,
                        positionMovement,
                        averagePoints,
                        confederation))
    except psycopg2.Error as error:
        response = error
        status_code = 400
    else:
        response = "Se insertaron los datos con éxito"
        status_code = 200
    conn.commit()
    cursor.close()
    conn.close()
    return response, status_code


def SelectData():
    conn = psycopg2.connect(**DBConnection.Credentials.DB_PARAMS)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM RankingFIFA')
    consult = cursor.fetchall()
    if consult is None:
        response = "No se encontraron datos."
        status_code = 404
    else:
        response = []
        for i in range(0,len(consult)):
            country = {'id': consult[i][0], 'ranking': consult[i][1], 'countryName': consult[i][2], 'flagLink': consult[i][3],
                        'abbreviation': consult[i][4], 'currentPoints': consult[i][5], 'rawPoints': str(consult[i][6]),
                        'previousPoints': consult[i][7],
                        'positionDifference': consult[i][8], 'positionMovement': consult[i][9],
                        'averagePoints': str(consult[i][10]), 'confederation': consult[i][11]}
            response.append(country)
        status_code = 200
    cursor.close()
    conn.close()
    return response, status_code