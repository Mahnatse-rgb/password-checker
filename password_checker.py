def password_is_valid(password):

    if password == '':
       raise Exception('password should exist')

    elif len(password) <= 8:
        raise Exception('password should be longer than than 8 characters')

    elif not any( c.islower() for c  in password):
        raise Exception('password should have at least one lowercase letter')
        
    elif not any( c.isupper for c in password):
        raise Exception('password should have at least one uppercase letter')
            
    elif not any(c.isdigit for c in password):
         raise Exception('password should at least have one digit')

    elif all( c.isalnum() for c in password):
        raise Exception('password should have at least one special character')

    else: 
        print("password_is_valid")

password_is_valid



def password_is_ok(password):

    if password != '' and len(password) > 8 and any( c.islower() for c  in password):
        return True

    else:
        return False
        #print('the password is never OK if conditions 1 and 2 are not met.')
    

password_is_ok