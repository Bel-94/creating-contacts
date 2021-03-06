import pyperclip
class Contact: 
    """
     Class that generates new  instances of contacts
     """
    contact_list=[]  #Empty contact list
    def __init__(self,first_name,last_name,phone_number,email):

        #Methods have one extra variable added to the beginning of their parameter list: The self variable.
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New contact first name.
            last_name : New contact last name.
            number: New contact phone number.
            email : New contact email address.
            '''
    # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    #Instance variables are variables that are unique to each new instance of the class. In our example above, we have created four instance variables, that take up the firstname, lastname, number, and email of our new contact.

    #Class variables are variables that belong to the entire class and can be accessed by all instances of the class. Here we create the contact_list variable that will be used to store our created contact objects .

    def save_contact(self):

        # '''
        # save_contact method saves contact objects into contact_list
        # '''

        Contact.contact_list.append(self)

    def delete_contact(self):

        # '''
        # delete_contact method deletes a saved contact from the contact_list
        # '''

        Contact.contact_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
        # '''
        # Method that takes in a number and returns a contact that matches that number.

        # Args:
        #     number: Phone number to search for
        # Returns :
        #     Contact of person that matches the number.
        # '''

        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact

    @classmethod
    def contact_exist(cls,number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                    return True

        return False

    @classmethod
    def display_contacts(cls):
        '''
        method that returns the contact list
        '''
        return cls.contact_list

    @classmethod
    def copy_email(cls,number):
        contact_found = Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)













































































