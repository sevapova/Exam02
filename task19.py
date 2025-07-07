'''19. Eng uzun ismni topish (max + list[str])
🧠 Vazifa: Ismlar ro‘yxatidan eng uzun ismni toping. Oddiy list[str] ishlating.

➡️ Kirish:

names = ['Ali', 'Diyor', 'Jasurbek', 'Muhammad']
⬅️ Chiqish:

Muhammad
'''

names = ['Ali', 'Diyor', 'Jasurbek', 'Muhammad']

longest_name = max(names, key=len)
print(longest_name)

