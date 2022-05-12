from datetime import datetime, timedelta
from time import strftime


class ControlerEmail():

    def __init__(self, host:str, por:int=None) -> None:  

        # // CONEXION WITH HOST // #

        from imaplib import IMAP4_SSL
        self.conexion = IMAP4_SSL(host)                   

    def login(self, user:str, key:str) -> bool:

        # // AUTHENTICATION // #

        self.conexion.login(user,key)
        return True        
                
    def select_email_folder(self, past_name:str, only_read=True):

        # // SELECT PAST // #

        self.conexion.select(past_name, only_read)        

    def get_all_ids(self) -> bytes:

        # // RETURN ALL ID IN THE FOLDER // #

        return self.conexion.search(None, "All")

    def get_from_id(self, from_email ) -> bytes:

        # // RETURN ID IN THE FOLDER WITH CONDITION : FROM // #

        return self.conexion.search(None, 'From', from_email)

    def get_date_id(self, since:str="01/01/2000", before:str="01/01/2050"):

        # // I NEED THINKING BETTER // :S #

        # // RETURN ID IN THE FOLDER WITH CONDITION DATE : ONLY SINCE OR ONLY BEFORE OR SINCE AND BEFORE // #   
             
        before = datetime.strftime(datetime.strptime(before,"%d/%m/%Y"), '%d-%b-%Y')         

        since = datetime.strftime(datetime.strptime(since,"%d/%m/%Y"), '%d-%b-%Y')

        return self.conexion.search(None, f'(SINCE "{since}" BEFORE "{before}")')       
        


my_controler = ControlerEmail('HOSTNAME')
my_controler.login('EMAIL_USER','KEY')
my_controler.select_email_folder("Inbox")
print(my_controler.get_date_id(before='11/05/2022'))


        
    

