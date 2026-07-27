email="Amit_ml@gmail.edu"
def analyze_email(email):
    """
    check email 
    Args:
    email:str:user email.
    Returns: None.
    """
    #check count "@" in the email
    if email.count("@")!=1:
        print("valid email")
    else:
        print("invaild email")
        
     #user name 
    user_name=email.split("@")[0]
     #domain name
    domain_name=email.split("@")[1].rsplit(".",1) [0]
    print("Usre name:",user_name)
    print("Domain name:",domain_name)
     
     
     
     
     
    # Placeholder for email analysis logic
    pass
