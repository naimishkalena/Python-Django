class scheme():

    def __init__(self,scheme_id,scheme_name,outgoing_rate,message_charge):

        self.scheme_id = scheme_id
        self.scheme_name = scheme_name
        self.outgoing_rate = outgoing_rate
        self.message_charge = message_charge

        print("Scheme Name :",scheme_name ," \nScheme Id :",scheme_id,"\nOutgoing Rate : ",outgoing_rate,"\nMessage Charge :",message_charge)

class customer(scheme):

    def __init__(self,name,cust_id,mobile_no):

        self.name = name
        self.cust_id = cust_id
        self.mobile_no = mobile_no

        print("Name : ",name,"\nCustomer Id :",cust_id,"\nMobile No : ",mobile_no)

sch = scheme("007","SAO","200","2.00")
cus = customer("Naimish Kalena",22,7622837322)