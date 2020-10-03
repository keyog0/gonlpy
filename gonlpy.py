from konlpy.tag import Mecab
from konlpy.tag import Okt
import time
from tqdm import tqdm
from collections import Counter
import json

okt = Okt()
mecab = Mecab()
#추가메뉴가 있을 경우 dictionary에 피자이름 추가
dictionary = [
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
dictionary_etc = [
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
dictionary_side = [
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
dictionary_drink = [
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
set_combo = [' 세트',' 콤보',' 사이드',' 음료']
keyword_map = json.load(open('keyword.json'))
print(keyword_map)

def converter(text) :
	convert = mecab.nouns(text)
	tmp = []
	set_toggle = False
	combo_toggle = False
	for noun in convert :
		if noun in keyword_map :
			if keyword_map[noun] == 100 :
				set_toggle = True
			elif keyword_map[noun] == 200 :
				combo_toggle = True
			else :
				tmp.append(keyword_map[noun])
	most = Counter(tmp).most_common(1)
	if set_toggle :
		return dictionary[most[0][0]]+set_combo[0]
	elif combo_toggle :
		return dictionary[most[0][0]]+set_combo[1]
	else :
		return dictionary[most[0][0]]

def converter_side(text) :
	convert = mecab.nouns(text)
	tmp = []
	set_toggle = False
	combo_toggle = False
	for noun in convert :
		if noun in keyword_map :
			if keyword_map[noun] == 100 :
				set_toggle = True
			elif keyword_map[noun] == 200 :
				combo_toggle = True
			else :
				tmp.append(keyword_map[noun])
	most = Counter(tmp).most_common(1)
	if set_toggle :
		return dictionary[most[0][0]]+set_combo[0]
	elif combo_toggle :
		return dictionary[most[0][0]]+set_combo[1]
	else :
		return dictionary[most[0][0]]

def converter_fast(text) :
	convert = mecab.nouns(text)
	for noun in convert :
		if noun in keyword_map :
			return dictionary[keyword_map[noun]]

def okt_converter(text) :
	tmp = []
	set_toggle = False
	combo_toggle = False
	for noun in convert :
		if noun in keyword_map :
			if keyword_map[noun] == 100 :
				set_toggle = True
			elif keyword_map[noun] == 200 :
				combo_toggle = True
			else :
				tmp.append(keyword_map[noun])
	most = Counter(tmp).most_common(1)
	if set_toggle :
		return dictionary[most[0][0]]+set_combo[0]
	elif combo_toggle :
		return dictionary[most[0][0]]+set_combo[1]
	else :
		return dictionary[most[0][0]]

def okt_converter_fast(text) :
	convert = mecab.nouns(text)
	for noun in convert :
		if noun in keyword_map :
			return dictionary[keyword_map[noun]]

if __name__ == '__main__' :
    m = '# 노란 체다치즈와 고소한 스모크햄이 만나 샌드위치처럼 든든하고 부담없는 한 끼 식사!!'
    o = '# 노란 체다치즈와 고소한 스모크햄이 만나 샌드위치처럼 든든하고 부담없는 한 끼 식사!!'
    se = '!@#!@$!@클래식 치즈 피자 세트 맛ㅇ있어요 정말로 !@%!@'
    fe = '!@#!@$!@파인애플이 들어간 하와이안 돌체 화덕 피자!@%!@'
    com = '!@!!!@!@!@슈퍼콤비네이션!@#!@#슈퍼 콤비네이션 피자 !@#'
    print(mecab.nouns('청포도 에이드'))
    print(mecab.nouns('마운틴듀 355ml '))
    print(mecab.nouns('미린다 오렌지_option'))
    print(mecab.nouns('자몽에이드_option'))
    print(mecab.nouns('라임에이드_option'))
    print(mecab.nouns('블루베리에이드_option'))
    print(mecab.nouns('콜드브루 아이스커피_option'))
    print(mecab.nouns('맛있는 콘치즈'))
    print(mecab.nouns('프렌치프라이 사이드'))
    print(mecab.nouns('순살3조각'))
    print(mecab.nouns('치즈스틱 치즈 스틱'))
    print(mecab.nouns('콘샐러드 콘 샐러드 '))
    print(mecab.nouns('칠리치즈 칠리 치즈 프라이즈 프라이'))
    print(mecab.nouns('촠촠 브라우니'))
    print(mecab.nouns('새콤달콤하고 프레쉬한 토마토의 맛 혼자서 부담없이 즐기는 클래식한 파스타'))

    print(converter(m))
    print(converter(o))
    print(converter(se))
    print(converter(fe))
    print(converter(com))
    print(converter(m))
    print(converter(o))
    print(converter(se))
    print(converter(fe))
    print(converter(com))
    start = time.time()
    # for i in tqdm(range(100000)) :
    #     mecab.pos(u'# 노란 체다치즈와 고소한 스모크햄이 만나 샌드위치처럼 든든하고 부담없는 한 끼 식사!!')
    # finish = time.time()-start
    # print('mecab finished {} sec'.format(finish))
    # start = time.time()
    # for i in tqdm(range(100000)) :
    #     okt.pos(u'# 노란 체다치즈와 고소한 스모크햄이 만나 샌드위치처럼 든든하고 부담없는 한 끼 식사!!')
    # finish = time.time()-start
    # print('okt finished {} sec'.format(finish))

    # for i in tqdm(range(100000)) :
    #     converter_fast(m)
    # finish = time.time()-start
    # print('converter_fast finished {} sec'.format(finish))
    # start = time.time()
    # for i in tqdm(range(100000)) :
    #     converter(m)
    # finish = time.time()-start
    # print('converter finished {} sec'.format(finish))