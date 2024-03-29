import json
import collections

objec = collections.OrderedDict()

objec['clean'] = ['한기재','헬스경향','동아닷컴','디지털뉴스팀', '\u3000', 'Copyrights', 'xa0',
                    '기사제공', '문화일보', 'googletagdisplay', 'windowjQuery', 'documentwrite', '\xa0\xa0\xa0\xa0',
                    '세계일보', 'jeong', 'GoodNewsPaper', 'GoodNewspaper', 'Park', 'park', 'chu'
                  ]

objec['stopword'] = ['에서', '으로', '했다', '하는', '이다', '있다', '하고', '있는', '까지', '이라고', '에는',
                        '한다', '지난', '관련', '대한', '됐다', '부터', '된다', '위해', '이번', '통해', '대해',
                        '애게', '했다고', '보다', '되는', '에서는', '있다고', '한다고', '하기', '에도', '때문',
                        '하며', '하지', '해야', '이어', '하면', '따라', '하면서', '라며', '라고', '되고', '단지',
                        '이라는', '이나', '한다는', '있따는', '했고', '이를', '있도록', '있어', '하게', '있다며',
                        '하기로', '에서도', '오는', '라는', '이런', '하겠다고', '만큼', '이는', '덧붙였다', '있을',
                        '이고', '이었다', '이라', '있으며', '있고', '이며', '했다며', '됐다고', '나타났다', '한다며',
                        '하도록', '있지만', '된다고', '되면서', '그러면서', '그동안', '해서는', '에게', '밝혔다', '한편',
                        '최근', '있다는', '보이', '되지', '정도', '지난해', '매년', '오늘', '되며', '하기도', '지난달',
                        '하겠다는', '했다세라', '올해', '바로', '바랍니다', '함께', '이후', '따르면', '같은', '오후',
                        '모두', '로부터', '전날', '면서', '했다는', '그리고', '있던', '다고', '습니다', '다는', '지만',
                        '입니다', '는데', '다며', '따르',

                        '것', '시키', '만들', '그', '지금', '되', '수', '그러', '이', '속', '보', '하나',
                        '않', '집', '없', '살', '모르', '사람', '적', '주', '월', '아니', '데', '등', '자신',
                        '같', '안', '우리', '어떤', '때', '내', '년', '가', '경우', '한', '명', '지', '생각', '대하',
                        '시간', '오', '그녀', '말', '다시', '그렇', '앞', '위하', '번',
                        '그것', '나', '두', '다른', '말하', '어떻', '알', '여자', '그러나', '개', '받', '전', '못하',
                        '들', '일', '사실', '그런', '이렇', '또', '점', '문제', '싶', '더', '사회', '많',
                        '좀', '원', '좋',	'잘', '크', '통하',	'소리',	'중', '놓'
                     
                        'ub', '어요', '..', '어서', '해서', 'ubub', 'xa', '아서', 'ubxa', 'ububub', 'ubububub'
                        'ububububub', 'ubububububububub',
                     
                        '하다', '좋다', '같다', '되다', '들다', '싶다', '나다', '않다'
                     ]


json.dump(objec, open('./stopword_list.json', 'w', encoding='utf-8'), ensure_ascii=False, indent='\t')

with open('./stopword_list.json', 'r', encoding='UTF-8') as f:
    load_file = json.load(f)
    stopword_ls = load_file['stopword']


# 중복 단어 검사
counter = collections.Counter(stopword_ls)
for i, j in zip(counter.values(), counter.keys()):
    if i >= 2:
        print(i, j)

