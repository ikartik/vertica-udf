'''

Python round-off UDF

Usage : 
admin=> select roundoff(123.456, 1);
 roundoff 
----------
   123.5
(1 row)

admin=> select roundoff(123.456, 2);
 roundoff 
----------
   123.46
(1 row)


'''
import vertica_sdk
  
class roundoff(vertica_sdk.ScalarFunction):

    def __init__(self):
        pass
    def setup(self, server_interface, col_types):
        pass
    def processBlock(self, server_interface, arg_reader, res_writer):
        server_interface.log("Python UDx - Round off method!")
        while(True):
            first = arg_reader.getDouble(0)
            second = arg_reader.getInt(1)
            res_writer.setFloat(round(first, second))
            res_writer.next()
            if not arg_reader.next():
                break
    def destroy(self, server_interface, col_types):
        pass

class roundoff_factory(vertica_sdk.ScalarFunctionFactory):

    def createScalarFunction(self, srv):
        return roundoff()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addFloat()
        arg_types.addInt()
        return_type.addFloat()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addFloat()
