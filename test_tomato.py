import Image
import glob


file_names = glob.glob("type1/*.jpg")

print len(file_names)

for x in file_names:
	image_file = Image.open(x)

	# image_file = image_file.resize((160, 120), Image.ANTIALIAS)
	image_file = image_file.thumbnail((40,40), Image.ANTIALIAS)
	image_file_flipped.save(x, optimize=True, quality=95)
	# new_file_name = x.replace("type2", "resType2")
	# image_file.save(new_file_name, optimize=True, quality=95)
	image_file_flipped = image_file.transpose(Image.FLIP_LEFT_RIGHT)
	new_file_name = x.replace(".jpg", "_flipped.jpg")
	image_file_flipped.save(new_file_name, optimize=True, quality=95)


	image_file_updown = image_file.transpose(Image.FLIP_UP_DOWN)
	new_file_name = x.replace(".jpg", "_updown.jpg")
	image_file_updown.save(new_file_name, optimize=True, quality=95)

	image_file_updown_flipped = image_file_flipped.transpose(Image.FLIP_UP_DOWN)
	new_file_name = x.replace(".jpg", "_flipped_updown.jpg")
	image_file_updown_flipped.save(new_file_name, optimize=True, quality=95)
