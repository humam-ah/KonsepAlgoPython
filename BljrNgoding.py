print('[Bahasa yang tersedia: JavaScript, Python, PHP, Solidity, Java]')
bahasa = input('Bahasa yang Anda Gunakan: ')

match bahasa:
    case "JavaScript":
        print('Anda bisa bekerja sebagai Web Developer')

    case "Python":
        print('Anda bisa bekerja sebagai Data Scientist')

    case "PHP":
        print('Anda bisa bekerja sebagai Backend Developer')

    case "Solidity":
        print('Anda bisa bekerja sebagai Blockchain Developer')

    case "Java":
        print('Anda bisa bekerja sebagai Mobile App Developer')

    case _:
        print('Mohon ketikkan bahasa pemrograman yang ada pada daftar')                    