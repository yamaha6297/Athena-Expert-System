#inporting
import os
import csv
import time

#requirements available
requirement_ram = []
requirement_storage = []
requirement_cam = []
requirement_color = []
requirement_so = []
requirement_battery = []


#function to check integer entry
def checkInt(msj):
      while True:
        valor = input(msj)
        try:
            valor = int(valor)
            return valor
        except ValueError:
            return -1

#dialogue for client that exposes requirements
def dialogClientReq():

      requeriments_available()

      global requirement_cam
      global requirement_color
      global requirement_ram
      global requirement_storage
      global requirement_so
      global requirement_battery

      index = 0

      memory = -1
      cam = -1
      storage = -1
      screen = -1
      software = -1
      battery = -1
      color = -1

      #-------- memory requirement --------
      while memory < 0 or memory > len(requirement_ram):
            os.system('clear')
            print("**** Requerimientos ****\n")
            print("Memoria (RAM): \n")
            print("0- No tengo una preferencia")
            i = 1
            for item in requirement_ram:
                  print(str(i) + "- " + str(item) + " GB")
                  i += 1
            memory = checkInt("\nElija una opcion: ")
      if memory == 0: index += 1
      
      #-------- cam requirements --------
      while cam < 0 or cam > len(requirement_cam):
            os.system('clear')
            print("**** Requerimientos ****\n")
            print("Cámara (megapixeles): \n")
            print("0- No tengo una preferencia")
            i = 1
            for item in requirement_cam:
                  print(str(i) + "- " + str(item))
                  i += 1
            cam = checkInt("\nElija una opcion: ")
      if cam == 0: index += 1

      #-------- storage requirements --------
      while storage < 0 or storage > len(requirement_storage):
            os.system('clear')
            print("**** Requerimientos ****\n")
            print("Almacenamiento (interno): \n")
            print("0- No tengo una preferencia")
            i = 1
            for item in requirement_storage:
                  print(str(i) + "- " + str(item) + " GB")
                  i += 1
            storage = checkInt("\nElija una opcion: ")
      if storage == 0: index += 1
      
      #-------- screen requirements --------
      while screen < 0 or screen > 2: 
            os.system('clear')
            print("**** Requerimientos ****\n")
            print("Tamaño de Pantalla (pulgadas): \n")
            print("0- No tengo una preferencia")
            print("1- Menor a 5")
            print("2- Mayor o igual a 5")
            screen = checkInt("\nElija una opcion: ")
      if screen == 0: index += 1

      #-------- software requirements --------
      while software < 0 or software > len(requirement_so):
            os.system('clear')
            print("**** Requerimientos ****\n")
            print("Tamaño de Pantalla (pulgadas): \n")
            print("0- No tengo una preferencia")
            i = 1
            for item in requirement_so:
                  print(str(i) + "- " + str(item))
                  i += 1
            software = checkInt("\nElija una opcion: ")
      if software == 0: index += 1
       
      #-------- battery requirements --------
      while battery < 0 or battery > 2:
            os.system('clear')
            print("**** Requerimientos ****\n")
            print("Bateria (mAh): \n")
            print("0- No tengo una preferencia")
            print("1- Menor a " + str(requirement_battery[0]))
            print("2- Mayor o igual a " + str(requirement_battery[0]))
            battery = checkInt("\nElija una opcion: ")
      if battery == 0: index += 1
      
      #-------- color requirements --------
      while color < 0 or color > len(requirement_color):
            os.system('clear')
            print("**** Requerimientos ****\n")
            print("Color: \n")
            print("0- No tengo una preferencia")
            i = 1
            for item in requirement_color:
                  print(str(i) + "- " + item)
                  i += 1
            color = checkInt("\nElija una opcion: ")
      if color == 0: index += 1

      requeriments = [memory, cam, storage, software, battery, color, screen, index]
      return requeriments

#dialog for client that specifies a sale
def dialogMakeSale():
      print("Venta realizada. Gracias por su compra..!")

#dialog for client that does not specify a sale
def dialogNoMakeSale():
      print("No contamos con celulares disponibles para lo que busca. Disculpe las molestias.")

#dialog for check availability
#ranges: check 'README'
def dialog_check_availability(array):
      #array = [memory, cam, storage, software, battery, color, screen, i]

      requeriments_available()

      global requirement_cam
      global requirement_color
      global requirement_ram
      global requirement_storage

      #values and values range for features
      memory_range = [ 1, 1.5, 2, 3, 4, 6 ]
      cam_range = [ 2, 5, 7, 8, 12, 13, 24, 40 ]
      storage_range = [ 4, 8, 16, 32, 64, 128 ]
      color_values = [ "Blanco", "Dorado", "Negro", "Gris", "Morado"]

      max_rank = 0
      max_ranking = 0
      system_operative = None

      phone_ranking = []

      os.system('clear')
      print("---- Verificando disponibilidad... ----")
      print("---------------------------------------")
      time.sleep(1)
      print("---------------------------------------")
      time.sleep(1)
      print("---------------------------------------")
      time.sleep(1)
      print("---------------------------------------")
      time.sleep(1)
      os.system('clear')
      with open('phones.csv', newline='') as File:  
            reader = csv.DictReader(File)
            for row in reader:

                  rank_recomendation = 0

                  #check memory
                  if array[0] != 0:
                        memory_check = memory_range[array[0] - 1]
                        if float(row['RAM']) == float(memory_check):
                                    rank_recomendation += 1
                                    
                  #check cam
                  if array[1] != 0:
                        cam_check = cam_range[array[1] - 1]
                        if int(row['Camara_trasera']) == int(cam_check):
                              rank_recomendation += 1
                        if int(row['Camara_frontal']) == int(cam_check):
                              rank_recomendation += 1
                        if row['Flash_led_trasero'] == 'SI' or row['Flash_led_frontal'] == 'SI':
                              rank_recomendation += 1

                  #check storage
                  if array[2] != 0:
                        storage_check = storage_range[array[2] - 1]
                        if int(row['Almacenamiento']) == int(storage_check):
                              rank_recomendation += 1
                        if row['Ranura_SD'] == 'SI':
                              rank_recomendation += 1

                  #check software
                  if array[3] != 0:
                        if array[3] == 1:
                              system_operative = 'Android'
                        if array[3] == 2:
                              system_operative = 'iOS'


                  #check batterry
                  if array[4] != 0:
                        if array[4] == 1:
                              if int(row['Bateria']) <= 3000:
                                    rank_recomendation += 1
                        if array[4] == 2:
                              if int(row['Bateria']) > 3000:
                                    rank_recomendation += 1
                  
                  #check color
                  if array[5] != 0:
                        if row['Color'] == color_values[array[5] - 1]:
                              rank_recomendation += 1

                  #check screen
                  if array[6] != 0:
                        if array[6] == 1:
                              if float(row['Pantalla']) <= 5:
                                    rank_recomendation += 1
                        if array[6] == 2:
                              if float(row['Pantalla']) > 5:
                                    rank_recomendation += 1

                  if system_operative != None:

                        if rank_recomendation != 0 and row['Software'] == system_operative:
                              data = {"ID":int(row['ID']), "rank_recomendation": rank_recomendation,"ranking":int(row['Ranking'])}
                              phone_ranking.insert(len(phone_ranking), data)

                              if rank_recomendation > max_rank:
                                    max_rank = rank_recomendation
                              if int(row['Ranking']) > max_ranking:
                                    max_ranking = int(row['Ranking'])
                  else:
                        if rank_recomendation != 0:
                              data = {"ID":int(row['ID']), "rank_recomendation": rank_recomendation,"ranking":int(row['Ranking'])}
                              phone_ranking.insert(len(phone_ranking), data)

                              if rank_recomendation > max_rank:
                                    max_rank = rank_recomendation
                              if int(row['Ranking']) > max_ranking:
                                    max_ranking = int(row['Ranking'])
                  
      phones = []

      index = max_ranking
      while index >= 0:
            for item in phone_ranking:
                  if item['ranking'] == index:
                        phones.insert(len(phones), item)
            index -= 1

      phones_recomendation = []
      index = max_rank
      
      if system_operative == 'iOS':
            number_recomendations = 1
      else:
            number_recomendations = 3

      while len(phones_recomendation) < number_recomendations:
            for item in phones:
                  if item['rank_recomendation'] == index:
                        phones_recomendation.insert(len(phones_recomendation),item)
                        if len(phones_recomendation) > (number_recomendations - 1):
                              break
            index -= 1

      return phones_recomendation       

def dialog_show_options(array):

      print("------- Nuestras recomendaciones -------")
      print("----------------------------------------\n")

      with open('phones.csv', newline='') as File:  
            reader = csv.DictReader(File)
            for row in reader:
                  for item in array:
                      if int(item['ID']) == int(row['ID']):
                              print("Modelo: " + str(row['Modelo']) + ".")
                              print("Camara frontal: " + str(row['Camara_frontal']) + " megapixeles.")
                              print("Flash frontal: " + str(row['Flash_led_frontal']) + ".")
                              print("Camara trasera: " + str(row['Camara_trasera']) + " megapixeles.")
                              print("Flash trasero: " + str(row['Flash_led_trasero']) + ".")
                              print("Pantalla: " + str(row['Pantalla']) + " pulgadas.")
                              print("RAM: " + str(row['RAM']) + " GB.")
                              print("Almacenamiento: " + str(row['Almacenamiento']) + " GB.")
                              print("Ranura SD: " + str(row['Ranura_SD']) + ".")
                              print("Software: " + str(row['Software']) + ".")
                              print("Bateria: " + str(row['Bateria']) + " mAh.")
                              print("Color: " + str(row['Color']) + ".")
                              print("SIM: " + str(row['SIM']) + ".")
                              print("Precio: " + str(row['Precio']) + " $.")
                              print("---------------------------------------------------------------------")
                              print("---------------------------------------------------------------------")

def dialog_evaluate_budget(array):

      check_budget = 0
      index = 0
      phones = []

      while check_budget < 1 or check_budget > index:
            
            index = 2
            print("1 - No me convence ninguno de los modelos presentados")
            
            with open('phones.csv', newline='') as File:  
                  reader = csv.DictReader(File)

                  for row in reader:
                        for item in array:                  
                        
                              if int(row['ID']) == item['ID']:
                                    phones.insert(len(phones),int(row['ID']))
                                    print(str(index) + " - Modelo: " + str(row['Modelo']) + ". Precio: " + str(row['Precio']) + " $.")
                                    index += 1

                  if len(array) == 1:
                        print("\nTambien contamos con una version similar en Android. \n")
                        if array[0]['ID'] == 17:
                              phones.insert(len(phones),16)
                              print(str(index) + " - Modelo: Huawei P9. Precio: 11500 $.")
                        elif array[0]['ID'] == 18:
                              phones.insert(len(phones),4)
                              print(str(index) + " - Modelo: Galaxy S8. Precio: 21000 $.")
                        elif array[0]['ID'] == 19:
                              phones.insert(len(phones),5)
                              print(str(index) + " - Modelo: Galaxy S9. Precio: 31100 $.")

            check_budget = checkInt("Elija una opcion: ")

            id_choise = phones[check_budget - 2] 

            in_file = open('phones.csv', 'r')
            reader = csv.reader(in_file)
            in_list = list(reader)
            in_file.close()

            _index = False
            for item in in_list:
                  if _index:
                        if int(item[0]) == int(id_choise):
                              item[len(item)-1] = int(item[len(item)-1]) + 1
                  if not(_index):
                        _index = True

            out_file = open('phones.csv', 'w', newline = '')
            writer_list = csv.writer(out_file)
            writer_list.writerows(in_list)
            out_file.close()    


      return check_budget

def dialog_consult_use():

      requeriments_available()

      range_sn = [ [1, 2], [3, 4] ]
      range_apps = [ [1, 2], [5, 6] ]
      range_cam = [ [1, 2], [4, 5] ]
      range_size = [ 1, 2]

      social_network = -1
      apps = -1
      cam = -1
      size_screen = -1

      while social_network < 0 or social_network > 1:
            os.system('clear')
            print("------- Usos del cliente -------")
            print("--------------------------------\n")
            print("Utiliza redes sociales?\n")
            print("1- NO\n")
            print("2- SI\n")
            social_network = checkInt("Elija su opcion: ") - 1
      
      while apps < 0 or apps > 1:
            os.system('clear')
            print("------- Usos del cliente -------")
            print("--------------------------------\n")
            print("Utiliza muchas aplicaciones?\n")
            print("1- NO\n")
            print("2- SI\n")
            apps = checkInt("Elija su opcion: ") - 1
      
      while cam < 0 or cam > 1:
            os.system('clear')
            print("------- Usos del cliente -------")
            print("--------------------------------\n")
            print("Le gusta sacar fotos?\n")
            print("1- NO\n")
            print("2- SI\n")
            cam = checkInt("Elija su opcion: ") - 1
      
      while size_screen < 0 or size_screen > 1:
            os.system('clear')
            print("------- Usos del cliente -------")
            print("--------------------------------\n")
            print("Lo utiliza para leer archivos o ver contenidos?\n")
            print("1- NO\n")
            print("2- SI\n")
            size_screen = checkInt("Elija su opcion: ") - 1

      #array = [memory, cam, storage, software, battery, color, screen, i]
      
      uses_requeriments_min = [range_sn[social_network][0], 
                               range_cam[cam][0],
                               range_apps[apps][0],
                               1, 2, 0, 
                               range_size[size_screen], 5]

      uses_requeriments_max = [range_sn[social_network][1], 
                               range_cam[cam][1],
                               range_apps[apps][1],
                               1, 2, 0, 
                               range_size[size_screen], 6]
      
      return [uses_requeriments_min, uses_requeriments_max]

def requeriments_available():

      global requirement_cam
      global requirement_color
      global requirement_ram
      global requirement_storage
      global requirement_so
      global requirement_battery

      with open('phones.csv', newline='') as File:  

            reader = csv.DictReader(File)

            for row in reader:

                  requirement_cam.append(int(row['Camara_trasera']))
                  requirement_cam.append(int(row['Camara_frontal']))
                  requirement_color.append(str(row['Color']))
                  requirement_ram.append(float(row['RAM']))
                  requirement_storage.append(int(row['Almacenamiento']))
                  requirement_so.append(row['Software'])
                  requirement_battery.append(int(row['Bateria']))

      requirement_cam = sorted(list(set(requirement_cam))) 
      requirement_color = sorted(list(set(requirement_color)))
      requirement_ram = sorted(list(set(requirement_ram)))
      requirement_storage = sorted(list(set(requirement_storage)))
      requirement_so = sorted(list(set(requirement_so)))
      battery = sum(requirement_battery) // len(requirement_battery)
      requirement_battery = [battery]
                 