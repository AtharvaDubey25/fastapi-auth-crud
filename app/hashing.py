from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'],deprecated='auto')  # pwd_context is an instance of CryptContext which will use bcrypt algorithm and decrypted=True means if you ever switch to another algoritm it can handle migration

class Hash:
    @staticmethod       # belongs to class not instance
    def bcrypt(password:str):
        return pwd_context.hash(password)    # function to call to hash
    
    @staticmethod
    def verify(plain_password:str,hashed_password:str):
        return pwd_context.verify(plain_password,hashed_password) # verifying the two passwords whether they are the same 0r not
        