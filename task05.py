'''5. So‘zlar sonini hisoblash
🧠 Vazifa: Matn ichidagi har bir so‘z necha marta qatnashganini aniqlang. Natijani dict tarzida qaytaring.

➡️ Kirish: "salom salom dunyo" ⬅️ Chiqish: {'salom': 2, 'dunyo': 1}
'''
def count_words(text):
    words = text.strip().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def run_word_counter():
    text = input("Matnni kiriting: ")
    result = count_words(text)
    print("So'zlar soni:", result)

run_word_counter()