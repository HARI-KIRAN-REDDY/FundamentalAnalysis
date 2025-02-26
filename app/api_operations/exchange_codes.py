def get_exchange_country(exchange_code):
    exchange_mapping = {
        # India
        "NSE": ("India", "https://flagcdn.com/w320/in.png"),
        "NSI": ("India", "https://flagcdn.com/w320/in.png"),
        "BSE": ("India", "https://flagcdn.com/w320/in.png"),
        "BOM": ("India", "https://flagcdn.com/w320/in.png"),  # Bombay Stock Exchange

        # USA
        "NYSE": ("USA", "https://flagcdn.com/w320/us.png"),
        "NYQ": ("USA", "https://flagcdn.com/w320/us.png"),  # NYSE (Yahoo Finance)
        "NASDAQ": ("USA", "https://flagcdn.com/w320/us.png"),
        "NMS": ("USA", "https://flagcdn.com/w320/us.png"),  # Nasdaq (Yahoo Finance)
        "AMEX": ("USA", "https://flagcdn.com/w320/us.png"),  # American Stock Exchange

        # Canada
        "TSE": ("Canada", "https://flagcdn.com/w320/ca.png"),
        "TSX": ("Canada", "https://flagcdn.com/w320/ca.png"),
        "VAN": ("Canada", "https://flagcdn.com/w320/ca.png"),  # TSX Venture Exchange

        # United Kingdom & Europe
        "LSE": ("United Kingdom", "https://flagcdn.com/w320/gb.png"),
        "LON": ("United Kingdom", "https://flagcdn.com/w320/gb.png"),  # London Stock Exchange
        "EURONEXT": ("Europe", "https://flagcdn.com/w320/eu.png"),
        "AMS": ("Netherlands", "https://flagcdn.com/w320/nl.png"),  # Amsterdam Exchange
        "BRU": ("Belgium", "https://flagcdn.com/w320/be.png"),
        "PAR": ("France", "https://flagcdn.com/w320/fr.png"),
        "XETRA": ("Germany", "https://flagcdn.com/w320/de.png"),
        "FRA": ("Germany", "https://flagcdn.com/w320/de.png"),  # Frankfurt Stock Exchange

        # Asia
        "HKEX": ("Hong Kong", "https://flagcdn.com/w320/hk.png"),
        "HKG": ("Hong Kong", "https://flagcdn.com/w320/hk.png"),
        "SGX": ("Singapore", "https://flagcdn.com/w320/sg.png"),
        "SES": ("Singapore", "https://flagcdn.com/w320/sg.png"),
        "ASX": ("Australia", "https://flagcdn.com/w320/au.png"),
        "JPX": ("Japan", "https://flagcdn.com/w320/jp.png"),
        "TYO": ("Japan", "https://flagcdn.com/w320/jp.png"),  # Tokyo Stock Exchange
        "SSE": ("China", "https://flagcdn.com/w320/cn.png"),
        "SHH": ("China", "https://flagcdn.com/w320/cn.png"),
        "SZSE": ("China", "https://flagcdn.com/w320/cn.png"),
        "KRX": ("South Korea", "https://flagcdn.com/w320/kr.png"),
        "KOSPI": ("South Korea", "https://flagcdn.com/w320/kr.png"),  # KOSPI Index
        "TWSE": ("Taiwan", "https://flagcdn.com/w320/tw.png"),

        # Other Markets
        "BME": ("Spain", "https://flagcdn.com/w320/es.png"),  # Bolsa de Madrid
        "MOEX": ("Russia", "https://flagcdn.com/w320/ru.png"),  # Moscow Exchange
        "SA": ("Brazil", "https://flagcdn.com/w320/br.png"),  # B3 (Brasil, Bolsa, Balcão)
        "SN": ("Chile", "https://flagcdn.com/w320/cl.png"),  # Bolsa de Comercio de Santiago
        "JOH": ("South Africa", "https://flagcdn.com/w320/za.png"),  # Johannesburg Stock Exchange
    }

    return exchange_mapping.get(exchange_code.upper(),
                                ("Unknown Exchange Code", "https://flagcdn.com/w320/unknown.png"))

