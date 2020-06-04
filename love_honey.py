from twilio.rest import Client 
 
account_sid = 'AC66a32e32487dcfe917a0584608edc1e1' 
auth_token = '7a811e2be201a23c9a5d4594bfd24d4a' 
client = Client(account_sid, auth_token) 
 
def appLove():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:+919966269426' 
                          ) 
 
    print(message.sid)