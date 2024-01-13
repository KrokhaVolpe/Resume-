input_company = input('Enter company: ')
file_name = 'company.txt'

with open(file_name, 'a') as company_send:
    company_send.write(f"{input_company}\n")
    

