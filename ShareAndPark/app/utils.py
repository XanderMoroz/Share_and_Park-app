def custom_popup_render(place, user_auth=False):
    if user_auth==False:
        # Рендер карточки парковки на карте follium для не авторизованного пользователя
        html_no_auth = f"""
                        <!DOCTYPE html>
                        <html>
                        <link rel="stylesheet" type="text/css" href="static/styles/index.css">
                        <link rel="stylesheet" type="text/css" href="static/styles/card.css">
                        <div class='card'>
                        <img class='card__image' src="{place.image.url}" alt="Flowers in Chania" width="230" height="172">
                        <h5 class='card__address' >{place.title}</h5>
                        <h5 class='card__subtitle' >{place.description}</h5>
                        <h4 class='card__title'>{place.pricePerHour} ₽ / час </h4>
                        <button class='card__button' disabled >ТРЕБУЕТСЯ АВТОРИЗАЦИЯ</button>
                        </div>
                        <html>
                        """
        return html_no_auth
    else:
        # Рендер карточки парковки на карте follium для авторизованного пользователя
        html_auth = f"""
                        <!DOCTYPE html>
                        <html>
                        <link rel="stylesheet" type="text/css" href="static/styles/index.css">
                        <link rel="stylesheet" type="text/css" href="static/styles/card.css">
                        <div class='card'>
                        <img class='card__image' src="{place.image.url}" alt="Flowers in Chania" width="230" height="172">
                        <h5 class='card__address' >{place.title}</h5>
                        <h5 class='card__subtitle' >{place.description}</h5>
                        <h4 class='card__title'>{place.pricePerHour} ₽ / час </h4>
                        <a class='card__button' href="/{place.id}">ПОДРОБНЕЕ</a>
                        </div>
                        <html>
                        """
        return html_auth







subway_station = [

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "А"
    ('AVMK', 'Авиамоторная (калин.)'),
    ('AVMN', 'Авиамоторная (некр.)'),
    ('AVTZ', 'Автозаводская'),
    ('AKAD', 'Академическая'),
    ('ALSD', 'Александровский сад'),
    ('ALKS', 'Алексеевская'),
    ('ALAT', 'Алма-Атинская'),
    ('ALTF', 'Алтуфьево'),
    ('ANNO', 'Аннино'),
    ('ARBA', 'Арбатская (арб.-покр.)'),
    ('ARBF', 'Арбатская (фил.)'),
    ('AERP', 'Аэропорт'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "Б"
    ('BABU', 'Бабушкинская'),
    ('BGRT', 'Багратионовская'),
    ('BARR', 'Баррикадная'),
    ('BAUM', 'Бауманская'),
    ('BGVY', 'Беговая'),
    ('BLMR', 'Беломорская'),
    ('BLRZ', 'Белорусская (змск.)'),
    ('BLRK', 'Белорусская (кольц.)'),
    ('BELY', 'Беляево'),
    ('BIBR', 'Бибирево'),
    ('BBIL', 'Библиотека имени Ленина'),
    ('BTCP', 'Битцевский парк'),
    ('BRSV', 'Борисово'),
    ('BORV', 'Боровицкая'),
    ('BORS', 'Боровское шоссе'),
    ('BTSD', 'Ботанический сад'),
    ('BRTS', 'Братиславская'),
    ('BVAU', 'Бульвар Адмирала Ушакова'),
    ('BVDD', 'Бульвар Дмитрия Донского'),
    ('BURS', 'Бульвар Рокоссовского'),
    ('BNAL', 'Бунинская аллея'),
    ('BUTR', 'Бутырская'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "В"
    ('VDNH', 'ВДНХ'),
    ('VRLB', 'Верхние Лихоборы'),
    ('VLDK', 'Владыкино'),
    ('VDST', 'Водный стадион'),
    ('VKVS', 'Войковская'),
    ('VLGP', 'Волгоградский проспект'),
    ('VOLZ', 'Волжская'),
    ('VLKL', 'Волоколамская'),
    ('VRBG', 'Воробьёвы горы'),
    ('VSTV', 'Выставочная'),
    ('VKHN', 'Выхино'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "Г"
    ('GOVR', 'Говорово'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "Д"
    ('DLVC', 'Деловой центр'),
    ('DNMO', 'Динамо'),
    ('DMIT', 'Дмитровская'),
    ('DOBR', 'Добрынинская'),
    ('DMDV', 'Домодедовская'),
    ('DSTV', 'Достоевская'),
    ('DUBR', 'Дубровка'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "Ж"
    ('ZHUL', 'Жулебино'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "З"
    ('ZYAB', 'Зябликово'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "И"
    ('IZML', 'Измайловская'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "К"
    ('KALU', 'Калужская'),
    ('KANT', 'Кантемировская'),
    ('KSHR', 'Каширская'),
    ('KVSA', 'Киевская (арб.-покр.)'),
    ('KVSF', 'Киевская (фил.)'),
    ('KVSK', 'Киевская (кольц.)'),
    ('KTGR', 'Китай-город (калуж.)'),
    ('KTGT', 'Китай-город (таган.)'),
    ('KOZH', 'Кожуховская'),
    ('KLMS', 'Коломенская'),
    ('KMSK', 'Комсомольская (кольц.)'),
    ('KMSS', 'Комсомольская (сокол.)'),
    ('KONK', 'Коньково'),
    ('KOSN', 'Косино'),
    ('KOTL', 'Котельники'),
    ('KRGV', 'Красногвардейская'),
    ('KRPR', 'Краснопресненская'),
    ('KRSL', 'Красносельская'),
    ('KRVR', 'Красные Ворота'),
    ('KRZS', 'Крестьянская застава'),
    ('KRPT', 'Кропоткинская'),
    ('KRLT', 'Крылатское'),
    ('KZNM', 'Кузнецкий Мост'),
    ('KZMN', 'Кузьминки'),
    ('KUNA', 'Кунцевская (арб.-покр.)'),
    ('KUNF', 'Кунцевская (фил.)'),
    ('KURA', 'Курская (арб.-покр.)'),
    ('KURK', 'Курская (кольц.)'),
    ('KTZV', 'Кутузовская'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "Л"
    ('LNPR', 'Ленинский проспект'),
    ('LRMP', 'Лермонтовский проспект'),
    ('LSPR', 'Лесопарковая'),
    ('LEFR', 'Лефортово'),
    ('LMSP', 'Ломоносовский проспект'),
    ('LBNK', 'Лубянка'),
    ('LUKH', 'Лухмановская'),
    ('LUBL', 'Люблино'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "М"
    ('MRSK', 'Марксистская'),
    ('MARR', 'Марьина Роща'),
    ('MARO', 'Марьино'),
    ('MAYK', 'Маяковская'),
    ('MDVD', 'Медведково'),
    ('MZDN', 'Международная'),
    ('MEND', 'Менделеевская'),
    ('MNSK', 'Минская'),
    ('MTNO', 'Митино'),
    ('MCHP', 'Мичуринский проспект'),
    ('MLDZ', 'Молодёжная'),
    ('MYAK', 'Мякинино'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "Н"
    ('NAGT', 'Нагатинская'),
    ('NAGR', 'Нагорная'),
    ('NAHP', 'Нахимовский проспект'),
    ('NEKR', 'Некрасовка'),
    ('NIZG', 'Нижегородская'),
    ('NVGR', 'Новогиреево'),
    ('NVKS', 'Новокосино'),
    ('NVKZ', 'Новокузнецкая'),
    ('NVPR', 'Новопеределкино'),
    ('NVSL', 'Новослободская'),
    ('NVYS', 'Новоясеневская'),
    ('NVCH', 'Новые Черёмушки'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "О"
    ('OZER', 'Озёрная'),
    ('OKRZ', 'Окружная'),
    ('OKSK', 'Окская'),
    ('OKTK', 'Октябрьская (кольц.)'),
    ('OKTR', 'Октябрьская (калуж.)'),
    ('OKTP', 'Октябрьское Поле'),
    ('OLKH', 'Ольховая'),
    ('ORHV', 'Орехово'),
    ('OTRD', 'Отрадное'),
    ('OHRD', 'Охотный Ряд'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "П"
    ('PVLZ', 'Павелецкая (змск.)'),
    ('PVLK', 'Павелецкая (кольц.)'),
    ('PRKU', 'Парк культуры(кольц.)'),
    ('PRKK', 'Парк культуры'),
    ('PPBA', 'Парк Победы (арб.-покр.)'),
    ('PPBS', 'Парк Победы (солнц.)'),
    ('PRTZ', 'Партизанская'),
    ('PRMS', 'Первомайская'),
    ('PERV', 'Перово'),
    ('PRMS', 'Петровско-Разумовская (серп.)'),
    ('PRML', 'Петровско-Разумовская (любл.)'),
    ('PECH', 'Печатники'),
    ('PION', 'Пионерская'),
    ('PLNR', 'Планерная'),
    ('PLIL', 'Площадь Ильича'),
    ('PLRV', 'Площадь Революции'),
    ('PLZV', 'Полежаевская'),
    ('POLK', 'Полянка'),
    ('PRZH', 'Пражская'),
    ('PRPL', 'Преображенская площадь'),
    ('PRKN', 'Прокшино'),
    ('PRLT', 'Пролетарская'),
    ('PRVR', 'Проспект Вернадского'),
    ('PMRK', 'Проспект Мира (кольц.)'),
    ('PMRR', 'Проспект Мира (калуж.)'),
    ('PRFS', 'Профсоюзная'),
    ('PUSH', 'Пушкинская'),
    ('PTCS', 'Пятницкое шоссе'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "Р"
    ('RAMN', 'Раменки'),
    ('RASS', 'Рассказовка'),
    ('RCVK', 'Речной вокзал'),
    ('RIZH', 'Рижская'),
    ('RIMS', 'Римская'),
    ('RMNC', 'Румянцево'),
    ('RYAZ', 'Рязанский проспект'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "С"
    ('SAVL', 'Савёловская'),
    ('SLRV', 'Саларьево'),
    ('SVIB', 'Свиблово'),
    ('SEVS', 'Севастопольская'),
    ('SLGR', 'Селигерская'),
    ('SMNV', 'Семёновская'),
    ('SERP', 'Серпуховская'),
    ('SLVB', 'Славянский бульвар'),
    ('SMLA', 'Смоленская (арб.-покр.)'),
    ('SMLF', 'Смоленская (фил.)'),
    ('SOKL', 'Сокол'),
    ('SKLN', 'Сокольники'),
    ('SOLN', 'Солнцево'),
    ('SPRK', 'Спартак'),
    ('SPRT', 'Спортивная'),
    ('SRTB', 'Сретенский бульвар'),
    ('STXN', 'Стахановская'),
    ('STRG', 'Строгино'),
    ('STUD', 'Студенческая'),
    ('SUHR', 'Сухаревская'),
    ('SHDN', 'Сходненская'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "Т"
    ('TGNR', 'Таганская'),
    ('TGNK', 'Таганская (кольц.)'),
    ('TVRS', 'Тверская'),
    ('TRTL', 'Театральная'),
    ('TXTL', 'Текстильщики'),
    ('THNP', 'Технопарк'),
    ('TPST', 'Тёплый Стан'),
    ('TIMR', 'Тимирязевская'),
    ('TRTR', 'Третьяковская (калуж.)'),
    ('TRTK', 'Третьяковская'),
    ('TRPR', 'Тропарёво'),
    ('TRBN', 'Трубная'),
    ('TULS', 'Тульская'),
    ('TURG', 'Тургеневская'),
    ('TUSH', 'Тушинская'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "У"
    ('1905', 'Улица 1905 года'),
    ('ULAY', 'Улица Академика Янгеля'),
    ('ULGR', 'Улица Горчакова'),
    ('ULDM', 'Улица Дмитриевского'),
    ('ULSK', 'Улица Скобелевская'),
    ('ULST', 'Улица Старокачаловская'),
    ('UNVR', 'Университет'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "Ф"
    ('FLTL', 'Филатов Луг'),
    ('FLPK', 'Филёвский парк'),
    ('FILI', 'Фили'),
    ('FONV', 'Фонвизинская'),
    ('FRNZ', 'Фрунзенская'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "Х"
    ('HVRN', 'Ховрино'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "Ц"
    ('CRCN', 'Царицыно'),
    ('CVBV', 'Цветной бульвар'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "Ч"
    ('CHRK', 'Черкизовская'),
    ('CHER', 'Чертановская'),
    ('CHEX', 'Чеховская'),
    ('CHPR', 'Чистые пруды'),
    ('CHKL', 'Чкаловская'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "Ш"
    ('SHAB', 'Шаболовская'),
    ('SPLV', 'Шипиловская'),
    ('SHEN', 'Шоссе Энтузиастов'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "Щ"
    ('SHEL', 'Щёлковская'),
    ('SHUK', 'Щукинская'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "Э"
    ('ELZA', 'Электрозаводская (арб.-покр.)'),
    ('ELZN', 'Электрозаводская (некр.)'),

    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "Ю"
    ('UGVS', 'Юго-Восточная'),
    ('UGZP', 'Юго-Западная'),
    ('UZHN', 'Южная'),
    # СТАНЦИИ МОСКОВСКОГО МЕТРО НА БУКВУ "Я"
    ('YASN', 'Ясенево'),

]