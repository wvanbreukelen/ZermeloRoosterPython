import Zermelo;

api = Zermelo.API('SCHOOL');

api.getStudentGrid(999, 999999999, 9999999999);

#print(api.callAPI("test", {"test": "test"}));
api.saveToken("CODE");