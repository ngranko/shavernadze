HEADER_NAME = 'headerName'
KEY_NAME = 'keyName'
RESPONSE_PATH = 'responsePath'

dataMappings = [
    {
        HEADER_NAME: 'Название',
        KEY_NAME: 'name',
        RESPONSE_PATH: ['name'],
    },
    {
        HEADER_NAME: 'Адрес',
        KEY_NAME: 'address',
        RESPONSE_PATH: ['formatted_address'],
    },
    {
        HEADER_NAME: 'Район',
        KEY_NAME: 'district',
        RESPONSE_PATH: [
            'plus_code',
            'compound_code'
        ],
    },
    {
        HEADER_NAME: 'Рейтинг',
        KEY_NAME: 'rating',
        RESPONSE_PATH: ['rating'],
    },
    {
        HEADER_NAME: 'Уровень цен',
        KEY_NAME: 'price_level',
        RESPONSE_PATH: ['price_level'],
    },
]
