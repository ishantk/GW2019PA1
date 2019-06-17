class Login:

    def loginUser(self):
        print(">> Login dear User !!")

class GoogleLogin(Login):

    def loginUser(self, email, password):
        print(">> Google Login Done !!")


class FacebookLogin(Login):

    def loginUser(self, fbUserName, password):
        print(">> Facebook Login Done !!")


class OTPLogin(Login):

    def loginUser(self, phone):
        print(">> OTP Login Done !!")


class Cab:
    def bookCab(self, source, destination):
        print(">> Cab Booked from {} to {}".format(source, destination))

class OLAMicro(Cab):
    def bookCab(self, source, destination):
        print(">> OLA Micro Cab Booked from {} to {}".format(source, destination))

class OLAMini(Cab):
    def bookCab(self, source, destination):
        print(">> OLA Mini Cab Booked from {} to {}".format(source, destination))

class OLASedan(Cab):
    def bookCab(self, source, destination):
        print(">> OLA Sedan Cab Booked from {} to {}".format(source, destination))

# In Python everything is dynamic (RUN TIME)
# Polymorphism : RUN TIME POLYMORPHISM

login = Login()
login.loginUser()

print()

login = GoogleLogin()
login.loginUser("john@example.com", "pass123")

print()

login = OTPLogin()
login.loginUser("+91 99999 88888")

print("***********")
print()

cab = Cab()
cab.bookCab("SilverArc", "MBD")

cab = OLASedan()
cab.bookCab("SilverArc", "MBD")

