import pymongo
import gridfs

if __name__ == '__main__':
    # read in the image.

    datafile = open(r'C:\Users\Ismail\Downloads\photo.jpg',encoding="utf-8")
    thedata = datafile.read()

    # connect to database

    connection = pymongo.Connection("localhost", 27017)
    database = connection['example']

    # create a new gridfs object.
    fs = gridfs.GridFS(database)

    # store the data in the database. Returns the id of the file in gridFS
    stored = fs.put(thedata, filename="testimage")

    # retrieve what was just stored.
    outputdata = fs.get(stored).read()

    # create an output file and store the image in the output file
    outfilename = "path to output file"
    output = open(outfilename, "w")

    output.write(outputdata)
    # close the output file
    output.close()

    # for experimental code restore to known state and close connection
    fs.delete(stored)
    connection.drop_database('example')
    #    print(connection.database_names())
    connection.close()



