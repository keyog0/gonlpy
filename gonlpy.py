# -*- coding: utf-8 -*-
from konlpy.tag import Mecab
from konlpy.tag import Okt
import time
from tqdm import tqdm
from collections import Counter
import json

okt = Okt()
mecab = Mecab()
#추가메뉴가 있을 경우 dictionary에 피자이름 추가
class NameConverter :
	def __init__(self) :
		self.dictionary_pizza = [
						'클래식 치즈 피자',
						'햄앤체다 피자',
						'페퍼로니 피자',
						'하와이안 피자',
						'고르곤졸라 피자',
						'베이컨 포테이토 피자',
						'불고기 피자',
						'고구마 피자',
						'페퍼로니 매니아 피자',
						'슈퍼 콤비네이션 피자',
						'아시안 시푸드 피자',
						'부라타 치즈 피자'
						]
		self.dictionary_etc = [
						'토마토 파스타',
						'알리오올리오 파스타',
						'까르보나라 파스타',
						'치즈 오븐 파스타',
						'불닭 치즈 파스타',
						'갈릭디핑소스 기타',
						'핫소스 기타',
						'렌치소스 기타',
						'파이어소스 기타',
						'오이피클 기타',
						'고구마무스 추가(토핑)',
						'치즈 추가(토핑)',
						'고고 패키지'
						]
		self.dictionary_side = [
						'콘치즈',
						'프렌치 프라이',
						'순살치킨앤프라이',
						'치즈스틱',
						'콘샐러드',
						'칠리치즈 프라이',
						'오리지널 버팔로윙',
						'불닭 버팔로윙',
						'데리야끼 버팔로윙',
						'브라우니',
						'애플망고스틱',
						]
		self.dictionary_drink = [
						'콜라',
						'사이다',
						'마운틴듀',
						'미린다 오렌지',
						'오렌지주스',
						'포도 주스',
						'청포도 에이드',
						'자몽 에이드',
						'라임 에이드',
						'블루베리 레몬 에이드',
						'콜드브루'
						]

		self.set_combo = [' 세트',' 콤보']
		self.count_side = [' 2개',' 4개']
		self.Class = ['피자','사이드','음료','기타']
		self.keyword_pizza = json.load(open('keyword/keyword_pizza.json'))
		self.keyword_side = json.load(open('keyword/keyword_side.json'))
		self.keyword_drink = json.load(open('keyword/keyword_drink.json'))
		self.keyword_etc = json.load(open('keyword/keyword_etc.json'))
	
	def convert(self,text) :
		convert = mecab.morphs(text)
		output = text
		class_tmp = []
		set_toggle = False
		combo_toggle = False
		class_name = 'Error'
		for noun in convert :
			if noun in self.keyword_pizza :
				class_tmp.append('피자')
			if noun in self.keyword_side :
				class_tmp.append('사이드')
			if noun in self.keyword_drink :
				class_tmp.append('음료')
			if noun in self.keyword_etc :
				class_tmp.append('기타')

		try :
			class_name = Counter(class_tmp).most_common(1)[0][0]
		except :
			pass
		if class_name == '피자' :
			output = self.converter_pizza(text,self.keyword_pizza,self.dictionary_pizza)
			return output
		elif class_name == '사이드' :
			output = self.converter_side(text,self.keyword_side,self.dictionary_side)
			return output+' '+class_name
		elif class_name == '음료' :
			output = self.converter_drink(text,self.keyword_drink,self.dictionary_drink)
			return output+' '+class_name
		elif class_name == '기타' :
			output = self.converter_etc(text,self.keyword_etc,self.dictionary_etc)
			return output
		else :
			return output

	def converter_pizza(self,text,keyword,dictionary) :
		convert = mecab.morphs(text)
		tmp = []
		set_toggle = False
		combo_toggle = False
		for noun in convert :
			if noun in keyword :
				if keyword[noun] == 100 :
					set_toggle = True
				elif keyword[noun] == 200 :
					combo_toggle = True
				elif keyword[noun] == 500 :
					pass
				else :
					tmp.append(keyword[noun])
		most = Counter(tmp).most_common(1)
		if set_toggle :
			return dictionary[most[0][0]]+self.set_combo[0]
		elif combo_toggle :
			return dictionary[most[0][0]]+self.set_combo[1]
		else :
			return dictionary[most[0][0]]

	def converter_side(self,text,keyword,dictionary) :
		convert = mecab.morphs(text)
		tmp = []
		bufflo_toggle = False
		two_toggle = False
		four_toggle = False
		for noun in convert :
			if noun in keyword :
				if keyword[noun] == 500 :
					bufflo_toggle = True
				if bufflo_toggle :
					if keyword[noun] == 200 :
						four_toggle = True
					else :
						two_toggle = True
				else :
					tmp.append(keyword[noun])
		most = Counter(tmp).most_common(1)
		if two_toggle :
			return dictionary[most[0][0]]+self.count_side[0]
		elif four_toggle :
			return dictionary[most[0][0]]+self.count_side[1]
		else :
			return dictionary[most[0][0]]

	def converter_drink(self,text,keyword,dictionary) :
		convert = mecab.morphs(text)
		tmp = []
		for noun in convert :
			if noun in keyword :
				if keyword[noun] == 3 :
					tmp.append(keyword[noun])
				if keyword[noun] == 500 :
					pass
				else :
					tmp.append(keyword[noun])
		most = Counter(tmp).most_common(1)
		return dictionary[most[0][0]]

	def converter_etc(self,text,keyword,dictionary) :
		convert = mecab.morphs(text)
		tmp = []
		for noun in convert :
			if noun in keyword :
				if keyword[noun] == 500 or keyword[noun] == 600:
					pass
				else :
					tmp.append(keyword[noun])
		most = Counter(tmp).most_common(1)
		return dictionary[most[0][0]]

	def converter_fast(self,text,keyword,dictionary) :
		convert = mecab.nouns(text)
		for noun in convert :
			if noun in keyword :
				return dictionary[keyword[noun]]

	def okt_converter(self,text,keyword,dictionary) :
		tmp = []
		set_toggle = False
		combo_toggle = False
		for noun in convert :
			if noun in keyword :
				if keyword[noun] == 100 :
					set_toggle = True
				elif keyword[noun] == 200 :
					combo_toggle = True
				else :
					tmp.append(keyword[noun])
		most = Counter(tmp).most_common(1)
		if set_toggle :
			return dictionary[most[0][0]]+set_combo[0]
		elif combo_toggle :
			return dictionary[most[0][0]]+set_combo[1]
		else :
			return dictionary[most[0][0]]

	def okt_converter_fast(self,text,keyword,dictionary) :
		convert = mecab.nouns(text)
		for noun in convert :
			if noun in keyword :
				return dictionary[keyword[noun]]

if __name__ == '__main__' :
	converter = NameConverter()

	m = '# 노란 체다치즈와 고소한 스모크햄이 만나 샌드위치처럼 든든하고 부담없는 한 끼 식사!!'
	o = '# 노란 체다치즈와 고소한 스모크햄이 만나 샌드위치처럼 든든하고 부담없는 한 끼 식사!!'
	se = '!@#!@$!@클래식 치즈 피자 세트 맛ㅇ있어요 정말로 !@%!@'
	fe = '!@#!@$!@파인애플이 들어간 하와이안 돌체 화덕 피자!@%!@'
	com = '!@!!!@!@!@슈퍼콤비네이션!@#!@#슈퍼 콤비네이션 피자 !@#'
	print(converter.convert('청포도 에이드'))
	print(converter.convert('마운틴듀 355ml '))
	print(converter.convert('미린다 오렌지_option'))
	print(converter.convert('자몽에이드_option'))
	print(converter.convert('라임에이드_option'))
	print(converter.convert('블루베리에이드_option'))
	print(converter.convert('콜드브루 아이스커피_option'))
	print(converter.convert('맛있는 콘치즈'))
	print(converter.convert('프렌치프라이 사이드'))
	print(converter.convert('순살3조각'))
	print(converter.convert('치즈스틱 치즈 스틱'))
	print(converter.convert('콘샐러드 콘 샐러드 '))
	print(converter.convert('칠리치즈 칠리 치즈 프라이즈 프라이'))
	print(converter.convert('촠촠 브라우니'))
	print(converter.convert('새콤달콤하고 프레쉬한 토마토의 맛 혼자서 부담없이 즐기는 클래식한 파스타'))
	print(converter.convert('알리오올리오 파스타 알리오 올리오 파스타'))
	print(converter.convert('까르보나라 크림파스타 크림 파스타'))
	print(converter.convert('치즈 오븐 파스타'))
	print(converter.convert('불닭 파스타'))
	print(converter.convert('갈릭디핑소스 갈릭소스'))
	print(converter.convert('랜치 소스 랜치소스 렌치소스'))
	print(converter.convert('파이어 소스 파이어소스 볼케이노소스'))
	print(converter.convert('치즈추가 치즈 추가'))
	print(converter.convert('고고 패키지 고고패키지 2인 세트'))
	print(converter.convert('고고 패키지 고고패키지 2인 세트'))

	print(converter.convert('# 피자의 클래식! 신선한 토마토 소스와 고소한 치즈의 오리지널 피자'))
	print(converter.convert(o))
	print(converter.convert(se))
	print(converter.convert(fe))
	print(converter.convert(com))
	print(converter.convert(m))
	print(converter.convert(o))
	print(converter.convert(se))
	print(converter.convert(fe))
	print(converter.convert(com))
	start = time.time()
	# for i in tqdm(range(100000)) :
	#	 mecab.pos(u'# 노란 체다치즈와 고소한 스모크햄이 만나 샌드위치처럼 든든하고 부담없는 한 끼 식사!!')
	# finish = time.time()-start
	# print('mecab finished {} sec'.format(finish))
	# start = time.time()
	# for i in tqdm(range(100000)) :
	#	 okt.pos(u'# 노란 체다치즈와 고소한 스모크햄이 만나 샌드위치처럼 든든하고 부담없는 한 끼 식사!!')
	# finish = time.time()-start
	# print('okt finished {} sec'.format(finish))

	# for i in tqdm(range(100000)) :
	#	 converter_fast(m)
	# finish = time.time()-start
	# print('converter_fast finished {} sec'.format(finish))
	# start = time.time()
	# for i in tqdm(range(100000)) :
	#	 converter(m)
	# finish = time.time()-start
	# print('converter finished {} sec'.format(finish))

	for i in tqdm(range(2500)) :
		converter.convert('청포도 에이드')
		converter.convert('마운틴듀 355ml ')
		converter.convert('미린다 오렌지_option')
		converter.convert('자몽에이드_option')
		converter.convert('라임에이드_option')
		converter.convert('블루베리에이드_option')
		converter.convert('콜드브루 아이스커피_option')
		converter.convert('맛있는 콘치즈')
		converter.convert('프렌치프라이 사이드')
		converter.convert('순살3조각')
		converter.convert('치즈스틱 치즈 스틱')
		converter.convert('콘샐러드 콘 샐러드 ')
		converter.convert('칠리치즈 칠리 치즈 프라이즈 프라이')
		converter.convert('촠촠 브라우니')
		converter.convert('새콤달콤하고 프레쉬한 토마토의 맛 혼자서 부담없이 즐기는 클래식한 파스타')
		converter.convert('알리오올리오 파스타 알리오 올리오 파스타')
		converter.convert('까르보나라 크림파스타 크림 파스타')
		converter.convert('치즈 오븐 파스타')
		converter.convert('불닭 파스타')
		converter.convert('갈릭디핑소스 갈릭소스')
		converter.convert('랜치 소스 랜치소스 렌치소스')
		converter.convert('파이어 소스 파이어소스 볼케이노소스')
		converter.convert('치즈추가 치즈 추가')
		converter.convert('고고 패키지 고고패키지 2인 세트')
		converter.convert('고고 패키지 고고패키지 2인 세트')
		converter.convert('# 피자의 클래식! 신선한 토마토 소스와 고소한 치즈의 오리지널 피자')
		converter.convert(o)
		converter.convert(se)
		converter.convert(fe)
		converter.convert(com)
		converter.convert(m)
		converter.convert(o)
		converter.convert(se)
		converter.convert(fe)
		converter.convert(com)
		converter.convert(com)
		converter.convert(m)
		converter.convert(o)
		converter.convert(se)
		converter.convert(fe)
		converter.convert(com)

	finish = time.time() - start
	print('converter finished {} sec'.format(finish))