import requests, time

total = 10000
cookie = str(input("Enter your cookie: "))

with requests.Session() as session:

  session.cookies['.ROBLOSECURITY'] = cookie
  userId = session.get('https://www.roblox.com/mobileapi/userinfo').json()['UserID']

  def main():
      global total
      cursor = ''
      while cursor != None:
          response = session.get(f'https://economy.roblox.com/v2/users/{userId}/transactions?transactionType=Purchase&limit=100&cursor={cursor}').json()
          if 'data' in response:
              print(f'Found another {len(response["data"])} purchases')
              for purchase in response['data']:
                  if purchase['currency']['type'] == 'Robux':
                      total += purchase['currency']['amount']
              cursor = response['nextPageCursor']
          else:
              time.sleep(30)

  main()

  total = str(total).replace('-', '')
  print(f'\nYou have {total} robux spent in total')
