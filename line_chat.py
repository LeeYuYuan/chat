def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines



def count(lines):
	allen_word_count = 0
	allen_stricker_count = 0
	allen_pic_count = 0
	viki_word_count = 0
	viki_stricker_count = 0
	viki_pic_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_stricker_count = allen_stricker_count + 1
			elif s[2] == '圖片':
				allen_pic_count = allen_pic_count + 1
			else:
				for m in s[2:]:
					allen_word_count = allen_word_count + len(m)
		if name == 'Viki':
			if s[2] == '貼圖':
				viki_stricker_count = viki_stricker_count + 1
			elif s[2] == '圖片':
				viki_pic_count = viki_pic_count + 1
			else:
				for m in s[2:]:
					viki_word_count = viki_word_count + len(m)
	print('Allen說了', allen_word_count, '個字')
	print('Allen傳了', allen_stricker_count, '個貼圖')
	print('Allen傳了', allen_pic_count, '個圖片')
	print('Viki說了', viki_word_count, '個字')
	print('Viki傳了', viki_stricker_count, '個貼圖')
	print('Viki傳了', viki_pic_count, '個圖片')


def write_new(new_file, lines):
		with open(new_file, 'w') as f:
			for result in lines:
				f.write(result + '\n')


def main():
	lines = read_file('-LINE-Viki.txt')
	count(lines)
	#write_new('output.txt', lines)

main()
