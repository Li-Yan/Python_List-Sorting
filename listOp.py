def Refine(s):
	s1 = ''
	s2 = ''

	#In case of '-9%^3' or '---apple' or '%#$#$#@------98', s1 remain all '-' while s2 does not
	for ch in s:
		if ch >= 'a' and ch <= 'z' or ch >= 'A' and ch <= 'Z' or ch >= '0' and ch <= '9' or ch == '-':
			s1 = s1 + ch
			if ch != '-':
				s2 = s2 + ch
	
	#Check whether s2 is a number, if yes, return as a number; if not, eliminate all '-'
	if IsNumber(s2):
		if s1[0] == '-':
			return '-' + s2
		else:
			return s2
	else:
		return s2

def IsNumber(s):
	if (s[0] == '-'):
		str = s[1 : len(s) - 1]
	else:
		str = s

	for ch in str:
		if ch < '0' or ch >'9':
			return False
	return True

def Separate(ss, w_or_n, word, number):
	for i in range(0, len(ss)):
		s = Refine(ss[i])
		if IsNumber(s):
			w_or_n.append('n')
			number.append(int(s))
		else:
			w_or_n.append('w')
			word.append(s)

def Rearrange(w_or_n, word, number):
	ss = list();
	word_index = 0
	number_index = 0

	for ch in w_or_n:
		if ch == 'w':
			ss.append(word[word_index])
			word_index = word_index + 1
		else:
			ss.append(number[number_index])
			number_index = number_index + 1
	
	return ss
