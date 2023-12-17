from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pwinput
import sys
import os
import ctypes
import datetime
from datetime import time as dtime
from colorama import Fore

THIS_VERSION = "2.8.1"
y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTCYAN_EX
w = Fore.LIGHTWHITE_EX


def main():
    clear()
    setTitle(f"cptcCOPILOT Menu v{THIS_VERSION}")
    hometitle()
    print(f"""      {y}[{b}-{y}]{w} Main Options:           
    \n          {y}[{w}01{y}]{w} Auto Book              
    \n          {y}[{w}02{y}]{w} User Booking Switch            
    \n          {y}[{w}03{y}]{w} Court Stealer :o             
    \n          {y}[{w}04{y}]{w} SOON™️                                      
    \n          {y}[{w}05{y}]{w} SOON™️                                 
    \n                                                                     
    \t\t\t\t\t\t\t\t\t\t\t\t\t""")
    global choice
    choice = input(f"""{y}[{b}#{y}]{w} Choice: """).lstrip("0")
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    if choice == '1':
        transition()
        hometitle()
        credits()
        autobook()
        input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} I massacred this tool while trying to fix something, (it dont work).")
        main()
    elif choice == '2':
        transition()
        hometitle()
        credits()
        quickswitch()
        input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} I massacred this tool while trying to fix something, (it dont work).")
        main()
    elif choice == '3':
        transition()
        hometitle()
        credits()
        courtstealer()
        input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} I massacred this tool while trying to fix something, (it dont work).")
        main()
    elif choice == '4':
        transition()
        input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} This tool is under development, so it is not yet usable.")
        main()
    elif choice == '5':
        transition()
        input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} This tool is under development, so it is not yet usable.")

def courtstealer():
    # input date and time, output courts available
    # every 2 minutes refresh
    # check the color tag of each court

    booker = input("enter username of person trying to book ")
    pwd = pwinput.pwinput("enter password for booker", mask='*')
    date = input("enter date of booking e.g. 'Tuesday 31': ")
    courttime = input("what time would you like e.g. '6:00 am'? ")

    if "Saturday" in date or "Sunday" in date:
        weekend = True
    else:
        weekend = False

    weekendtimetocourtidx = {
        "7:00 am":1,
        "8:30 am":2,
        "10:00 am":3,
        "11:30 am":4,
        "1:00 pm":5,
        "2:30 pm":6,
        "4:00 pm":7,
        "5:30 pm":8,
        "7:00 pm":9,
        "8:30 pm":10
    }

    weektimetocourtidx = {
        "6:00 am":1,
        "7:00 am":2,
        "8:30 am":3,
        "10:00 am":4,
        "11:30 am":5,
        "1:00 pm":6,
        "2:30 pm":7,
        "4:00 pm":8,
        "5:30 pm":9,
        "7:00 pm":10,
        "8:30 pm":11
    }


    availablecourts = []

    driver.get("https://cptc.gametime.net/auth")

    try:
        driver.find_element(By.NAME, "username").send_keys(booker)
        driver.find_element(By.NAME, "password").send_keys(pwd)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/form/fieldset/ul/li[4]/button").click()
    except Exception as e:
        print(e)

    time.sleep(2)

    try:
        driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[3]/div/div/ul/li[3]/a").click()
    except Exception as e:
        print(e)

    time.sleep(2)

    try:
        for i in range(2, 9):
            day = "/html/body/div[3]/div[3]/div[4]/div[2]/div[1]/div[1]/div[2]/ul/li["
            day += str(i)
            day += ']/a/span'
            finalday = driver.find_element(By.XPATH, day).text
            if finalday == date:
                driver.find_element(By.XPATH, day).click()
    except Exception as e:
        print(e)

    time.sleep(2)

    try:
        driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[2]/div[1]/div[2]/span[1]").click()
        time.sleep(2)
        courtstart = "/html/body/div[3]/div[3]/div[4]/div[2]/div[1]/div[4]/table/tbody/tr/td["
        for i in range(1, 5):
            courtstart += str(i)
            courtstart += "]/div["
            if weekend:
                courtstart += str(weekendtimetocourtidx[courttime])
            if not weekend:
                courtstart += str(weektimetocourtidx[courttime])
            courtstart += "]"
            bgcolorelement = driver.find_element(By.XPATH, courtstart)
            style_attribute = bgcolorelement.get_attribute('style')
            try:
                if 'background-color' not in style_attribute and 'height: 155px' in style_attribute:
                    availablecourts.append(i)
                    courtstart = courtstart[:-9]
                else:
                    courtstart = courtstart[:-9]
            except:
                print("exception at " + courtstart)
                courtstart = courtstart[:-9]
                pass

        time.sleep(2)

        driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[2]/div[1]/div[2]/span[2]/a").click()
        time.sleep(2)
        for i in range(1, 5):
            courtstart += str(i)
            courtstart += "]/div["
            if weekend:
                courtstart += str(weekendtimetocourtidx[courttime])
            if not weekend:
                courtstart += str(weektimetocourtidx[courttime])
            courtstart += "]"
            bgcolorelement = driver.find_element(By.XPATH, courtstart)
            style_attribute = bgcolorelement.get_attribute('style')
            print("courtstart = " + courtstart)
            try:
                if 'background-color' not in style_attribute and 'height: 155px' in style_attribute:
                    availablecourts.append(i+4)
                    courtstart = courtstart[:-9]
                else:
                    courtstart = courtstart[:-9]
            except:
                courtstart = courtstart[:-9]
                pass

        time.sleep(2)

        driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[2]/div[1]/div[2]/span[3]/a").click()
        time.sleep(2)
        for i in range(1, 5):
            courtstart += str(i)
            courtstart += "]/div["
            if weekend:
                courtstart += str(weekendtimetocourtidx[courttime])
            if not weekend:
                courtstart += str(weektimetocourtidx[courttime])
            courtstart += "]"
            bgcolorelement = driver.find_element(By.XPATH, courtstart)
            style_attribute = bgcolorelement.get_attribute('style')
            try:
                if 'background-color' not in style_attribute and 'height: 155px' in style_attribute:
                    availablecourts.append(i+8)
                    courtstart = courtstart[:-9]
                else:
                    courtstart = courtstart[:-9]
            except:
                courtstart = courtstart[:-9]
                pass

    except Exception as e:
        print(e)

    time.sleep(2)

    print("available courts: ")
    print(availablecourts)




def quickswitch():
    cancelingaccount = input("enter username of account with booking: ")
    bookingaccount = input("enter username of account trying to obtain court: ")
    pwd = pwinput.pwinput("enter password for 1st booker: ", mask='*')
    pwd2 = pwinput.pwinput("enter password for 2nd booker (type ' for same password): ", mask='*')
    date = input("enter date of booking e.g. 'Friday 17': ")
    courttime = input("enter time of booking e.g. '5:30 pm': ")
    court = int(input("enter court: "))
    walkonreserved = input("walk on or reserved: ")
    correctButton = None

    cancelbutton = "/html/body/div[3]/div[3]/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/ul/li/span[4]/a"
    bookingdatestr = "/html/body/div[3]/div[3]/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/ul/li/span[2]"

    driver.get("https://cptc.gametime.net/auth")

    try:
        driver.find_element(By.NAME, "username").send_keys(cancelingaccount)
        driver.find_element(By.NAME, "password").send_keys(pwd)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/form/fieldset/ul/li[4]/button").click()
    except Exception as e:
        print(e)

    time.sleep(5)

    bookingdate = driver.find_element(By.XPATH, bookingdatestr).text

    dates = date.split()
    for datecheck in dates:
        if datecheck in bookingdate:
            correctButton = True

    time.sleep(0.5)

    try:
        if correctButton:
            driver.find_element(By.XPATH, cancelbutton).click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[2]/form/button[2]/span").click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div[5]/div[2]/form/div[2]/div[1]/div[3]/span/span[1]/span/button").click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[1]/ul/li[3]/a").click()
        else:
            print("bruh")
    except Exception as e:
        print(e)

    time.sleep(2)

    try:
        driver.find_element(By.NAME, "username").send_keys(bookingaccount)
        if pwd2 == "'":
            driver.find_element(By.NAME, "password").send_keys(pwd)
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/form/fieldset/ul/li[4]/button").click()
        else:
            driver.find_element(By.NAME, "password").send_keys(pwd2)
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/form/fieldset/ul/li[4]/button").click()
    except Exception as e:
        print(e)

    time.sleep(2)

    try:
        driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[3]/div/div/ul/li[3]/a").click()
    except Exception as e:
        print(e)

    time.sleep(2)

    try:
        for i in range(2, 9):
            day = "/html/body/div[3]/div[3]/div[4]/div[2]/div[1]/div[1]/div[2]/ul/li["
            day += str(i)
            day += ']/a/span'
            finalday = driver.find_element(By.XPATH, day).text
            if finalday == date:
                driver.find_element(By.XPATH, day).click()
    except Exception as e:
        print(e)

    time.sleep(2)

    try:
        if 1 <= court <= 4:
            driver.find_element(By.XPATH,
                                "/html/body/div[3]/div[3]/div[4]/div[2]/div[1]/div[2]/span[1]").click()
            courtgroup = 1
        elif 5 <= court <= 8:
            driver.find_element(By.XPATH,
                                "/html/body/div[3]/div[3]/div[4]/div[2]/div[1]/div[2]/span[2]/a").click()
            courtgroup = 5
        elif 9 <= court <= 12:
            driver.find_element(By.XPATH,
                                "/html/body/div[3]/div[3]/div[4]/div[2]/div[1]/div[2]/span[3]/a").click()
            courtgroup = 9
        else:
            driver.find_element(By.XPATH,
                                "/html/body/div[3]/div[3]/div[4]/div[2]/div[1]/div[2]/span[4]/a").click()
            courtgroup = 13
    except Exception as e:
        print(e)

    time.sleep(2)

    try:
        courtindex = court - courtgroup
        courtindex += 1
        courtbegining = "/html/body/div[3]/div[3]/div[4]/div[2]/div[1]/div[4]/table/tbody/tr/td["
        courtbegining += str(courtindex)
        courtbegining += "]"
        for i in range(1, 12):
            try:
                courtbegining += '/div['
                courtbegining += str(i)
                courtbegining += ']/div'
                currentcourttime = driver.find_element(By.XPATH, courtbegining)
                if currentcourttime.text == courttime:
                    currentcourttime.click()
                else:
                    courtbegining = courtbegining[:-11]
            except:
                pass
    except Exception as e:
        print(e)

    time.sleep(2)

    try:
        if walkonreserved == "reserved":
            driver.find_element(By.XPATH,
                                "/html/body/div[3]/div[3]/div[5]/div[2]/form/fieldset[2]/ul/li[1]/ul/li[1]/input").click()
        elif walkonreserved == "walk on":
            driver.find_element(By.XPATH,
                                "/html/body/div[3]/div[3]/div[5]/div[2]/form/fieldset[2]/ul/li[1]/ul/li[2]/input").click()
        else:
            driver.find_element(By.XPATH,
                                "/html/body/div[3]/div[3]/div[5]/div[2]/form/fieldset[2]/ul/li[1]/ul/li[2]/input").click()
    except Exception as e:
        print(e)

    time.sleep(2)

    try:
        driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[2]/form/button/span").click()
    except Exception as e:
        print(e)

    time.sleep(2)

    print("mission done")
    sys.exit()



def autobook():
    date = input("enter date e.g. 'Tuesday 31': ")
    court = int(input("which court would you like? "))
    booker = input("enter username of person trying to book ")
    pwd = pwinput.pwinput("enter password for booker: ", mask='*')
    courttime = input("what time would you like e.g. '6:00 am'? ")
    bookingtime = input("when do you want the court to be booked? e.g. 'HH:MM', '16:54' ")
    walkonreserved = input("walk on or reserved? e.g 'walk on' ")
    courtgroup = 0

    while True:
        current_time = datetime.datetime.now().strftime('%H:%M')
        eight_pm = dtime(20, 0)
        if current_time > eight_pm and walkonreserved == "walk on":
            instantbook = True
        else:
            instantbook = False


        if current_time == bookingtime:
            driver.get("https://cptc.gametime.net/auth")

            try:
                driver.find_element(By.NAME, "username").send_keys(booker)
                driver.find_element(By.NAME, "password").send_keys(pwd)
                driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/form/fieldset/ul/li[4]/button").click()
            except Exception as e:
                print(e)

            time.sleep(2)

            try:
                driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[3]/div/div/ul/li[3]/a").click()
            except Exception as e:
                print(e)

            time.sleep(2)

            try:
                for i in range(2, 9):
                    day = "/html/body/div[3]/div[3]/div[4]/div[2]/div[1]/div[1]/div[2]/ul/li["
                    day += str(i)
                    day += ']/a/span'
                    finalday = driver.find_element(By.XPATH, day).text
                    if finalday == date:
                        driver.find_element(By.XPATH, day).click()
            except Exception as e:
                print(e)

            time.sleep(2)

            try:
                if 1 <= court <= 4:
                    driver.find_element(By.XPATH,
                                        "/html/body/div[3]/div[3]/div[4]/div[2]/div[1]/div[2]/span[1]").click()
                    courtgroup = 1
                elif 5 <= court <= 8:
                    driver.find_element(By.XPATH,
                                        "/html/body/div[3]/div[3]/div[4]/div[2]/div[1]/div[2]/span[2]/a").click()
                    courtgroup = 5
                elif 9 <= court <= 12:
                    driver.find_element(By.XPATH,
                                        "/html/body/div[3]/div[3]/div[4]/div[2]/div[1]/div[2]/span[3]/a").click()
                    courtgroup = 9
                else:
                    driver.find_element(By.XPATH,
                                        "/html/body/div[3]/div[3]/div[4]/div[2]/div[1]/div[2]/span[4]/a").click()
                    courtgroup = 13
            except Exception as e:
                print(e)

            time.sleep(2)

            try:
                courtindex = court - courtgroup
                courtindex += 1
                courtbegining = "/html/body/div[3]/div[3]/div[4]/div[2]/div[1]/div[4]/table/tbody/tr/td["
                courtbegining += str(courtindex)
                courtbegining += "]"
                for i in range(1, 12):
                    try:
                        courtbegining += '/div['
                        courtbegining += str(i)
                        courtbegining += ']/div'
                        currentcourttime = driver.find_element(By.XPATH, courtbegining)
                        if currentcourttime.text == courttime:
                            currentcourttime.click()
                        else:
                            courtbegining = courtbegining[:-11]
                    except:
                        pass
            except Exception as e:
                print(e)

            if not instantbook:
                time.sleep(280)

            try:
                driver.refresh()
            except Exception as e:
                print(e)

            time.sleep(2)

            try:
                if walkonreserved == "reserved":
                    driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[2]/form/fieldset[2]/ul/li[1]/ul/li[1]/input").click()
                elif walkonreserved == "walk on":
                    driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[2]/form/fieldset[2]/ul/li[1]/ul/li[2]/input").click()
                else:
                    driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[2]/form/fieldset[2]/ul/li[1]/ul/li[2]/input").click()

                driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[2]/form/button/span").click()
            except Exception as e:
                print(e)

            time.sleep(2)

            print("mission done")
            sys.exit()



        print(f"Current time: {current_time}. Waiting for target time...")
        time.sleep(5)


def hometitle():
    print(f"""\n\n   
                 ██████╗██████╗ ████████╗ ██████╗     ██████╗ ██████╗ ██████╗ ██╗██╗      ██████╗ ████████╗
                ██╔════╝██╔══██╗╚══██╔══╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██║██║     ██╔═══██╗╚══██╔══╝
                ██║     ██████╔╝   ██║   ██║         ██║     ██║   ██║██████╔╝██║██║     ██║   ██║   ██║   
                ██║     ██╔═══╝    ██║   ██║         ██║     ██║   ██║██╔═══╝ ██║██║     ██║   ██║   ██║   
                ╚██████╗██║        ██║   ╚██████╗    ╚██████╗╚██████╔╝██║     ██║███████╗╚██████╔╝   ██║   
                 ╚═════╝╚═╝        ╚═╝    ╚═════╝     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝ ╚═════╝    ╚═╝   



                                                                                               \n""".replace('█',
                                                                                                             f'{b}█{y}'))


def loader():
    l = ['|', '/', '-', '\\']
    for i in l + l + l:
        sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Cooking... {i}""")
        sys.stdout.flush()
        time.sleep(0.2)


def setTitle(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} - made by aspect")
    elif system == 'posix':
        sys.stdout.write(f"\x1b]0;{_str} - made by aspect\x07")
    else:
        pass


def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n' * 120)
    return


def transition():
    clear()
    loader()
    clear()


def credits():
    print(
        f"""{y}------------------------------------------------------------------------------------------------------------------------\n{w}  ub.com/aspxcts {b}|{w} https://github.com/aspxcts {b}|{w} https://github.com/aspxcts {b}|{w} https://github.com/aspxcts {b}|{w} https://gith\n{y}------------------------------------------------------------------------------------------------------------------------\n""")


string = 'hi'

if __name__ == "__main__":
    main()