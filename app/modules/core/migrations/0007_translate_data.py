from django.db import migrations

# Translations keyed by the Russian source value. Applied only to rows whose
# *_ru field matches the key, so it is safe to re-run and won't clobber rows
# that already differ. Personal names are intentionally left as-is (kk == en == ru).

ABOUT_SECTION = {
    'title': {
        'О КОМПАНИИ': ('КОМПАНИЯ ТУРАЛЫ', 'ABOUT US'),
    },
    'description': {
        'Мы проводим геологическое изучение недр Казахстана, обеспечивая решение геологических задач в различных отраслях недропользования. Компания располагает квалифицированными кадрами, экспертизой, опытом и финансовой устойчивостью для оперативного и безопасного выполнения проектов.': (
            'Біз Қазақстан жер қойнауын геологиялық зерттеуді жүргізіп, жер қойнауын пайдаланудың әртүрлі салаларында геологиялық міндеттердің шешілуін қамтамасыз етеміз. Компанияда жобаларды жедел әрі қауіпсіз орындау үшін білікті кадрлар, сараптама, тәжірибе және қаржылық тұрақтылық бар.',
            'We conduct geological exploration of Kazakhstan’s subsoil, addressing geological challenges across various sectors of subsoil use. The company has qualified personnel, expertise, experience and financial stability to deliver projects promptly and safely.'),
    },
    'main_stat_description': {
        'Более 80 млрд тенге — общий объём государственного финансирования': (
            '80 млрд теңгеден астам — мемлекеттік қаржыландырудың жалпы көлемі',
            'Over KZT 80 billion — total state financing'),
    },
    'main_stat_value': {},
}

ABOUT_STAT = {
    'description': {
        'Более 200+ специалистов и экспертов': ('200+ маман мен сарапшыдан астам', 'Over 200+ specialists and experts'),
        'Работаем во всех регионах страны': ('Елдің барлық өңірлерінде жұмыс істейміз', 'We operate in all regions of the country'),
        'Более 16 проектов с момента основания': ('Құрылғаннан бері 16-дан астам жоба', 'Over 16 projects since founding'),
        'Собственные буровые станки': ('Меншікті бұрғылау қондырғылары', 'Own drilling rigs'),
    },
    'label': {
        'СПЕЦИАЛИСТОВ': ('МАМАН', 'SPECIALISTS'),
        'РЕГИОНОВ': ('ӨҢІР', 'REGIONS'),
        'ПРОЕКТОВ': ('ЖОБА', 'PROJECTS'),
        'СТАНКОВ': ('ҚОНДЫРҒЫ', 'RIGS'),
    },
    'value': {},
}

ABOUT_EVENT = {
    'date_label': {
        '21 июня 2011': ('2011 жылғы 21 маусым', '21 June 2011'),
        '30 декабря 2021': ('2021 жылғы 30 желтоқсан', '30 December 2021'),
        '8 сентября 2023': ('2023 жылғы 8 қыркүйек', '8 September 2023'),
        '14 сентября 2023': ('2023 жылғы 14 қыркүйек', '14 September 2023'),
    },
    'title': {
        'Основание компании': ('Компанияның құрылуы', 'Founding of the company'),
        'Переход под управление Самрук-Қазына': ('Самұрық-Қазына басқаруына өту', 'Transfer to Samruk-Kazyna management'),
        'Передача 100% акций в Самрук-Қазына': ('Акциялардың 100%-ын Самұрық-Қазынаға беру', 'Transfer of 100% of shares to Samruk-Kazyna'),
        'Передача голосующих акций в Тау-Кен Самрук': ('Дауыс беретін акцияларды Тау-Кен Самұрыққа беру', 'Transfer of voting shares to Tau-Ken Samruk'),
    },
    'description': {
        'Постановлением Правительства РК №684 от 21 июня 2011 года АО «Казгеология» создано как высокотехнологичная геологоразведочная компания Республики Казахстан.': (
            'ҚР Үкіметінің 2011 жылғы 21 маусымдағы №684 қаулысымен «Қазгеология» АҚ Қазақстан Республикасының жоғары технологиялық геологиялық барлау компаниясы ретінде құрылды.',
            'By Resolution of the Government of the RK No. 684 dated 21 June 2011, Kazgeology JSC was established as a high-tech geological exploration company of the Republic of Kazakhstan.'),
        'Постановлением Правительства РК №971 от 30 декабря 2021 года принято решение о передаче акций компании в АО «Фонд национального благосостояния «Самрук-Қазына».': (
            'ҚР Үкіметінің 2021 жылғы 30 желтоқсандағы №971 қаулысымен компания акцияларын «Самұрық-Қазына» ұлттық әл-ауқат қоры» АҚ-ға беру туралы шешім қабылданды.',
            'By Resolution of the Government of the RK No. 971 dated 30 December 2021, a decision was made to transfer the company’s shares to Samruk-Kazyna Sovereign Wealth Fund JSC.'),
        'Приказом Председателя Комитета государственного имущества и приватизации Министерства финансов РК №650 от 8 сентября 2023 года осуществлена передача 100% акций компании в собственность АО «ФНБ «Самрук-Қазына».': (
            'ҚР Қаржы министрлігі Мемлекеттік мүлік және жекешелендіру комитеті Төрағасының 2023 жылғы 8 қыркүйектегі №650 бұйрығымен компания акцияларының 100%-ы «Самұрық-Қазына» ҰӘҚ» АҚ меншігіне берілді.',
            'By Order of the Chairman of the State Property and Privatization Committee of the Ministry of Finance of the RK No. 650 dated 8 September 2023, 100% of the company’s shares were transferred to the ownership of Samruk-Kazyna SWF JSC.'),
        'На основании договора №1707-И от 14 сентября 2023 года произведена передача 100% голосующих акций АО «Казгеология» от АО «ФНБ «Самрук-Қазына» в АО «НГК «Тау-Кен Самрук».': (
            '2023 жылғы 14 қыркүйектегі №1707-И шарт негізінде «Қазгеология» АҚ дауыс беретін акцияларының 100%-ы «Самұрық-Қазына» ҰӘҚ» АҚ-дан «Тау-Кен Самұрық» ҰТК» АҚ-ға берілді.',
            'Under Agreement No. 1707-I dated 14 September 2023, 100% of the voting shares of Kazgeology JSC were transferred from Samruk-Kazyna SWF JSC to Tau-Ken Samruk NMC JSC.'),
    },
}

BOARD_MEMBER = {
    'role': {
        'Председатель': ('Төраға', 'Chairman'),
        'Член СД — Представитель Единственного акционера': ('ДК мүшесі — Жалғыз акционердің өкілі', 'Board member — Representative of the Sole Shareholder'),
        'Член СД — Генеральный директор': ('ДК мүшесі — Бас директор', 'Board member — General Director'),
        'Член СД — Независимый директор': ('ДК мүшесі — Тәуелсіз директор', 'Board member — Independent Director'),
    },
}

BOARD_SECRETARY = {
    'label': {
        'ВРИО Корпоративного секретаря': ('Корпоративтік хатшының м.а.', 'Acting Corporate Secretary'),
    },
}

BOARD_COMMITTEE = {
    'title': {
        'Комитет по стратегическому планированию, инвестициям и устойчивому развитию': ('Стратегиялық жоспарлау, инвестициялар және орнықты даму комитеті', 'Committee for Strategic Planning, Investment and Sustainable Development'),
        'Комитет по кадрам, вознаграждениям и социальным вопросам': ('Кадрлар, сыйақылар және әлеуметтік мәселелер комитеті', 'Committee for HR, Remuneration and Social Affairs'),
        'Комитет по аудиту': ('Аудит комитеті', 'Audit Committee'),
    },
    'count_label': {
        '3 человека': ('3 адам', '3 members'),
    },
}

BOARD_CM = {
    'role_label': {
        'Председатель': ('Төраға', 'Chairman'),
    },
    'note': {
        'независимый директор': ('тәуелсіз директор', 'independent director'),
        'представитель ЕА': ('ЖА өкілі', 'representative of the Sole Shareholder'),
    },
}

ORGUNIT = {
    'name': {
        'Совет директоров': ('Директорлар кеңесі', 'Board of Directors'),
        'Генеральный директор': ('Бас директор', 'General Director'),
    },
}

CORP_EVENT = {
    'title': {
        'Принятие Советом директоров Общества решении о заключении сделки в совершении которых акционерным обществом имеется заинтересованность': (
            'Қоғамның Директорлар кеңесінің акционерлік қоғам мүдделі болатын мәмілені жасасу туралы шешім қабылдауы',
            'Adoption by the Company’s Board of Directors of a decision to conclude a related-party transaction'),
        'Заключение сделками, в совершении которых акционерным обществом имеется заинтересованность': (
            'Акционерлік қоғам мүдделі болатын мәмілелерді жасасу',
            'Conclusion of related-party transactions'),
        'Информация об избрании Совета директоров АО "Казгеология"': (
            '«Қазгеология» АҚ Директорлар кеңесін сайлау туралы ақпарат',
            'Information on the election of the Board of Directors of Kazgeology JSC'),
        'Информация о списке, и (или) об изменении в списке организаций, в которых эмитент обладает десятью и более процентами акций (долей, паев) каждой такой организации': (
            'Эмитент әрбір осындай ұйым акцияларының (үлестерінің, пайларының) он және одан да көп пайызына иелік ететін ұйымдар тізбесі және (немесе) ондағы өзгерістер туралы ақпарат',
            'Information on the list of, and/or changes to the list of, organizations in which the issuer holds ten or more percent of the shares (interests, units) of each such organization'),
    },
}

PRIVACY = {
    'hero_label': {'АО «Казгеология»': ('«Қазгеология» АҚ', 'Kazgeology JSC')},
    'hero_title': {'ПОЛИТИКА\nКОНФИДЕНЦИАЛЬНОСТИ': ('ҚҰПИЯЛЫЛЫҚ\nСАЯСАТЫ', 'PRIVACY\nPOLICY')},
    'hero_subtitle': {'Порядок обработки и защиты персональных данных пользователей сайта.': ('Сайт пайдаланушыларының дербес деректерін өңдеу және қорғау тәртібі.', 'Procedure for processing and protecting personal data of website users.')},
    'document_title': {'Политика конфиденциальности': ('Құпиялылық саясаты', 'Privacy Policy')},
    'updated_date': {'28 мая 2026': ('2026 жылғы 28 мамыр', '28 May 2026')},
    'intro_text': {'Настоящая Политика конфиденциальности определяет порядок сбора, хранения, использования и защиты персональных данных пользователей сайта АО «Казгеология».': (
        'Осы Құпиялылық саясаты «Қазгеология» АҚ сайты пайдаланушыларының дербес деректерін жинау, сақтау, пайдалану және қорғау тәртібін айқындайды.',
        'This Privacy Policy defines the procedure for collecting, storing, using and protecting the personal data of users of the Kazgeology JSC website.')},
}

PRIVACY_SECTION = {
    'title': {
        '1. Общие положения': ('1. Жалпы ережелер', '1. General provisions'),
        '2. Какие данные могут обрабатываться': ('2. Қандай деректер өңделуі мүмкін', '2. What data may be processed'),
        '3. Цели обработки данных': ('3. Деректерді өңдеу мақсаттары', '3. Purposes of data processing'),
        '4. Передача данных третьим лицам': ('4. Деректерді үшінші тұлғаларға беру', '4. Transfer of data to third parties'),
        '5. Хранение и защита данных': ('5. Деректерді сақтау және қорғау', '5. Data storage and protection'),
        '6. Права пользователя': ('6. Пайдаланушының құқықтары', '6. User rights'),
        '7. Изменение политики': ('7. Саясатты өзгерту', '7. Changes to the policy'),
    },
    'content': {
        'Компания может обрабатывать следующие сведения:': ('Компания келесі мәліметтерді өңдей алады:', 'The company may process the following information:'),
        'Персональные данные используются для:': ('Дербес деректер мыналар үшін пайдаланылады:', 'Personal data is used for:'),
        'Компания не передает персональные данные третьим лицам без согласия пользователя, за исключением случаев, предусмотренных законодательством, либо когда такая передача необходима для обработки обращения пользователя.': (
            'Компания пайдаланушының келісімінсіз дербес деректерді үшінші тұлғаларға бермейді, заңнамада көзделген жағдайларды немесе мұндай беру пайдаланушының өтінішін өңдеу үшін қажет болатын жағдайларды қоспағанда.',
            'The company does not transfer personal data to third parties without the user’s consent, except as provided by law or when such transfer is necessary to process the user’s request.'),
        'Данные хранятся в течение срока, необходимого для достижения целей обработки, если иной срок не установлен законодательством. Компания применяет разумные меры защиты от несанкционированного доступа, изменения, раскрытия или уничтожения информации.': (
            'Деректер өңдеу мақсаттарына жету үшін қажетті мерзім ішінде сақталады, егер заңнамада өзге мерзім белгіленбесе. Компания ақпаратқа рұқсатсыз қол жеткізуден, өзгертуден, ашудан немесе жоюдан қорғаудың ақылға қонымды шараларын қолданады.',
            'Data is stored for the period necessary to achieve the processing purposes, unless another period is established by law. The company applies reasonable measures to protect against unauthorized access, alteration, disclosure or destruction of information.'),
        'Пользователь вправе запросить информацию об обработке своих данных, а также обратиться с просьбой:': (
            'Пайдаланушы өз деректерінің өңделуі туралы ақпаратты сұратуға, сондай-ақ мынадай өтінішпен жүгінуге құқылы:',
            'The user has the right to request information about the processing of their data, as well as to request:'),
        'Компания может обновлять настоящую Политику. Актуальная редакция размещается на этой странице и применяется с момента публикации, если в тексте не указано иное.': (
            'Компания осы Саясатты жаңартып отыруы мүмкін. Өзекті редакция осы бетте орналастырылады және мәтінде өзгеше көрсетілмесе, жарияланған сәттен бастап қолданылады.',
            'The company may update this Policy. The current version is posted on this page and applies from the moment of publication, unless otherwise stated.'),
    },
    'list_items': {
        'имя, адрес электронной почты, номер телефона и текст обращения;\nтехнические данные: IP-адрес, тип браузера, дата и время посещения;\nинформацию, которую пользователь добровольно передает через формы': (
            'аты, электрондық пошта мекенжайы, телефон нөмірі және өтініш мәтіні;\nтехникалық деректер: IP-мекенжай, браузер түрі, кіру күні мен уақыты;\nпайдаланушы нысандар арқылы өз еркімен беретін ақпарат',
            'name, email address, phone number and the text of the request;\ntechnical data: IP address, browser type, date and time of visit;\ninformation that the user voluntarily provides through forms'),
        'обработки обращений и предоставления ответа пользователю;\nобеспечения корректной и безопасной работы сайта;\nвыполнения требований законодательства Республики Казахстан;\nулучшения качества информационных услуг': (
            'өтініштерді өңдеу және пайдаланушыға жауап беру;\nсайттың дұрыс әрі қауіпсіз жұмысын қамтамасыз ету;\nҚазақстан Республикасы заңнамасының талаптарын орындау;\nақпараттық қызметтер сапасын арттыру',
            'processing requests and providing a response to the user;\nensuring correct and secure operation of the website;\ncomplying with the legislation of the Republic of Kazakhstan;\nimproving the quality of information services'),
        'уточнить или обновить персональные данные;\nпрекратить обработку данных, если для этого есть законные основания;\nполучить разъяснение по вопросам защиты персональных данных.': (
            'дербес деректерді нақтылау немесе жаңарту;\nзаңды негіздер болған жағдайда деректерді өңдеуді тоқтату;\nдербес деректерді қорғау мәселелері бойынша түсініктеме алу.',
            'clarify or update personal data;\nstop data processing if there are legitimate grounds for it;\nobtain clarification on personal data protection matters.'),
    },
}


def apply_map(obj, field, mapping):
    ru = getattr(obj, field + '_ru', None) or getattr(obj, field, None)
    if ru in mapping:
        kk, en = mapping[ru]
        cur_kk = getattr(obj, field + '_kk', None)
        cur_en = getattr(obj, field + '_en', None)
        # Overwrite when empty OR still equal to the Russian source (a leftover
        # from `update_translation_fields`, which copies ru into every language).
        if not cur_kk or cur_kk == ru:
            setattr(obj, field + '_kk', kk)
        if not cur_en or cur_en == ru:
            setattr(obj, field + '_en', en)
        return True
    return False


def translate(apps, schema_editor):
    specs = [
        ('about', 'AboutSection', ABOUT_SECTION),
        ('about', 'AboutStatistic', ABOUT_STAT),
        ('about', 'AboutHistoryEvent', ABOUT_EVENT),
        ('board', 'BoardMember', BOARD_MEMBER),
        ('board', 'BoardSecretary', BOARD_SECRETARY),
        ('board', 'BoardCommittee', BOARD_COMMITTEE),
        ('board', 'BoardCommitteeMember', BOARD_CM),
        ('core', 'OrgUnit', ORGUNIT),
        ('core', 'CorporateEvent', CORP_EVENT),
        ('core', 'PrivacyPolicy', PRIVACY),
        ('core', 'PrivacyPolicySection', PRIVACY_SECTION),
    ]
    for app_label, model_name, field_maps in specs:
        Model = apps.get_model(app_label, model_name)
        for obj in Model.objects.all():
            changed = False
            for field, mapping in field_maps.items():
                if mapping and apply_map(obj, field, mapping):
                    changed = True
            if changed:
                obj.save()

    # Personal names: keep identical across languages (kk == en == ru) so they
    # never appear blank when modeltranslation has no fallback configured.
    for app_label, model_name in [('board', 'BoardMember'), ('board', 'BoardSecretary'),
                                  ('board', 'BoardCommitteeMember')]:
        Model = apps.get_model(app_label, model_name)
        for obj in Model.objects.all():
            ru = getattr(obj, 'full_name_ru', None) or getattr(obj, 'full_name', None)
            changed = False
            if ru and not getattr(obj, 'full_name_kk', None):
                obj.full_name_kk = ru; changed = True
            if ru and not getattr(obj, 'full_name_en', None):
                obj.full_name_en = ru; changed = True
            if changed:
                obj.save()


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_corporateevent_title_en_corporateevent_title_kk_and_more'),
        ('about', '0004_abouthistoryevent_date_label_en_and_more'),
        ('board', '0004_boardcommittee_count_label_en_and_more'),
    ]

    operations = [
        migrations.RunPython(translate, noop),
    ]
