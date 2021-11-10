from paynow import Paynow
# Integration ID: 12539
# Integration Key: d596aa07-900c-47f5-a56c-7a6c89759c71
import time
paynow = Paynow(
    '12884', 
    '3fba233a-b62e-429a-a9ea-611ad6273e9a',
    'http://localhost:3000/', 
    'http://localhost:3000/'
    )




    payment = paynow.create_payment('Order#{}'.format(str(transaction_data['sendingWallet'])), 'mpasiinnocent@gmail.com')
    # payment.add('Bananas', 2.50)



    response = paynow.send_mobile(payment, '0771111111', 'ecocash')
    # response = paynow.send(payment)
    if(response.success):
        poll_url = response.poll_url

        print("Poll Url: ", poll_url)

        status = paynow.check_transaction_status(poll_url)

        time.sleep(30)

        print("Success Payment Status: ", status.status) 
        if status.status == 'sent':
            print("Sent successfully")
        return status
    else:
        status = response.status
        print("Else Payment Status: ", status)
        return status

def initiate_transaction(data):
    transact = make_payment(data)
    return transact







    # paynow = Paynow(
#     '12884', 
#     '3fba233a-b62e-429a-a9ea-611ad6273e9a',
#     'http://google.com', 
#     'http://google.com'
#     )

# payment = paynow.create_payment('Order #100', 'test@example.com')

# payment.add('Bananas', 2.50)
# payment.add('Apples', 3.40)

# response = paynow.send(payment)