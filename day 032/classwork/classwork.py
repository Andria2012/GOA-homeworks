names = ["გიო", "ანა", "საბა"]
sentence = ", ".join(names)
print(sentence)



animals = []
animals.append("კუ")
print(animals)



print("პირველი:", animals[0])
print("ბოლო:", animals[-1])



word = "მეგობრები"
print("ასოების რაოდენობა:", len(word))



my_list = ["მე", "მიყვარს", "გოა"]
print("ელემენტების რაოდენობა:", len(my_list))



songs = ["song1", "song2", "song3"]
songs.insert(2, "pantera")
print(songs)



joined_songs = "|".join(songs)
print(joined_songs)




text = "python"
print(text.upper())
print(text.lower())
print(text.capitalize())