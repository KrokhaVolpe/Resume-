def check_company():
    while True:
        file_name = 'company.txt'
        input_company = input('Назва компанії (або "s" для виходу): ')

        if input_company.lower() == 's':
            break

        with open(file_name, 'r') as company_file:
            companies = [line.strip().lower() for line in company_file]

            if input_company.lower() in companies:
                print(f"Резюме для компанії {input_company} вже відправлено.")
            else:
                print("Потрібно відправити резюме.")
                answer_user = input('Додати компанію до списку? Y-так N-Ні: ')

                if answer_user.lower() == 'y':

                    with open('company.txt', 'a') as company_file:
                        company_file.write(input_company.lower() + '\n')
                        print("Компанію додано до списку")



        
check_company()



 
