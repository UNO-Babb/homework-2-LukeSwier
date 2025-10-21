#BusSchedule.py
#Name:
#Date:
#Assignment:

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
now = datetime.now() 
formatted_time = now.strftime("%#I:%M%p")
print("Current Time: " + formatted_time)

def isfuturetime(data):
  if ":" not in data:
    return False 
  if converttomiltaryminutes(formatted_time) > converttomiltaryminutes(data):
    return False
  else:
    return True

def firsttwotimes(data):
  nextbus = None 
  followingbus = None
  for d in data:
    if nextbus is None:
      nextbus = d
      nextbus
    elif followingbus is None:
      followingbus = d
      followingbus
      break
  return nextbus,followingbus
  

  
def loadURL(url):
  """
  This function loads a given URL and returns the text
  that is displayed on the site. It does not return the
  raw HTML code but only the code that is visible on the page.
  """
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument("--headless");
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(url)
  content=driver.find_element(By.XPATH, "/html/body").text
  driver.quit()

  return content

def loadTestPage():
  """
  This function returns the contents of our test page.
  This is done to avoid unnecessary calls to the site
  for our testing.
  """
  page = open("testPage.txt", 'r')
  contents = page.read()
  page.close()

  return contents

def converttomiltaryminutes(originaltime):
  hours,minutesandAMorPM = originaltime.split(":")
  minutes = minutesandAMorPM[:-2]
  AMorPM = minutesandAMorPM[-2:]
  hour = int(hours)
  minute = int(minutes)

  if AMorPM == "PM" and hour != 12:
    hour = hour + 12
  elif AMorPM == "AM" and hour == 12:
    hour = 0
  totalminutes = hour * 60 + minute
  return totalminutes




def main():
  direction = "NORTH"
  stop = "1264"
  route = "24"
  url = "https://myride.ometro.com/Schedule?stopCode=" + stop + "&routeNumber=" + route + "&directionName=" + direction
  c1 = loadURL(url) #loads the web page
  words = c1.split()
  bustimes = []
  #c1 = loadTestPage() #loads the test page
  #print(c1)

  nextbus,followingbus = firsttwotimes(bustimes)
  minutestillnext = converttomiltaryminutes(nextbus) - converttomiltaryminutes(formatted_time)
  minutestillfollowing = converttomiltaryminutes(followingbus) - converttomiltaryminutes(formatted_time)
  print("It is " + minutestillnext + " minutes until the next bus")
  print("It is " + minutestillfollowing + " minutes until following bus")
  

main()