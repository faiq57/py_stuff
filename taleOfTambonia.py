# Written by Faiq Izhal
# - My earliest code that I've found and stored on Pastebin (May 22nd 2021). I had just graduated from high school!
# - A text adventure game!

# Defining functions
def yes_no():
  global prompt
  prompt = ''
  while prompt != 'Y' and prompt != 'y' and prompt != 'N' and prompt != 'n':
    prompt = input()

# Number generator
random_num = 0
while random_num == 0:
  random_num = input('For procedural number generation, type in a seed. ')
  ran_len = len(random_num)
  rn = 0
  for i in range(ran_len):
    rn = rn + ord(random_num[i])
  rn = (rn * rn) % (1087 * 1091) / (1087 * 1091) * (10 ** 10)
  random_num = round(rn)
  if random_num == 0:
    print('You need to type in something.\n')

# Tale of Tambonia
print('What is your name?')
name = input()
home = input('What country are you from? ')
print('You have arrived at the great city of Tambonia. Here, great adventure awaits! In front of you is a button. Will you press it? (Y/N)')
yes_no()
if  prompt == 'y' or prompt == 'Y':
  print('The world as we know it will never be the same ever again. The button press had triggered every nuclear warhead at every great nation. As such, the small nation of Tambonia had met its demise. In other words, you are dead! You better thank god that you are dead. At least you would not have to see the consequences of your action. \n GAME OVER')
  # Game should end
else:
  print('Crisis averted. The people of Tambonia thanks you. They invite you to a welcoming party. Do you accept? (Y/N)')
  yes_no()
  if prompt == 'y' or prompt =='Y':
    chance_party = random_num % 3
    if chance_party == 0:
      print('You had too much to drink at the party and now you are lost in the middle of the forest with nowhere to go. At least you will live until your supply of Jarate is exhauted. Grandpa from ' + home + ' will be proud.' + '\nGAME OVER')
      # Game should end
    elif chance_party == 1:
      print('The locals were very welcoming at the party. Almost too welcoming. They had you stripped and sit in a cauldron of hot water. You had naively thought that maybe the people of Tambonia greet foreigners with a hot bath. But make no mistake, these cannibals are looking to fill their stomach with exotic ' + name + ' meat. Fresh from ' + home + '. \n GAME OVER')
      # Game should end
    elif chance_party == 2:
      print('The party was a blast! You met a new friend at the party, Toron. Toron invited you to come to his house tomorrow because he have something cool to show you.')
      print('Do you go to Toron\'s home? (Y/N)')
      yes_no()
      if prompt == 'y' or prompt == 'Y':
        print('You could not believe your eyes. Toron\'s house is actually carved into a literal mountain. He showed you the basement, where he found a portal, presumeably into another dimension. Do you go in the portal? (Y/N)')
        yes_no()
        if prompt == 'y' or prompt == 'Y':
          print('You decided to take the leap of faith into the portal and was never seen again. What happened to ' + name + ' you ask? Let\'s leave that up to imagination. \n THE END')
          # Game should end
        else:
          print('You spent the rest of the day hanging out with your pal, Toron. Later, you return to your hotel room and you stayed there until the your flight back to ' + home + '. \n THE END')
          # Game should end
      else:
        print('You took Toron\'s contact information and that was it. The next day, without nothing to do, you lounged around in your hotel room while waiting for the day of your flight home. \n THE END')
        # Game should end
  else:
    chance_rest = random_num % 2
    if chance_rest == 0:
      print('The locals took offense at your adamant refusal to accept their invitation. So they had you tied up and threw you into the ocean. Oh and by the way, they also declared war to ' + home + '. So yeah... \n GAME OVER')
      # Game should end
    if chance_rest == 1:
      print('The locals respect your choice to not attend their party. Without nothing to do, you lounged around in your hotel room while waiting for the day of your flight home. \n THE END')
      # Game should end
